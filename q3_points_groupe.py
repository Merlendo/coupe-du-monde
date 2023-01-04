#!/usr/bin/env python
# coding: utf-8

import os


def resultat_match(L):
    """
    Prends la ligne de résultat match et retournent les statistiques du match pour les deux équipes. 

    Parameters
    ----------
    L : list
        Prends en paramètre une ligne de resultat de match.

    Returns
    -------
    list
        Retourne : [nombre de point, différence de but, nombre de but] de l'équipe 1.
    list
        Retourne : [nombre de point, différence de but, nombre de but] de l'équipe 2.

    """

    équipe_1 = L[0]
    buts_1 = int(L[1])
    équipe_2 = L[2]
    buts_2 = int(L[3])

    if buts_1 > buts_2:
        return [équipe_1, 3, buts_1-buts_2, buts_1], [équipe_2, 0, buts_2-buts_1, buts_2]

    elif buts_1 < buts_2:
        return [équipe_1, 0, buts_1-buts_2, buts_1], [équipe_2, 3, buts_2-buts_1, buts_2]

    else:
        return [équipe_1, 1, buts_1-buts_2, buts_1], [équipe_2, 1, buts_2-buts_1, buts_2]


def comptage_points_groupe():
    """
    Créer un fichier de type points_groupe_lettregroupe.csv.
    Ces fichiers contiennent : Nom équipe, nombre de points, différence de buts, nombre de but

    Returns
    -------
    None.

    """
    for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        with open("Matchs\matchs_groupe_" + str(i) + ".csv", "r", encoding="utf8") as fichier_match:
            l_fichier_match = [line.strip().split(",")
                               for line in fichier_match]

        with open("Equipes\équipes_groupe_" + str(i) + ".csv", "r", encoding="utf8") as fichier_equipes:
            l_equipe = [line.strip() for line in fichier_equipes]

        # Créer une listes de listes temporaires avec toutes les données des matchs
        raw = []
        for e in l_fichier_match:
            l1, l2 = resultat_match(e)
            raw.append(l1)
            raw.append(l2)

        # Vérifie que le dossier Points est bien créé
        filename = r"Points\points_groupe_" + str(i) + ".csv"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Ajoutes les données des matchs par équipe
        for equipe in l_equipe:
            ligne = [equipe, 0, 0, 0]
            for e in raw:
                if e[0] == equipe:
                    ligne[1] += e[1]
                    ligne[2] += e[2]
                    ligne[3] += e[3]

            # Ecrit la ligne dans le fichier points_groupe
            with open(filename, "a", encoding="utf8") as fichier_points:
                fichier_points.write(
                    f"{ligne[0]},{ligne[1]},{ligne[2]},{ligne[3]}\n")
