#!/usr/bin/env python3

import os
from random import randrange
from math import ceil

argent = 5000
continuer_partie = True
print "Vous arrivez a la table de la roulette avec", argent, "$."
while continuer_partie:
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Faites vos jeux ! Sur quel nombre voulez-vous miser ? (entre 0 et 49) : ")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Le nombre est negatif")
        if nombre_mise > 49:
            print("Le nombre est superieur a 49")
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Saisissez le montant de votre mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("Montant eronne")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est negative ou nulle.")
        if mise > argent:
            print("Hola Hola ! Du calme, vous ne pouvez pas miser autant !!! Vous n'avez que", argent, "$")
    numero_gagnant = randrange(50)
    print("Les jeux sont faits... et la roulette s'arrete sur le numero", numero_gagnant,  "!")
    if numero_gagnant == nombre_mise:
        print("Felicitations ! Vous avez gagne", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2:
        mise = ceil(mise * 0.5)
        print("Vous avez mise sur la bonne couleur. Vous obtenez", mise, "$")
        argent += mise
    else:
        print("Desole, ce n'est pas pour cette fois... Vous perdez votre mise.")
        argent -= mise
    if argent <= 0:
        print("Vous etes ruine ! Votre femme vous attend a la maison avec le rouleau a patisserie...")
        continuer_partie = False
    else:
        print("Votre cagnote est de ", argent, "$")
        quitter = input("Souhaitez-vous quitter la roulette (o/n) ? ")
        if quitter == "o":
            print("Vous quittez la table avec ", argent, "$")
            continuer_partie = False
