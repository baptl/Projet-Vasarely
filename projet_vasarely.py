"""
Projet Vasarely (version 2)
Auteur : baptl
Date : 31/03/2019
Programme permettant de dessiner un canevas de pavés hexagonaux déformés dans le style "op art" de Vasarely.
Entrées : paramètres saisis par l'utilisateur (voir listes d'arguments des fonctions ci-dessous).
Sorties : dessin d'un canevas de pavés hexagonaux déformés (à l'écran, fenêtre "turtle").

"""


import turtle
# importe le module "turtle" utilisé pour le dessin = en fonction des paramètres saisis


import math
# importe le module "math" permettant de calculer les coordonnées des points de passage


from deformation import deformation
# importe la fonction "deformation" depuis le module du même nom (voir documentation *)


def hexagone(t, c, longueur, col1, col2, col3, deformation, centre, rayon) :

    """
    Fonction permettant de tracer 1 pavé hexagonal (à l'aide du module "turtle").
    Entrées : paramètres saisis par l'utilisateur, transmis par la fonction "pavage".
    Sorties : tracé d'1 pavé hexagonal (à l'écran, fenêtre "turtle").
    Arguments :
    t = tortue (remplace l'objet "Turtle" dans les fonctions liées au module "turtle") ;
    c = liste contenant les coordonnées (x, y) du centre du pavé hexagonal (transmises par la fonction "pavage") ;
    longueur = distance entre le centre "c" et n'importe quel coin de son périmètre extérieur ;
    col1, col2, col3 = couleurs de remplissage ;
    deformation = fonction appelée par "hexagone", ayant pour effet de déformer les pavés hexagonaux ;
    centre = liste contenant les coordonnées (c_x, c_y, c_z) du centre de la sphère de déformation ;
    rayon = rayon de la sphère de déformation.

    """

    t.up()
    # désactivation du "pinceau"

    t.goto((deformation((c[0], c[1], 0), centre, rayon)[0], deformation((c[0], c[1], 0), centre, rayon)[1]))
    # déplacement vers le centre "c" (déformé le cas échéant)

    t.down()
    # ré-activation du "pinceau"

    palette_couleurs = [col1, col2, col3]
    # création d'une liste où sont indexées pour référence les couleurs choisies par l'utilisateur (input)

    los1pos1 = [(c[0] + longueur), c[1]]
    los1pos2 = [(c[0] + (longueur * math.cos(math.pi/3))), (c[1] + (longueur * math.sin(math.pi/3)))]
    los1pos3 = [(c[0] - (longueur * math.cos(math.pi/3))), (c[1] + (longueur * math.sin(math.pi/3)))]
    # positions successives des points du losange 1 (hors retour à "c")

    los2pos1 = [(c[0] - (longueur * math.cos(math.pi/3))), (c[1] + (longueur * math.sin(math.pi/3)))]
    los2pos2 = [(c[0] - longueur), c[1]]
    los2pos3 = [(c[0] - (longueur * math.cos(math.pi/3))), (c[1] - (longueur * math.sin(math.pi/3)))]
    # positions successives des points du losange 2 (hors retour à "c")

    los3pos1 = [(c[0] - (longueur * math.cos(math.pi/3))), (c[1] - (longueur * math.sin(math.pi/3)))]
    los3pos2 = [(c[0] + (longueur * math.cos(math.pi/3))), (c[1] - (longueur * math.sin(math.pi/3)))]
    los3pos3 = [(c[0] + longueur), c[1]]
    # positions successives des points du losange 3 (hors retour à "c")

    map_los1 = [los1pos1, los1pos2, los1pos3, c] # carte du losange 1 (incluant le retour à "c")
    map_los2 = [los2pos1, los2pos2, los2pos3, c] # carte du losange 2 (incluant le retour à "c")
    map_los3 = [los3pos1, los3pos2, los3pos3, c] # carte du losange 3 (incluant le retour à "c")

    map_glob = [map_los1, map_los2, map_los3] # carte globale de l'hexagone, où chaque losange = une étape
    # création d'une liste où sont indexées pour référence les positions des différents points à parcourir

    for i in range (3) : # pour chacun des 3 losanges composant 1 hexagone
        map = map_glob[i] # choix de la carte du losange
        t.color(palette_couleurs[i]) # choix de la couleur à appliquer
        t.begin_fill() # début du remplissage
        for i in range (4) : # pour chacun des 4 segments composant 1 losange
            p = map[i] # identification du point suivant à atteindre, déplacement vers celui-ci (déformé le cas échéant)
            t.goto((deformation((p[0], p[1], 0), centre, rayon)[0], deformation((p[0], p[1], 0), centre, rayon)[1]))
        t.end_fill() # fin du remplissage


