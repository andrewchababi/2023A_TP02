from enum import Enum
import random

from simulation_constants import *
from animal import *
from grille_animaux import *

def simulation_est_terminee(grille):
    # TODO: Vérifier si la simulation est terminée.
    # Elle se termine lorsque le nombre de proies ou le nombre de prédateurs est égal à zéro.
    # Renvoyer un booléen indiquant l'état de la simulation.
    terminee = grille["nb_proies"] == 0 or grille["nb_predateurs"] == 0
    return terminee


def rendre_animaux_disponibles(grille):
    # TODO: Parcourir chaque case de la grille et rendre tous les animaux disponibles (Booléen à True) pour la prochaine itération.
    for ligne in grille["matrice"]:
        for case in ligne:
            if case["animal"] != None:
                case["animal"]["disponible"] = True


def deplacer_animal(grille, ligne, col, animal):
    # TODO: Trouver un voisin vide où déplacer l'animal, effectuer le déplacement et mettre à jour l'état
    # et la disponibilité de l'animal. Utiliser "choix_voisin_autour", "definit_etat", "definir_animal",
    # "definir_disponibilite" et "vider_case" pour réaliser ces étapes.
    nb_voisin, nouv_lign, nouv_col = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
    
    definir_etat(grille, Contenu.VIDE, nouv_lign, nouv_col )
    
    definir_animal(grille, animal, nouv_lign, nouv_col)
    
    definir_disponibilite(animal, False)
        
    vider_case(grille, ligne, col)
    
    

        

def executer_cycle_proie(grille, ligne, col, animal):
    # TODO: Gérer le cycle de vie d'une proie à une position donnée sur la grille.
    # 1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PROIE, le retirer de la grille et décrémenter le compteur de proies.
    # 2. Si l'animal est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PROIE), tenter de générer un nouveau bébé proie.
    #    Pour ce faire, chercher un voisin vide autour de la proie. Si un voisin est trouvé, créer un bébé proie et le placer dans la grille.
    # 3. Sinon, déplacer l'animal vers une case vide à proximité.
    
    #increases age of the prey
    incrementer_age(animal, NB_JRS_PUBERTE_PROIE)
    age_animal = obtenir_age(animal)
    
    jours_gestation = obtenir_jours_gestation(animal)
    
    #if prey dies it reduces the counter by 1
    if age_animal> MAX_AGE_PROIE:
        vider_case(grille, ligne, col)
        decrementer_nb_proies(grille)
    #if the age is larger than puberty and gestation days are more than required we attempt to creat a new animal  
    else:
        if age_animal >= NB_JRS_PUBERTE_PROIE and jours_gestation >= NB_JRS_GESTATION_PROIE:
            #Finds an empty cell
            nb_voisins, ligne_choisi, colone_choisi = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
            if nb_voisins and check_nb_proies(grille, NB_MAX_PROIES):
                nouvau_animal = creer_case(etat=Contenu.PROIE, animal=creer_animal())
                definir_animal(grille, nouvau_animal,ligne_choisi, colone_choisi)
                incrementer_nb_proies(grille)
                grille["matrice"][ligne][col]["jrs_gestation"] = 0
        else:
            deplacer_animal(grille, ligne, col, animal)
                    
    return grille







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
    incrementer_age(animal, NB_JRS_PUBERTE_PROIE)
    age_predateur = obtenir_age(animal)
    age_predateur += NB_JRS_PUBERTE_PRED  #ask maaroff about this
    
    jour_gestion_pred = obtenir_jours_gestation(animal)
    
    
    if age_predateur <= MAX_AGE_PRED and age_predateur >= NB_JRS_PUBERTE_PRED and obtenir_energie(animal) >= MIN_SANTE_PRED:
        prey_trouve , prey_ligne_choisi, prey_col_choisi = choix_voisin_autour(grille, ligne, col, Contenu.PROIE)
        
        if prey_trouve:
            definir_disponibilite(animal, False)
            ajouter_energie(animal, 1)
            vider_case(grille, ligne, col)
            decrementer_nb_proies(grille)
            
            if jour_gestion_pred > NB_JRS_GESTATION_PRED:
                #part that creates baby pred
                jour_gestion_pred = 0
                nouvau_pred = creer_case(etat=Contenu.PREDATEUR, animal=creer_animal())
                definir_animal(grille, nouvau_pred ,prey_ligne_choisi, prey_col_choisi)
                incrementer_nb_predateurs(grille)
                #part that locates it
                baby_creer, ligne_babe_creer, col_babe_creer = choix_voisin_autour(grille, ligne, col, Contenu.PREDATEUR)
                
                if baby_creer:
                    grille["matrice"][ligne_babe_creer][col_babe_creer] = creer_case(etat=Contenu.PREDATEUR, animal=creer_animal())
        else:
            move_found, move_line, move_col = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
            if move_found:
                deplacer_animal(grille, move_line, move_col, animal)
            else:
                ajouter_energie(animal, -1)
                
    else:
        vider_case(grille, ligne, col)
        decrementer_nb_predateurs(grille)
        
    return grille
        
        



def executer_cycle(grille):
    # TODO: Marquer tous les animaux comme disponibles pour ce cycle, puis parcourir la grille pour exécuter la bonne procédure
    # du cycle de vie pour chaque animal. Il est nécessaires d'utiliser au minimum les fonctions "rendre_animaux_disponibles",
    # "executer_cycle_proie" et "executer_cycle_predateur".
    rendre_animaux_disponibles(grille)
    nb_lig,nb_col=obtenir_dimensions(grille)
    for ligne in range(nb_lig):
        for col in range(nb_col):
            if obtenir_case(grille, ligne, col) != creer_case(etat= Contenu.VIDE, animal= None):
                animal = obtenir_animal(grille, ligne, col)
                if obtenir_disponibilite(animal):
                    if  obtenir_etat(grille, ligne, col) == Contenu.PROIE:
                        executer_cycle_proie(grille, ligne, col, animal)
                    else:
                        executer_cycle_predateur(grille, ligne, col, animal)
                        
    return grille
            


