#!/usr/bin/env python
# coding: utf-8

from random import randint, random
from math import tanh

# Implémentation poids équipes
# ------------------------------------------------------------------------------------------------- #
def liste_classement_équipes():
    """
    Ouvre le fichier classement_équipes.csv et retourne un dictionnaire.

    Returns
    -------
    dict
        Dictionnaire contenant la valeur de chaques équipes.
    """
    with open("classement_équipes.csv", "r", encoding="utf8") as f:
        l = [[line.strip().split(",")[0], float(line.strip().split(",")[1])]
             for line in f]
        return {k: v for k, v in l}


def match(A, B, affichage=False):
    """
     Choisi un gagnant entre deux équipes
   
     Parameters
     ----------
     A : str
         Equipe A.
     B : str
         Equipe B.
     affichage : bool, optional
                 Affiche la probabilité de gagné de l'équipe. 
                 Le défaut est False.
   
     Returns
     -------
     str 
         Retourne l'équipe qui a gagnée.
     """
    d = liste_classement_équipes()
    rating_A = d[A]
    rating_B = d[B]

    coeff = 25
    diff = (rating_B - rating_A) / coeff
    proba_A = (1 - tanh(diff)) / 2
    proba_B = 1 - proba_A
    r = random()

    if r > proba_B:
        if affichage:
            print(f"`{A} à gagné avec un proba de {proba_A} contre {B}")
        return A
    else:
        if affichage:
            print(f"{B} à gagné avec un proba de {proba_B} contre {A}")
        return B
    
    
def match_phase_final_v2(A, B):
    """
    Match en phase finales

    Returns
    -------
    str 
        Retourne une fstring du resultat du match
    """
    équipes_gagnate = match(A, B)
    
    if équipes_gagnate == A:
        return f"{A},gagné,{B},perdu"
    else:
        return f"{A},perdu,{B},gagné"
# ------------------------------------------------------------------------------------------------ #


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
    """
    Lie un fichier csv et retourne une liste des équipes qualifiés 

    Parameters
    ----------
    résultat_csv : str
                   Nom du fichier csv.

    Returns
    -------
    list
        Listes des équipes qualifiés.
    équipes : list
        Liste des lignes du fichier csv.

    """
    with open(résultat_csv, "r", encoding="utf8") as fichier_qualifié:
        équipes = [line.strip().split(",") for line in fichier_qualifié]
    return [équipe_résultat(e, "gagné") for e in équipes], équipes


def phase_finale(phase_précédente, phase_suivante):
    """
    Prend le fichier csv de la phase présédente et créer le fichier csv de la phase suivante
    
    Parameters
    ----------
    phase_précédente : str
                       Nom fichier csv phase précédente.
    phase_suivante : str
                     Nom fichier csv phase précédente.
.

    Returns
    -------
    None.

    """
    équipes = liste_phase_final(phase_précédente)[0]
    taille = len(équipes)

    for i in range(0, taille, 2):
        équipe_1 = équipes[i]
        équipe_2 = équipes[i+1]

        with open(phase_suivante, "a", encoding="utf8") as fichié_phase_final:
            fichié_phase_final.write(
                f"{match_phase_final_v2(équipe_1, équipe_2)}\n")


def huitième():
    """
    Créer le fichier csv des huitièmes de finale

    Returns
    -------
    None.

    """
    équipes = liste_huitième_triée()
    taille = len(équipes)

    for i in range(0, taille, 2):
        équipe_1 = équipes[i]
        équipe_2 = équipes[i+1]

        with open(r"Phase Final\résultats_huitièmes.csv", "a", encoding="utf8") as fichié_huitième:
            fichié_huitième.write(
                f"{match_phase_final_v2(équipe_1, équipe_2)}\n")


def quart():
    """
    Créer le fichier csv des quarts de finale

    Returns
    -------
    None.

    """
    phase_finale(r"Phase Final\résultats_huitièmes.csv",
                 r"Phase Final\résultats_quart.csv")


def demi():
    """
    Créer le fichier csv des demis de finale

    Returns
    -------
    None.

    """
    phase_finale(r"Phase Final\résultats_quart.csv",
                 r"Phase Final\résultats_demi.csv")


def petite_finale():
    """
    Créer le fichier csv de la petite finale

    Returns
    -------
    None.

    """
    with open(r"Phase Final\résultats_demi.csv", "r", encoding="utf8") as fichier_non_qualifié:
        équipes = [line.strip().split(",") for line in fichier_non_qualifié]

    équipe_liste = [équipe_résultat(e, "perdu") for e in équipes]
    taille = len(équipe_liste)

    for i in range(0, taille, 2):
        équipe_1 = équipe_liste[i]
        équipe_2 = équipe_liste[i+1]

        with open(r"Phase Final\résultats_3e_place.csv", "a", encoding="utf8") as fichié_3e:
            fichié_3e.write(
                f"{match_phase_final_v2(équipe_1, équipe_2)}\n")


def finale():
    """
    Créer le fichier csv de la finale

    Returns
    -------
    None.

    """
    phase_finale(r"Phase Final\résultats_demi.csv",
                 r"Phase Final\résultats_finale.csv")
