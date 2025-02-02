from simulation_constants import NB_COLONNE, NB_LIGNE

# Texte
TITRE = "La Forêt de la Vie"

# Polices
CHEMIN_POLICE = "C:\Users\Andrew Chababi\coding shit\First-labs\INF1007\Tp_lab\TP_2\2023A_TP02\assets\Brightly_Crush.ttf"
"./assets/Brightly_Crush.ttf"
TAILLE_POLICE = 34

# Couleurs
COULEUR_PROIE_AVANT_PUBERTE = (131, 252, 50)  # Vert clair
COULEUR_PROIE_APRES_PUBERTE = (115, 214, 49)  # Vert foncé
COULEUR_PRED_AVANT_PUBERTE = (255, 135, 135)  # Rose
COULEUR_PRED_APRES_PUBERTE = (255, 0, 0)  # Rouge
COULEUR_PRED_MANQUE_ENERGIE = (255, 118, 28)  # Orange
COULEUR_CASE = (255, 255, 255)  # Blanc
COULEUR_BORDURE_CASE = (255, 255, 255)  # Blanc
COULEUR_TEXTE = (0, 0, 0)  # Noir

# Images
CHEMIN_IMAGE_FOND = "C:\Users\Andrew Chababi\coding shit\First-labs\INF1007\Tp_lab\TP_2\2023A_TP02\assets\background.jpg"
#"C:\\Users\\Andrew Chababi\\coding shit\\First-labs\\INF1007\\Tp_lab\\TP_2\\2023A_TP02\\assets\\background.jpg"
 #"C:/Users/YourUsername/path_to_script/assets/background.jpg"

# Disposition
DIMENSION_CASE = 20
MARGE_CASE = 2
MARGE_SUPP_LATERALES = 30
MARGE_SUPP_HAUT = 150
MARGE_SUPP_BAS = MARGE_SUPP_LATERALES

LARGEUR_ECRAN = (DIMENSION_CASE + MARGE_CASE) * NB_COLONNE + 2 * MARGE_SUPP_LATERALES

HAUTEUR_ECRAN = (
    (DIMENSION_CASE + MARGE_CASE) * NB_LIGNE
    + MARGE_CASE
    + MARGE_SUPP_HAUT
    + MARGE_SUPP_BAS
)

GRID_Y_INITIAL = (
    HAUTEUR_ECRAN - MARGE_SUPP_BAS - (DIMENSION_CASE + MARGE_CASE) * NB_LIGNE
)
