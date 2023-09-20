from enum import Enum
import random

from simulation_constants import *


class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2


def creer_animal(age=0, jrs_gestation=0, energie=0, disponible=True):
    # TODO: Créer et retourner un dictionnaire représentant un animal. Utiliser les arguments de la fonction pour initialiser les valeurs.
    pass


def obtenir_age(animal):
    # TODO: Retourner la valeur de l'âge de l'animal donné (Int)
    pass


def obtenir_jours_gestation(animal):
    # TODO: Retourner le nombre de jours de gestation de l'animal donné (Int)
    pass


def obtenir_energie(animal):
    # TODO: Retourner la quantité d'énergie de l'animal donné (Int)
    pass


def obtenir_disponibilite(animal):
    # TODO: Retourner l'état de disponibilité de l'animal (Booléen)
    pass


def incrementer_age(animal, puberte):
    # TODO: Incrémenter l'âge de l'animal de 1
    # TODO: Si l'animal est plus âgé que l'âge de la puberté, incrémenter son nombre de jours de gestation de 1
    pass


def definir_jours_gestation(animal, jrs_gest):
    # TODO: Mettre à jour le nombre de jours de gestation de l'animal avec la valeur jrs_gest donnée (Int)
    pass


def ajouter_energie(animal, valeur):
    # TODO: Ajouter la quantité d'énergie donnée (valeur) à l'énergie actuelle de l'animal (Int)
    pass


def definir_disponibilite(animal, permis):
    # TODO: Mettre à jour l'état de disponibilité de l'animal en utilisant le paramètre permis (Booléen)
    pass


def creer_case(etat=Contenu.VIDE, animal=None):
    # TODO: Créer et retourner un dictionnaire représentant une case. Utiliser les arguments pour initialiser l'état et l'animal dans la case.
    pass


def creer_grille(nb_lignes, nb_colonnes):
    # TODO: Créer une matrice 2D de cases vides et la retourner sous forme de dictionnaire
    # TODO: Dans le dictionnaire, ajouter des métadonnées décrites dans l'énoncé (nombre de proies, de prédateurs, etc.)
    pass


def obtenir_population(grille):
    # TODO: Retourner un tuple contenant le nombre actuel de proies et de prédateurs dans la grille (Tuple[Int, Int])
    pass


def obtenir_dimensions(grille):
    # TODO: Retourner un tuple avec le nombre de lignes et de colonnes de la grille (Tuple[Int, Int])
    pass


def obtenir_animal(grille, ligne, col):
    # TODO: Retourner l'animal présent dans la case aux coordonnées données (ligne, col) (Dict)
    pass


def incrementer_nb_proies(grille):
    # TODO: Augmenter le compteur du nombre de proies dans la grille de 1 (Int)
    pass


def decrementer_nb_proies(grille):
    # TODO: Diminuer le compteur du nombre de proies dans la grille de 1 (Int)
    pass


def incrementer_nb_predateurs(grille):
    # TODO: Augmenter le compteur du nombre de prédateurs dans la grille de 1 (Int)
    pass


def decrementer_nb_predateurs(grille):
    # TODO: Diminuer le compteur du nombre de prédateurs dans la grille de 1 (Int)
    pass


def check_nb_proies(grille, max_val):
    # TODO: Vérifier si le nombre actuel de proies dans la grille est inférieur à max_val (Booléen)
    pass


def vider_case(grille, ligne, col):
    # TODO: Écraser la case située à la ligne et la colonne données avec une case vide
    pass


def definit_etat(grille, etat, ligne, col):
    # TODO: Mettre à jour l'état de la case située à la ligne et la colonne données.
    # Utiliser le paramètre 'etat', qui est une valeur de l'Enum Contenu (VIDE, PROIE, PREDATEUR).
    pass


def definir_animal(grille, animal, ligne, col):
    # TODO: Placer un animal (sous forme de dictionnaire) sur la case indiquée par les coordonnées (ligne, col).
    pass


def obtenir_etat(grille, ligne, col):
    # TODO: Obtenir et retourner l'état actuel de la case à la position (ligne, col).
    # Le type de retour est une valeur de l'Enum Contenu (VIDE, PROIE, PREDATEUR).
    pass


def generer_entier(min_val, max_val):
    # TODO: Utiliser une librairie pour générer un nombre entier aléatoire entre min_val et max_val inclus.
    # Le résultat doit être un entier.
    pass


def ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col):
    # TODO: Ajuster la position (ligne, colonne) pour une grille circulaire en utilisant les dimensions de la grille.
    # Indice: Un modulo (%) peut être utile.
    pass


def choix_voisin_autour(grille, ligne, col, contenu: Contenu):
    # TODO: Chercher tous les voisins autour de la cellule (ligne, col) qui correspondent au "contenu" donné (Enum).
    # TODO: Renvoyer le nombre total de ces voisins, ainsi que les coordonnées d'un voisin choisi aléatoirement (Tuple).
    #       Si le contenu n'est pas VIDE, le voisin doit être disponible (voir la fonction obtenir_disponibilite).
    # Indice: Utiliser la fonction "ajuster_position_pour_grille_circulaire" pour ajuster les positions des voisins qui sont en dehors de la grille.
    pass


def remplir_grille(grille, pourcentage_remplissage_total):
    # TODO: Obtenir les dimensions de la grille et calculer le nombre total de cases (nb_cases).
    # Utiliser la fonction "obtenir_dimensions" pour obtenir nb_lig et nb_col.

    # TODO: Calculer le nombre de proies et de prédateurs à placer dans la grille.
    # Utiliser les constantes POURCENTAGE_PROIES, MAX_AGE_PROIE, NB_JRS_GESTATION_PROIE et NB_JRS_PUBERTE_PROIE
    # pour les proies, et les équivalents pour les prédateurs.

    # TODO: Remplir la grille avec le nombre calculé de proies.
    # Utiliser les fonctions "creer_animal", "definit_etat", "definir_animal", et "incrementer_nb_proies".

    # TODO: Remplir la grille avec le nombre calculé de prédateurs.
    # Utiliser les fonctions "creer_animal", "definit_etat", "definir_animal", et "incrementer_nb_predateurs".
    pass


def simulation_est_terminee(grille):
    # TODO: Vérifier si la simulation est terminée.
    # Elle se termine lorsque le nombre de proies ou le nombre de prédateurs est égal à zéro.
    # Renvoyer un booléen indiquant l'état de la simulation.
    pass


def rendre_animaux_disponibles(grille):
    # TODO: Parcourir chaque case de la grille et rendre tous les animaux disponibles (Booléen à True) pour la prochaine itération.
    pass


def deplacer_animal(grille, ligne, col, animal):
    # TODO: Trouver un voisin vide où déplacer l'animal, effectuer le déplacement et mettre à jour l'état
    # et la disponibilité de l'animal. Utiliser "choix_voisin_autour", "definit_etat", "definir_animal",
    # "definir_disponibilite" et "vider_case" pour réaliser ces étapes.
    pass


def executer_cycle_proie(grille, ligne, col, animal):
    # TODO: Gérer le cycle de vie d'une proie à une position donnée sur la grille.
    # 1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PROIE, le retirer de la grille et décrémenter le compteur de proies.
    # 2. Si l'animal est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PROIE), tenter de générer un nouveau bébé proie.
    #    Pour ce faire, chercher un voisin vide autour de la proie. Si un voisin est trouvé, créer un bébé proie et le placer dans la grille.
    # 3. Sinon, déplacer l'animal vers une case vide à proximité.
    pass


def executer_cycle_predateur(grille, ligne, col, animal):
    # TODO: Gérer le cycle de vie d'un prédateur à une position donnée sur la grille.
    # 1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PRED ou si le prédateur manque d'énergie (énergie < MIN_ENERGIE), le retirer
    #    de la grille et décrémenter le compteur de prédateurs.
    # 2. Si le prédateur peut manger une proie dans une case voisine, le faire en le déplaçant dans la case de la proie et en
    #    incrémentant son énergie de AJOUT_ENERGIE (n'oubliez pas de décrémenter le compteur de proies). Après avoir mangé, si le
    #    prédateur est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PRED), tenter de générer un nouveau bébé
    #    prédateur. Pour ce faire, chercher un voisin vide autour du prédateur. Si un voisin est trouvé, créer un bébé prédateur et
    #    le placer dans la grille.
    # 3. Sinon, déplacer l'animal vers une case vide à proximité et décrémenter son énergie de 1.
    pass


def executer_cycle(grille):
    # TODO: Marquer tous les animaux comme disponibles pour ce cycle, puis parcourir la grille pour exécuter la bonne procédure
    # du cycle de vie pour chaque animal. Il est nécessaires d'utiliser au minimum les fonctions "rendre_animaux_disponibles",
    # "executer_cycle_proie" et "executer_cycle_predateur".
    pass
