<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Polytechnique_Montr%C3%A9al_logo.jpg" />
</p>

# TP01: Fondamentaux en Python - Données, Variables, Opérateurs et Interactions
- [Directives particulières](#directives)
- [Introduction](#Introduction)
- [Objectifs](#Objectif)
- [Description: La dynamique proie-prédateur](#Description)
- [Déroulement de la simulation](#simulation)
- [Fonctions à implémenter](#Fonctions)
- [Barème](#bareme)
- [Annexe: Guide et normes de codage](#annexe)

:alarm_clock: [Date de remise le dimanche 15 octobre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20231015T235959&p0=165&font=cursive)

## Directives particulières <a name="directives"></a>
* Respecter [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Noms de variables et fonctions adéquats (concis, compréhensibles);  
* Pas de librairies externes autres que celles déjà importées;  

## 1. Introduction <a name="Introduction"></a>
<p align='justify'>L'automate cellulaire, capable de calculabilité universelle malgré sa simplicité, est un concept captivant qui a séduit les scientifiques dans divers domaines allant de la biologie à la physique et à l'informatique. Parmi ces modèles, le "Jeu de la Vie", inventé par John Horton Conway en 1970, est particulièrement intrigant. Ce modèle, bien que simple en apparence, il génère une gamme impressionnante de comportements complexes, allant de formes statiques à des structures oscillantes et même des entités mobiles.</p>

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Gol-gun.gif" alt="Jeu de la Vie" width="500">
</p>
<p align='justify'>Dans cette version adaptée, nous explorerons une dimension supplémentaire de complexité : une dynamique proies-prédateurs. Notre grille de simulation ne se contentera pas d'héberger des cellules "vivantes" ou "mortes", mais aussi des lapins, représentant les proies, et des loups, incarnant les prédateurs. Cette extension ajoute non seulement du réalisme à notre simulation, mais elle nous permet également de comprendre les systèmes dynamiques et les équilibres naturels qui en résultent.</p>

<p align='justify'>Ce laboratoire n'est pas simplement un exercice de programmation : c'est une aventure de découverte. À chaque ligne de code, nous dévoilons un peu plus du mystère des systèmes complexes qui émergent de règles simples. Préparez-vous à plonger dans le monde fascinant des automates cellulaires et des interactions proies-prédateurs, tout en maitrisant les compétences clés en programmation Python.
</p>

## 2. Objectifs: <a name="Objectif"></a>
<p align='justify'> Ce laboratoire vise principalement à:</p>

1.  Maitriser l'utilisation de structures de contrôle 
2.  Maitriser l'utilisation de structures de données complexes en Python, notamment les listes imbriquées et les dictionnaires.
3.  Approfondir la transcription d'algorithmes dans un langage de programmation pour modéliser des phénomènes réels.

## 3. Description: La dynamique proie-prédateur <a name="Description"></a>

<p align='justify'>Bien que le nom "Jeu de la vie" suggère un jeu, il s'agit en réalité d'une simulation. Le socle théorique de notre laboratoire est basé sur le jeu de la vie, un automate cellulaire développé par John H. Conway. Dans cette version enrichie, chaque cellule de notre grille peut accueillir un loup, un lapin ou rester vide. L'état de chaque cellule évolue en fonction de ses voisines, créant une danse dynamique entre les proies et les prédateurs.</p>

Pour ceux désireux d'approfondir leurs connaissances, nous recommandons de consulter la page [Wikipedia du Jeu de la Vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) et [les équations de Lotka-Volterra](https://fr.wikipedia.org/wiki/%C3%89quations_de_Lotka-Volterra) qui offrent un aperçu mathématique de la dynamique proie-prédateur.


## 4. Déroulement de la simulation :<a name="simulation"></a>
<p align='justify'>La première étape dans la réalisation de notre simulation est la configuration initiale de la grille. Vous devrez définir un pourcentage de "remplissage" de la grille avec des loups et des lapins. Par exemple, si 30% de la grille est occupée, parmi ces occupants, 60% pourraient être des lapins et 40% des loups. </p>

<p align='justify'>Ensuite, chaque itération de notre simulation (un tour de boucle) évoluera en examinant l'état de chaque cellule en fonction de ses voisins immédiats. Par exemple, si un loup est adjacent à un lapin, il le consommera et gagnera de l'énergie. En dehors de ces interactions prédateur-proie, la simulation gère d'autres facteurs vitaux tels que le mouvement, la reproduction et la mortalité. Pour visualiser ces interactions, envisagez de consulter des schémas ou des simulations similaires en ligne.</p>

## 5. Fonctions à implémenter <a name="Fonctions"></a>
### 5.1. creer_animal
Cette fonction crée un nouvel animal avec des propriétés spécifiques.
- **Entrée** : 
  - age (int, défaut=0): L'âge de l'animal
  - jrs_gestation (int, défaut=0): Les jours de gestation d'un animal
  - energie (int, défaut=MIN_ENERGIE): L'énergie d'un animal 
  - disponible (bool, défaut=True): Statut de disponibilité d'un animal 
- **Sortie** :
  - un dictionnaire représentant l'animal
- **Exemple** :
  ```python
  creer_animal(5, 3, 20, True)
   ```
  Sortie attendue : 
  ```python
  {"age": 5, "jrs_gestation": 3, "energie": 20, "disponible": True}
  ```

### 5.2. obtenir_age
Cette fonction récupère l'âge d'un animal donné.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - L'âge de l'animal
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_age(animal))
   ```
  Sortie attendue : 
  ```python
  5
  ```


### 5.3. obtenir_jours_gestation
Cette fonction récupère les jours de gestation d'un animal donné.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - Les jours de gestation de l'animal
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_jours_gestation(animal))
   ```
  Sortie attendue : 
  ```python
  3
  ```

### 5.4. obtenir_energie
Cette fonction récupère l'énergie d'un animal donné.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - L'énergie de l'animal
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_energie(animal))
   ```
  Sortie attendue : 
  ```python
  20
  ```

### 5.5. obtenir_disponibilite
Cette fonction récupère le statut de disponibilité  d'un animal donné.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - Le statut de disponibilité  de l'animal
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_disponibilite(animal))
   ```
  Sortie attendue : 
  ```python
  True
  ```

## 6. Barème /20 <a name="bareme"></a>

|**Nom des fonctions**|**Nombre de points attribuer**|
| :- | :- |
|*Exercice 01*|0.5|
|*Exercice 02*|1.0|
|*Exercice 03*|1.5|
|*Exercice 04*|4.0|
|*Exercice 05*|1.5|
|*Exercice 06*|3.0|
|*Exercice 07*|2.5|
|*Exercice 08*|2.0|
|*Exercice 09*|4.0|

## Annexe: Guide et normes de codage <a name="annexe"></a>
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. 
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)

