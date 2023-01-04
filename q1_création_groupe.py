#!/usr/bin/env python
# coding: utf-8

from random import choice
import os


def creation_liste_equipe():
    """Ouvre liste_equipes.csv

    Returns
    -------
    equipe : list
             Listes des équipes.

    """
    equipe = []
    with open("liste_equipes.csv", "r", encoding="utf8") as f:
        for line in f:
            equipe.append(line.strip())
    return equipe


def creation_groupe():
    """
    Créer groupes de poules
    Ecrit les groupes dans un fichier de type équipe_groupe_lettregroupe.csv.

    Returns
    -------
    None.

    """
    equipe = creation_liste_equipe()
    for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        for _ in range(4):
            filename = r"Equipes\équipes_groupe_" + str(i) + ".csv"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "a", encoding="utf8") as f:
                nom_equipe = choice(equipe)
                f.write(nom_equipe + "\n")
                equipe.remove(nom_equipe)
