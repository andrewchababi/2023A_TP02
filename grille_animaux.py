from enum import Enum
import random

from simulation_constants import *
from animal import *


class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2


def creer_case(etat=Contenu.VIDE, animal=None):
    # TODO: Créer et retourner un dictionnaire représentant une case. Utiliser les arguments pour initialiser l'état et l'animal dans la case.
    case = {"etat": etat, "animal": animal}
    return case
    


def creer_grille(nb_lignes, nb_colonnes):
    # TODO: Créer une matrice 2D de cases vides et la retourner sous forme de dictionnaire
    # TODO: Dans le dictionnaire, ajouter des métadonnées décrites dans l'énoncé (nombre de proies, de prédateurs, etc.)
    matrice = [[creer_case() for _ in range(nb_lignes)] for _ in range(nb_colonnes)]  
    nb_proies = 0
    nb_predateurs = 0
    
    grille = {"matrice": matrice,
              "nb_proies": nb_proies,
              "nb_predateurs": nb_predateurs,
              "nb_lignes": nb_lignes,
              "nb_colonnes": nb_colonnes
              }
    return grille

def obtenir_case(grille, ligne, colonne):
    # TODO: 
    case = grille["matrice"][ligne][colonne]
    return case

def obtenir_etat(grille, ligne, colonne):
    etat = grille["matrice"][ligne][colonne]
    return etat["etat"]


def obtenir_animal(grille, ligne, colonne):
    # TODO: Retourner l'animal présent dans la case aux coordonnées données (ligne, col) (Dict)
    animal = grille["matrice"][ligne][colonne]
    return animal["animal"]

def obtenir_population(grille):
    # TODO: Retourner un tuple contenant le nombre actuel de proies et de prédateurs dans la grille (Tuple[Int, Int])
    nomb_proie = 0
    nomb_predateur = 0   
    
    for ligne in grille["matrice"]:
        for case in ligne:
            if case["etat"] == Contenu.PROIE:
                nomb_proie += 1
            elif case["etat"] == Contenu.PREDATEUR:
                nomb_predateur += 1    
    
    return nomb_proie, nomb_predateur           

def obtenir_dimensions(grille):
    # TODO: Retourner un tuple avec le nombre de lignes et de colonnes de la grille (Tuple[Int, Int])
    nomb_ligne = len(grille["matrice"])
    nomb_col = len(grille["matrice"][0]) if nomb_ligne > 0 else 0
    return nomb_ligne, nomb_col



def incrementer_nb_proies(grille):
    # TODO: Augmenter le compteur du nombre de proies dans la grille de 1 (Int)
    grille["nb_proies"] += 1


def decrementer_nb_proies(grille):
    # TODO: Diminuer le compteur du nombre de proies dans la grille de 1 (Int)
    grille["nb_proies"] -= 1 if grille["nb_proies"] > 0 else 0


def incrementer_nb_predateurs(grille):
    # TODO: Augmenter le compteur du nombre de prédateurs dans la grille de 1 (Int)
    grille["nb_predateurs"] += 1 if grille["nb_predateurs"] >= 0 else 0


def decrementer_nb_predateurs(grille):
    # TODO: Diminuer le compteur du nombre de prédateurs dans la grille de 1 (Int)
    grille["nb_predateurs"] -= 1 if grille["nb_predateurs"] > 0 else 0


def check_nb_proies(grille, max_val):
    # TODO: Vérifier si le nombre actuel de proies dans la grille est inférieur à max_val (Booléen)
    return grille["nb_proies"] < max_val


def vider_case(grille, ligne, col):
    # TODO: Écraser la case située à la ligne et la colonne données avec une case vide
    grille["matrice"][ligne][col] = creer_case()


def definir_etat(grille, etat, ligne, col):
    # TODO: Mettre à jour l'état de la case située à la ligne et la colonne données.
    grille["matrice"][ligne][col]["etat"] = etat



def definir_animal(grille, animal, ligne, col):
    # TODO: Placer un animal (sous forme de dictionnaire) sur la case indiquée par les coordonnées (ligne, col).
    grille["matrice"][ligne][col]["animal"] = animal
    
    
def definir_case(grille, case, ligne, col):
    grille["matrice"][ligne][col] = case


def generer_entier(min_val, max_val):
    # TODO: Utiliser une librairie pour générer un nombre entier aléatoire entre min_val et max_val inclus.
    # Le résultat doit être un entier.
    pass


def ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col):
    # TODO: Ajuster la position (ligne, colonne) pour une grille circulaire en utilisant les dimensions de la grille.
    # Indice: Un modulo (%) peut être utile.
    coor_lig = lig % dim_lig
    coor_col = col % dim_col
    return coor_lig, coor_col

