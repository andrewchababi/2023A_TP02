<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Polytechnique_Montr%C3%A9al_logo.jpg" />
</p>

# TP01: Fondamentaux en Python - Données, Variables, Opérateurs et Interactions
- [Directives particulières](#directives)
- [Introduction](#Introduction)
- [Exercice 01](#Ex01)
- [Exercice 02](#Ex02)
- [Exercice 03](#Ex03)
- [Exercice 04](#Ex04)
- [Exercice 05](#Ex05)
- [Exercice 06](#Ex06)
- [Exercice 07](#Ex07)
- [Exercice 08](#Ex08)
- [Exercice 09](#Ex09)
- [Barème](#bareme)
- [Annexe: Guide et normes de codage](#annexe)

:alarm_clock: [Date de remise le dimanche 24 septembre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20230924T235959&p0=165&font=cursive)

## Directives particulières <a name="directives"></a>
* Respecter [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Noms de variables et fonctions adéquats (concis, compréhensibles);  
* Pas de librairies externes autres que celles déjà importées;  

## 1. Introduction <a name="Introduction"></a>
<p align='justify'> À l'issue de ce laboratoire, les participants seront familiarisés avec les structures de base en Python : types de données, utilisation des variables, opérateurs arithmétiques et logiques, ainsi que l'interaction avec l'utilisateur via les fonctions `input` et `print`. </p>

## 2. Exercice 01: Interaction avec l'utilisateur <a name="Ex01"></a>
<p align='justify'> Créez un programme qui demande le prénom et le nom de l'utilisateur et renvoie un message personnalisé.</p>

**Consignes**: 
1.  Sollicitez le prénom de l'utilisateur.
2.  Faites de même pour le nom.
3.  Formatez et affichez un message d'accueil tel que: "Bonjour \[prénom\] \[nom\]!".

**Conseil**: Veillez à bien gérer les espaces dans le message.

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|Saad | Entrez votre prenom: Saad|
|Belgana | Entrez votre nom: Belgana|
|        | Bonjour Saad Belagana! |

## 3. Exercice 02: Calculs géométriques pour un rectangle<a name="Ex02"></a>
<p align='justify'> Créez un programme qui calcule le périmètre et l'aire d'un rectangle selon les dimensions fournies par l'utilisateur.

1.  Demandez la longueur du rectangle.
2.  Demandez ensuite sa largeur.
3.  Calculez et affichez le périmètre et l'aire.</p>

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|12.5 | Entrez la longueur du rectangle: 12.5|
|30.5 | Entrez la largeur du rectangle: 30.5|
|        | Le perimetre du rectangle est: 86.0|
|        | L'aire du rectangle est: 381.25|

## 4. Exercice 03: Travail avec des chaînes de caractères<a name="Ex03"></a>
<p align='justify'> Le traitement des chaînes de caractères est un aspect fondamental de la programmation. Dans cet exercice, vous vous familiariserez avec certaines opérations basiques liées aux chaînes en Python.

  

1.  Demandez une phrase à l'utilisateur.
2.  Comptez et affichez le nombre de mots dans cette phrase.
3.  Convertissez et affichez la phrase en majuscules.</p>

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|Bonjour INF1007! Bienvenue dans ce premier laboratoire. | Entrez une phrase: Bonjour INF1007! Bienvenue dans ce premier laboratoire.|
|        | La phrase contient 7 mots.|
|        | Phrase en majuscules: BONJOUR INF1007! BIENVENUE DANS CE PREMIER LABORATOIRE.|

## 5. Exercice 04: Conception d'une Mini-Calculatrice<a name="Ex04"></a>
Dans cet exercice, votre mission est de concevoir une calculatrice simple mais efficace. 

Voici comment vous allez procéder: 

**Sélection de l'opération:**    

Au démarrage, votre calculatrice devra présenter à l'utilisateur les opérations disponibles. Les opérations proposées sont :             

*   Addition             
*   Soustraction             
*   Multiplication             
*   Division      

L'utilisateur choisira l'opération qu'il souhaite effectuer en la sélectionnant parmi les options présentées.            

**Saisie des nombres:**   

Après avoir choisi l'opération, invitez l'utilisateur à saisir deux nombres sur lesquels l'opération sera effectuée. Assurez-vous que l'entrée est valide et qu'elle correspond à un nombre réel.            

**Calcul et Affichage:**   

Une fois les nombres saisis, votre programme effectuera l'opération choisie et affichera le résultat à l'utilisateur.   

  

**Gestion des erreurs:**            

Division par zéro: Votre calculatrice doit être à l'épreuve des erreurs. Si l'utilisateur tente une division par zéro, plutôt que de permettre au programme de s'arrêter ou de crasher, vous devriez afficher un message d'erreur indiquant : "Erreur : Division par zero" 

**Exemples**

| Entrée |  Résultat  |
|:-----|:--------|
|1| Choisissez une operation:|
|2| &emsp; 1. Addition|
|3| &emsp; 2. Soustraction|
|| &emsp; 3. Multiplication|
|| &emsp; 4. Division|
||1|
||Entrez le premier nombre: 2|
||Entrez le second nombre: 3|
||Resultat: 5.0|

| Entrée |  Résultat  |
|:-----|:--------|
|4| Choisissez une operation:|
|0| &emsp; 1. Addition|
|0| &emsp; 2. Soustraction|
|| &emsp; 3. Multiplication|
|| &emsp; 4. Division|
||0|
||Entrez le premier nombre: 0|
||Entrez le second nombre: 0|
||Erreur: Division par zero.|

## 6. Exercice 05: Calcul d'intérêt composé<a name="Ex05"></a>
<p align='justify'> Créez un programme qui aide les utilisateurs à prévoir la croissance de leur investissement basée sur un taux d'intérêt fixe.

**Instructions:** 
1.  Votre programme commencera par solliciter l'utilisateur pour qu'il fournisse trois informations essentielles:    
    *   La somme d'argent initialement déposée (P).             
    *   Le taux d'intérêt annuel offert par l'institution financière (en pourcentage).             
    *   Le nombre d'années (t) pendant lesquelles l'investissement sera maintenu.            
2.  Une fois ces données recueillies, convertissez le taux d'intérêt de pourcentage en décimal (r = taux d'intérêt / 100).   
3.  Utilisez la formule d'intérêt composé pour calculer la somme totale (A) à la fin de la période d'investissement: A = P(1 + r)**t 
    * P est la somme initiale.             
    * r est le taux d'intérêt annuel (en décimal).             
    * t est le nombre d'années.             
4.  Puisque l'intérêt est composé annuellement pour cet exercice, n (le nombre de fois que l'intérêt est composé par année) sera égal à 1.   
5.  En conclusion, le programme devra afficher à l'utilisateur la somme totale qu'il aurait à la fin de la période d'investissement. Cette présentation fournira une estimation précieuse de l'évolution potentielle de son investissement initial.            

**Remarque:** 
Il est crucial de toujours se rappeler que les rendements passés ne garantissent pas les performances futures en matière d'investissement. Cet outil est fourni à des fins éducatives et doit être utilisé comme un guide pour comprendre l'impact potentiel des intérêts composés.</p>

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|380000| Entrez le montant initial: 380000|
| 4.2       | Entrez le taux d'interet annuel (en %): 4.2|
|  25      | Entrez le nombre d'annees de l'investissement: 25|
| | Montant final apres 25 ans: 1062861.24|

## 7. Exercice 06: Calculateur d'IMC<a name="Ex06"></a>
<p align='justify'> </p>

L'Indice de Masse Corporelle, couramment désigné par son acronyme IMC, est une formule standardisée utilisée pour déterminer la corpulence d'une personne en fonction de sa taille et de son poids. Il permet de catégoriser le poids d'une personne dans l'un des groupes définis, allant de l'insuffisance pondérale à l'obésité. La formule pour calculer l'IMC est la suivante:

&emsp; $IMC = \frac{poids(en kg)}{taille(en m)^2}$

Vous êtes chargé de concevoir un programme interactif qui guide l'utilisateur à travers le processus de calcul de son IMC. Voici les étapes à suivre:

1. Le programme devrait initialement solliciter l'utilisateur pour entrer son poids (en kilogrammes) et sa taille (en mètres).
2. Avec ces données en main, le programme doit ensuite calculer l'IMC en utilisant la formule mentionnée ci-dessus.
3. Une fois le calcul effectué, l'IMC doit être présenté à l'utilisateur, de préférence avec une précision de deux décimales pour assurer la clarté.
4. Outre la valeur numérique, le programme doit également fournir une évaluation qualitative de l'IMC calculé. Voici les catégories à prendre en compte :
   * Insuffisance pondérale: IMC inférieur à 18.5.
   * Poids normal: IMC entre 18.5 et 24.9.
   * Surpoids: IMC entre 25 et 29.9.
   * Obésité: IMC de 30 ou plus.
5. Enfin, assurez-vous que votre programme se termine par un message positif ou des recommandations pour encourager l'utilisateur à adopter un mode de vie sain.

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|70| Entrez votre poids en kg: 70|
|1.78| Entrez votre taille en m: 1.78|
| | Votre IMC est: 22.09|
| | Votre poids est normal.|

## 8. Exercice 07: Décomposition de secondes<a name="Ex07"></a>
<p align='justify'> </p>

Lorsqu'on mesure une durée en secondes, il est courant de chercher à connaître la répartition de cette durée en termes d'années, jours, heures, minutes et secondes. Cela peut être utile pour avoir une meilleure compréhension du temps écoulé ou simplement pour satisfaire une curiosité mathématique. 

Vous êtes chargé de concevoir un programme qui détermine la répartition d'une certaine durée en secondes en années, jours, heures, minutes et secondes. 

Le programme devrait initialement solliciter l'utilisateur pour entrer la durée en secondes. Par exemple, s'il entre "31556952", cela signifie 31556952 secondes. Le programme devrait ensuite déterminer le nombre d'années, de jours, d'heures, de minutes et de secondes qui composent cette durée. Finalement, vous devez afficher la répartition en années, jours, heures, minutes et secondes pour la durée souhaitée.

Note importante: Dans votre programme, si une unité de temps (années, jours, heures, ou minutes) a une valeur de 0, elle ne devrait pas être affichée dans le résultat final. Cependant, les secondes restantes devront toujours être affichées, peu importe leur valeur.

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|31556952| En 31556952 secondes, on a: 1 annees, 5 heures, 49 minutes et 12 secondes.|

## 9. Exercice 08: Convertisseur Kilomètres-Miles<a name="Ex08"></a>
<p align='justify'> </p>

Avec la globalisation, il est de plus en plus courant d'interagir avec des systèmes de mesures variés. En particulier, le kilomètre, utilisé dans la majorité des pays comme le Canada, et le mile, principalement utilisé aux États-Unis, sont deux unités de distance couramment rencontrées. Avoir un convertisseur pratique peut s'avérer utile dans de nombreuses situations, que ce soit pour le voyage, la course à pied ou la planification d'itinéraires.   

Dans cet exercice, vous allez développer un convertisseur de distance fiable et convivial qui peut traduire des kilomètres en miles, et vice-versa. 

Au démarrage, interrogez l'utilisateur sur le type de conversion qu'il souhaite effectuer en entrant "1" pour une conversion de kilomètres vers miles (K vers M) et "2" pour une conversion de miles vers kilomètres (M vers K).

Après avoir choisi le type de conversion, demandez à l'utilisateur d'entrer la distance qu'il souhaite convertir.  

Selon le choix de l'utilisateur: 

1. Si la conversion est de kilomètres en miles, utilisez la formule :

   $miles=kilomètres\times0.621371$

 
2. Si la conversion est de miles en kilomètres, utilisez la formule : 

   $kilomètres=miles÷0.621371$

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|1|Type de conversion :|
|16|1: Kilometres vers Miles (K vers M)|
||2: Miles vers Kilometres (M vers K)|
||Entrez votre choix (1 ou 2): |
||1|
||Entrez la distance a convertir: |
||16|
||16 kilometres equivalent a 9.941936 miles.|

## 9. Exercice 09: Trajectoire quadratique d'un projectile<a name="Ex09"></a>

Imaginez que vous êtes un ingénieur en aéronautique et que vous travaillez sur la trajectoire d'un projectile. L'équation de la trajectoire dans un plan est modélisée par une équation quadratique de la forme $ax2+bx+c=0$, où a, b, et c sont des constantes spécifiques au projectile et à son environnement. 

Le but est de déterminer les moments exacts où le projectile atteint une altitude définie. 

Commencez par définir et calculer le discriminant de l'équation. Stockez le résultat dans une variable appelée "delta". En vous basant sur la valeur de "delta", déterminez si le projectile n'atteint jamais l'altitude spécifiée. 

  1. Si c'est le cas, affichez "Le projectile n'atteint jamais l'altitude désirée." 
  2. Si le discriminant indique qu'il existe un seul moment où le projectile atteint cette altitude, calculez-le. Si cet instant est positif, affichez "Le projectile atteint l'altitude à un seul moment précis." et affichez le. Sinon, affichez "Le projectile n'atteint jamais l'altitude désirée.".
  3. Si le discriminant indique que le projectile atteindrait cette altitude à deux moments distincts, calculez-les. Affichez "Le projectile atteint l'altitude a un seul moment précis." ainsi que l'instant en question, si un seul des instants est positif. Affichez "Le projectile atteint l'altitude à deux moments distincts." et la valeur des deux instants si les deux instants sont positifs. Sinon, affichez "Le projectile n'atteint jamais l'altitude désirée.".

**Exemple**

| Entrée |  Résultat  |
|:-----|:--------|
|1|Veuillez entrer la valeur de a (coefficient de x^2): |
|-2|1|
|1|Veuillez entrer la valeur de b (coefficient de x): |
||-2|
||Veuillez entrer la valeur de c (terme constant): |
||1|
||Le projectile atteint l'altitude a un seul moment précis.|
||Instant de l'impact: 1.0|

## 10. Barème /20 <a name="bareme"></a>

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

