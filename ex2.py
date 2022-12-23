#!/usr/bin/env python
# coding: utf-8

from random import randint
import os


def match_phase_groupe():
    """
    Ouvre les fichiers équipes_groupe.csv.
    Créer les matches possible du groupe en leurs attibuants un score de 0 à 3.

    Returns
    -------
    None.

    """
    for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        with open("Equipes\équipes_groupe_" + str(i) + ".csv", "r", encoding="utf8") as fichier_équipe:
            liste_groupe = [line.strip() for line in fichier_équipe]

        # Création des rencontre du groupe
        filename = r"Matchs\matchs_groupe_" + str(i) + ".csv"

        # Vérifie que le dossier Matchs existe
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "a", encoding="utf8") as fichier_matchs:
            for e in liste_groupe:
                for e2 in liste_groupe:
                    if e > e2:
                        score_1 = randint(0, 3)
                        score_2 = randint(0, 3)
                        fichier_matchs.write(f"{e},{score_1},{e2},{score_2}\n")
