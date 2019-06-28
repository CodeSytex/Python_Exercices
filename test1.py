# -*- coding:Latin-1 -*-
import os

bissextile = False

annee = "A"

while(annee != "Q"):
    annee = input('Saisissez une ann�e ou Q pour arr�ter : ')

    if annee !="Q":
        try:
            annee = int(annee)
            #if annee <=0:
            #    raise ValueError("L'ann�e saisie est n�gative ou nulle")
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
                print("L'ann�e ", annee, "est bissextile")
            else:
                print("L'ann�e ", annee, " n'est pas bissextile")

        except ValueError as exception_return: 
            print("Ceci :", annee, "n'est pas une ann�e correcte :", exception_return)
        except AssertionError:
            print("L'ann�e saisie inf�rieur ou �gale � 0")
    else:
        os.system("pause")
        print("Le programme va s'arr�ter")
