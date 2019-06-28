# -*- coding:Latin-1 -*-

#Méthode classique mais la fermture du fichier ne se fait pas automatiquement

#mon_fichier = open("fichier.txt", "r") # read
#contenu = mon_fichier.read()
#print(contenu)

#mon_fichier.close()


#mon_fichier = open("fichier.txt", "w") # write
#mon_fichier.write("Nouveau texte écrit")

#mon_fichier.close()


# A utiliser de préférence
# ferme le fichier automatiquement même si une erreur se produit

with open('fichier.txt', 'w') as mon_fichier:
    mon_fichier.write("Ceci est un texte écrit suite à un with")