def pavage(t, inf_gauche, sup_droit, longueur, col1, col2, col3, deformation, centre, rayon) :

    """
    Fonction permettant de dessiner un canevas de pavés hexagonaux
    (à l'aide du module "turtle" et de la fonction "hexagone").
    Entrées : paramètres saisis par l'utilisateur.
    Sorties : dessin d'un canevas de pavés hexagonaux (à l'écran, fenêtre "turtle").
    Arguments :
    t = tortue (remplace l'objet "Turtle" dans les fonctions liées au module "turtle") ;
    inf_gauche, sup_droit = dimensions de la page (= coordonnées des angles inférieur gauche et supérieur droit)
    longueur = longueur d'un segment de pavé (transmise à "hexagone") ;
    col1, col2, col3 = couleurs de remplissage ;
    deformation = fonction appelée par "hexagone", ayant pour effet de déformer les pavés hexagonaux ;
    centre = liste contenant les coordonnées (c_x, c_y, c_z) du centre de la sphère de déformation ;
    rayon = rayon de la sphère de déformation.

    """

    t.title("Projet Vasarely")
    # donne le titre de la fenêtre = titre de l'œuvre
    t.setup((sup_droit - inf_gauche), (sup_droit - inf_gauche))
    # règle ses dimensions = sup_droit - inf_gauche en largeur et en hauteur (position de la tortue centrée par défaut)
    c = [inf_gauche, inf_gauche]
    # positionne la tortue dans l'angle inférieur gauche qui servira de point de départ initial
    t.speed("fastest")
    # fait chauffer son moteur..., règle vitesse de la tortue :)
    t.hideturtle()
    # optionnel : masque la tortue
    num_ligne = 1
    # initialise le compteur de lignes en partant de 1
    while c[1] <= sup_droit :
        # boucle principale renouvelée jusqu'à ce que le point "c" atteigne la hauteur max (= bord haut)
        while c[0] <= sup_droit :
            # boucle secondaire renouvelée jusqu'à ce que le point "c" atteigne la largeur max (= bord droit)
            hexagone(t, c, longueur, col1, col2, col3, deformation, centre, rayon)
            # réalisation d'1 pavé hexagonal en faisant appel à la fonction "hexagone"
            c[0] = c[0] + longueur * 3
            # décalage du centre "c" de trois longueurs vers la droite pour réalisation du pavé suivant
        num_ligne = num_ligne + 1
        # incrémentation du compteur >> numéro de ligne suivante
        c[1] = c[1] + longueur * math.cos(30 * math.pi / 180)
        # décalage vers ligne suivante
        if num_ligne % 2 == 0 :
            # si c'est une ligne paire
            c[0] = inf_gauche + 1.5 * longueur
            # repositionnement du centre "c" contre le bord gauche décalé d'une longueur et demie vers la droite
        else :
            # dans le cas contraire
            c[0] = inf_gauche
            # repositionnement du centre "c" contre le bord gauche
    t.done()
    # une fois le dessin terminé : attente clic utilisateur pour effacer l'écran


"""
Ci-dessous le code principal avec message d'accueil, enregistrement des paramètres utilisateur,
et initialisation de la fonction "pavage".

"""


t = turtle # création de l'objet "Turtle"
print()
print("Bonjour et bienvenue dans ce programme de création d'œuvres d'art optique à la manière de Vasarely.")
print()
print("Pour commencer, veuillez saisir les dimensions de votre toile :")
print()
inf_gauche = int(input("Position de l'angle inférieur gauche = "))
sup_droit = int(input("Position de l'angle supérieur droit = "))
longueur = int(input("Longueur des côtés des pavés = "))
col1 = str(input("Couleur 1 = "))
col2 = str(input("Couleur 2 = "))
col3 = str(input("Couleur 3 = "))
centre = input("Coordonnées du centre de la sphère = ")
centre = centre.split() # séparation des trois valeurs (c_x, c_y, c_z)
centre = [int(i) for i in centre] # création d'une liste avec ces trois valeurs
r = int(input("Rayon de la sphère = "))
print()
print("Merci... C'est parti !")
# enregistrement des paramètres utilisateur

pavage(t, inf_gauche, sup_droit, longueur, col1, col2, col3, deformation, centre, r)
# initialisation de la fonction "pavage"
