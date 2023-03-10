#!/usr/bin/env python
# coding: utf-8


import os
from ex1 import creation_groupe
from ex2 import match_phase_groupe
from ex3 import comptage_points_groupe
from ex4 import classement_poule
from ex5 import huitième, quart, demi, petite_finale, finale, liste_phase_final


def supprime_dossiers():
    liste_dossier = ["Equipes", "Matchs", "Points", "Phase Final"]
    for dossier in liste_dossier:
        for file in os.listdir(dossier):
            # print(f"{file} removed...")
            os.remove(f"{dossier}\{file}")


def afficher_groupe(classement):
    liste_lettres = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in liste_lettres:
        print(f"\nGroupe {i}")
        for e in classement[liste_lettres.index(i)]:
            print(e)
    print("\n")


def affichage_phase_finale(nom_phase):
    print(f"{nom_phase.upper()}:\n")
    l = liste_phase_final(fr"Phase Final\résultats_{nom_phase}.csv")[1]
    for i in range(len(l)):
        print(f"{l[i][0]} vs {l[i][2]}")
        if i == 1 or i == 3 or i == 5:
            print()


def afficher_phases_finales():
    liste_phase_finale = ["huitièmes", "quart", "demi", "3e_place", "finale"]
    for phase in liste_phase_finale:
        affichage_phase_finale(phase)
        print("\n")


def afficher_classement():
    premier = liste_phase_final(r"Phase Final\résultats_finale.csv")[0][0]
    troisième = liste_phase_final(r"Phase Final\résultats_3e_place.csv")[0][0]

    ligne_petite_finale = liste_phase_final(
        r"Phase Final\résultats_finale.csv")[1][0]

    if ligne_petite_finale[1] == "gagné":
        deuxième = ligne_petite_finale[2]
    else:
        deuxième = ligne_petite_finale[0]

    print("Premier :", premier)
    print("Deuxième :", deuxième)
    print("Troisième :", troisième)


try:
    supprime_dossiers()
except FileNotFoundError:
    pass

creation_groupe()
match_phase_groupe()
comptage_points_groupe()
classement = classement_poule()
huitième()
quart()
demi()
petite_finale()
finale()


afficher_groupe(classement)
afficher_phases_finales()
afficher_classement()
