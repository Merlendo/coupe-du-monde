#!/usr/bin/env python
# coding: utf-8

from random import randint, random
from math import tanh


def match_phase_final(équipe_1, équipe_2):
    """
    Choisi un gagnant entre deux équipes

    Parameters
    ----------
    équipe_1 : str
               Equipe 1.
    équipe_2 : str
               Equipe 2.

    Returns
    -------
    str
        Retourne une f string.
    """
    choix = randint(0, 1)
    if choix == 0:
        return f"{équipe_1},gagné,{équipe_2},perdu"
    else:
        return f"{équipe_1},perdu,{équipe_2},gagné"


def équipe_résultat(e, résultat):
    """
    Determine le gagnant ou le perdant d'un match

    Parameters
    ----------
    e : str
        String contenant le résultat d'un match.
    résultat : str
               String pouvant être "gagné" ou "perdu".

    Returns
    -------
    str
        Retourne l'équipe qui a gagné ou perdu.
    """
    if e[1] == résultat:
        return e[0]
    elif e[3] == résultat:
        return e[2]


def liste_huitième():
    """
    Ouvre le fichier équipes_qualifiés.csv

    Returns
    -------
    list
        Retourn la listes des équipes qualifiés.

    """
    with open("Phase Final\équipes_qualifiés.csv", "r", encoding="utf8") as fichier_qualifié:
        return [line.strip() for line in fichier_qualifié]


def liste_huitième_triée():
    """
    Appel la fonction liste_huitième() et tries les équipes en suivant les
    règles de la fifa.

    Returns
    -------
    list
        Renvoi la listes des équipes qualifiées au huitième dans le bonne ordre.

    """
    équipes_huitième = liste_huitième()

    g1 = []
    g2 = []
    taille = len(équipes_huitième)

    for i in range(0, taille-1, 4):
        g1.append(équipes_huitième[i])
        g1.append(équipes_huitième[i+3])

    for i in range(0, taille-1, 4):
        g2.append(équipes_huitième[i+1])
        g2.append(équipes_huitième[i+2])

    return g1 + g2


def liste_phase_final(résultat_csv):
    with open(résultat_csv, "r", encoding="utf8") as fichier_qualifié:
        équipes = [line.strip().split(",") for line in fichier_qualifié]
    return [équipe_résultat(e, "gagné") for e in équipes], équipes


def phase_finale(phase_précédente, phase_suivante):
    équipes = liste_phase_final(phase_précédente)[0]
    taille = len(équipes)

    for i in range(0, taille, 2):
        équipe_1 = équipes[i]
        équipe_2 = équipes[i+1]

        with open(phase_suivante, "a", encoding="utf8") as fichié_phase_final:
            fichié_phase_final.write(
                f"{match_phase_final(équipe_1, équipe_2)}\n")


def huitième():
    équipes = liste_huitième_triée()
    taille = len(équipes)

    for i in range(0, taille, 2):
        équipe_1 = équipes[i]
        équipe_2 = équipes[i+1]

        with open(r"Phase Final\résultats_huitièmes.csv", "a", encoding="utf8") as fichié_huitième:
            fichié_huitième.write(
                f"{match_phase_final(équipe_1, équipe_2)}\n")


def quart():
    phase_finale(r"Phase Final\résultats_huitièmes.csv",
                 r"Phase Final\résultats_quart.csv")


def demi():
    phase_finale(r"Phase Final\résultats_quart.csv",
                 r"Phase Final\résultats_demi.csv")


def petite_finale():
    with open(r"Phase Final\résultats_demi.csv", "r", encoding="utf8") as fichier_non_qualifié:
        équipes = [line.strip().split(",") for line in fichier_non_qualifié]

    équipe_liste = [équipe_résultat(e, "perdu") for e in équipes]
    taille = len(équipe_liste)

    for i in range(0, taille, 2):
        équipe_1 = équipe_liste[i]
        équipe_2 = équipe_liste[i+1]

        with open(r"Phase Final\résultats_3e_place.csv", "a", encoding="utf8") as fichié_3e:
            fichié_3e.write(
                f"{match_phase_final(équipe_1, équipe_2)}\n")


def finale():
    phase_finale(r"Phase Final\résultats_demi.csv",
                 r"Phase Final\résultats_finale.csv")
