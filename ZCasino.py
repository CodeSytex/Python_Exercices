# -*- coding:Latin-1 -*-

import random
import time

Argent = 1000

Continue = True

print("*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*")
print("*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*")
print("           Bonjour et bienvenue au Casino               ")
print("*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*")
print("*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*")
print(" ")
print("Voici votre somme de départ : ", Argent)
print(" ")
print("Nous allons jouer au jeu de la roulette")
print(" ")

while Continue:

    NombreChoisi = -1
    while NombreChoisi < 0 or NombreChoisi > 49:
        NombreChoisi = input("Choisissez une nombre entre 0 et 49: ")

        try:
            NombreChoisi = int(NombreChoisi)
            assert NombreChoisi >=0 and NombreChoisi <49

        except ValueError:
            print("Le nombre choisi n'est pas correct")
        except AssertionError:
            print("Le nombre choisi n'est pas valable")


    Mise = -1

    while Mise < 0 or Mise > Argent:
        print("Montant disponible : ", Argent)
        Mise = input("Quelle somme voulez-vous miser ? ")

        try:
            Mise = int(Mise)
            if Mise > Argent:
               print("Vous n'avez pas cette somme")
            if Mise < 0:
                print("La mise doit être plus grande que 0")
        except ValueError:
            print("Somme mise pas correcte")

    Argent = Argent - Mise
    print("Les jeux sont faits, rien ne va plus")
    print("La roulette tourne")

    RouletteTourne = 0
    while RouletteTourne < 5:
        RouletteTourne += 1
        time.sleep(1)
        print("...")
    

    NombreAleatoire = random.randrange(49)

    print("La bille s'est arrêtée sur la case :", NombreAleatoire)

    if NombreAleatoire == NombreChoisi:
        print("Vous êtes tombé sur le bon chiffre ! ")
        Gain = Mise * 3
        Argent = Argent + Gain
        print("Votre gain : ", Gain)

    elif NombreAleatoire%2 == NombreChoisi%2:
        print("Vous avez choisi la bonne couleur")
        Gain = Mise * 0.5
        print("Votre gain : ", Gain)
        Argent = Argent + Gain
        
    else:
        print("Désolé vous avez perdu")

    print("Votre nouveau montant disponible : ", Argent)

    if Argent >0:
        TestReponse = True
        while TestReponse:
            ContinuezLeJeu = input("Voulez-vous rejouer ? O/N : ")
            if ContinuezLeJeu == "O" or ContinuezLeJeu == "o":
                TestReponse = False
            elif ContinuezLeJeu == "N" or ContinuezLeJeu == "n":
                print("A la prochaine ! ")
                Continue = False
                TestReponse = False
            else:
                print("Réponse pas valable")
    else:
        print("Vous n'avez plus d'argent, le jeu s'arrête")
        Continue = False
    
    