def choix_voisin_autour(grille, ligne, col, contenu: Contenu):
    # TODO: Chercher tous les voisins autour de la cellule (ligne, col) qui correspondent au "contenu" donné (Enum).
    # TODO: Renvoyer le nombre total de ces voisins, ainsi que les coordonnées d'un voisin choisi aléatoirement (Tuple).
    #       Si le contenu n'est pas VIDE, le voisin doit être disponible (voir la fonction obtenir_disponibilite).
    # Indice: Utiliser la fonction "ajuster_position_pour_grille_circulaire" pour ajuster les positions des voisins qui sont en dehors de la grille.
    dim_ligne, dim_col = obtenir_dimensions(grille)
    voisins_potentiels =  [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    voisins_valides = []
    
    for d_ligne, d_col in voisins_potentiels:
        adj_ligne, adj_col = ajuster_position_pour_grille_circulaire( ligne + d_ligne, col + d_col ,dim_col, dim_ligne)
        if grille["matrice"][adj_ligne][adj_col]["etat"] == contenu:
            if contenu == Contenu.VIDE:
                voisins_valides.append((adj_ligne,adj_col))
            else:
                animal = obtenir_animal(grille, adj_ligne, adj_col)
                if animal is not None and animal["disponible"]:
                    voisins_valides.append((adj_ligne, adj_col))                
                
    nb_voisins = len(voisins_valides)
    
    voisin_choisi = random.choice(voisins_valides) if nb_voisins > 0 else (None, None)
    
    ligne_choisi , colone_choisi = voisin_choisi
    
    return nb_voisins, ligne_choisi, colone_choisi
    
      



def remplir_grille(grille, pourcentage_proie, pourcentage_predateur):
    # TODO: Obtenir les dimensions de la grille.
    nmb_ligne, nmb_col = obtenir_dimensions(grille)

    # TODO: Calculer le nombre total de cases dans la grille.
    nmb_case_total = nmb_ligne * nmb_col 
    
    # TODO: Calculer le nombre de proies à placer dans la grille.
    nmb_de_proies = int(nmb_case_total*pourcentage_proie)
    
    # TODO: Calculer le nombre de prédateurs à placer dans la grille.
    nmb_de_predateur = int(nmb_case_total*pourcentage_predateur)
    
    # TODO: Générer et mélanger aléatoirement la liste de toutes les positions possibles.
    toutes_positions = [(i, j) for i in range(nmb_ligne) for j in range(nmb_col)]
    random.shuffle(toutes_positions)
    
    # TODO: Placer les proies dans la grille.
    # Utilisez MAX_AGE_PROIE pour générer un âge aléatoire entre 0 et l'âge maximum de la proie.
    # Utilisez NB_JRS_GESTATION_PROIE et NB_JRS_PUBERTE_PROIE pour déterminer la période de gestation si la proie est en âge de procréer.
    for _ in range(nmb_de_proies):
        i, j = toutes_positions.pop()
        age_proie = random.randint(0, MAX_AGE_PROIE)
        est_gestation = age_proie >= NB_JRS_PUBERTE_PROIE # and random.choice([True, False])
        proie = {"age": age_proie, "gestation": est_gestation}
        definir_animal(grille, proie, i, j)
        definir_etat(grille, Contenu.PROIE, i, j)
    
    # TODO: Mettre à jour le compteur du nombre de proies.
    grille["nb_proies"] = nmb_de_proies
    
    # TODO: Placer les prédateurs dans la grille.
    # Utilisez MAX_AGE_PRED pour générer un âge aléatoire entre 0 et l'âge maximum du prédateur.
    # Utilisez NB_JRS_GESTATION_PRED et NB_JRS_PUBERTE_PRED pour déterminer la période de gestation si le prédateur est en âge de procréer.
    # Utilisez AJOUT_ENERGIE pour initialiser la quantité d'énergie du prédateur.
    for _ in range(nmb_de_predateur):
        i, j = toutes_positions.pop()
        age_pred = random.randint(0, MAX_AGE_PRED)
        est_gestation = age_pred >= NB_JRS_PUBERTE_PRED #and random.choice([True, False])
        pred = {"age": age_pred, "gestation": est_gestation, "energie": AJOUT_ENERGIE}
        definir_animal(grille, pred, i, j)
        definir_etat(grille, Contenu.PREDATEUR, i, j)
    
    # TODO: Mettre à jour le compteur du nombre de prédateurs.
    grille["nb_predateurs"] = nmb_de_predateur
    
    