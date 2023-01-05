#!/usr/bin/env python
# coding: utf-8

import os
from q5_phase_finale.py import match


def match_phase_groupe():
    """
    Ouvre les fichiers équipes_groupe.csv.
    Créer les matches possibles du groupe en leurs attibuants un score de 0 à 3.

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
                        
                        score_1 = 0
                        score_2 = 0
                        
                        # Utilise la fonction match pour générer des buts
                        for _ in range(3):
                            probabilité_but_e1 = match(e, e2)
                            if probabilité_but_e1 == e:
                                score_1 += 1
                
                            probabilité_but_e2 = match(e, e2)
                            if probabilité_but_e2 == e2:
                                score_2 += 1
                                
                        fichier_matchs.write(f"{e},{score_1},{e2},{score_2}\n")
