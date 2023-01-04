#!/usr/bin/env python
# coding: utf-8

from operator import itemgetter
import os


def classement_poule():
    """
    Classes les équipes des poules.
    Classement : Nombre de points -> Nombre de points -> Différence de buts -> nombre de but

    Returns
    -------
    classement_poule : list
                       Renvoie le classement de toutes les poules pour faciliter l'affichage.

    """
    classement_poule = []
    for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        with open("Points\points_groupe_" + str(i) + ".csv", "r", encoding="utf8") as fichier_point:
            equipe_groupe = []

            for line in fichier_point:
                equipe = []
                l = line.strip().split(",")
                nom = l[0]
                point = int(l[1])
                difference_but = int(l[2])
                nombre_de_but = int(l[3])
                equipe = [nom, point, difference_but, nombre_de_but]
                equipe_groupe.append(equipe)

        classement = sorted(
            equipe_groupe, key=itemgetter(1, 2, 3), reverse=True)
        classement_poule.append(classement)

        # Vérifie que le dossier Phase Final existe
        filename = r"Phase Final\équipes_qualifiés.csv"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Ecrit les deux premières équipes dans le fichier équipes_qualifiés.csv
        for i in range(2):
            with open(filename, "a", encoding="utf8") as fichier_qualifié:
                fichier_qualifié.write(f"{classement[i][0]}\n")

    return classement_poule
