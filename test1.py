# -*- coding:Latin-1 -*-
import os

bissextile = False

annee = "A"

while(annee != "Q"):
    annee = input('Saisissez une année ou Q pour arrêter : ')

    if annee !="Q":
        try:
            annee = int(annee)
            #if annee <=0:
            #    raise ValueError("L'année saisie est négative ou nulle")
            assert annee > 0

            if annee % 400 == 0:
                bissextile = False
            elif annee % 100 == 0:
                bissextile = False
            elif annee % 4 == 0:
                bissextile = True
            else:
                bissextile = False

            if bissextile:
                print("L'année ", annee, "est bissextile")
            else:
                print("L'année ", annee, " n'est pas bissextile")

        except ValueError as exception_return: 
            print("Ceci :", annee, "n'est pas une année correcte :", exception_return)
        except AssertionError:
            print("L'année saisie inférieur ou égale à 0")
    else:
        os.system("pause")
        print("Le programme va s'arrêter")
