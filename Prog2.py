# -*- coding:Latin-1 -*-

chaine = str() # Crée une chaîne vide
# On aurait obtenu le même résultat en tapant chaine = ""

#while chaine.lower() != "q":
#    print("Tapez 'Q' pour quitter...")
 #    chaine = input()

#print("Merci !")


nom = "villoz"
prenom = "sébastien"
age = 36

print("J'ai {2} ans, je m'appelle {0} {1}". \
      format(nom.capitalize(), prenom.capitalize(), age))

print("J'ai {age} ans, je m'appelle {prenom} {nom}". \
      format(nom = "Dupont", prenom = "Daniel", age= 20))

for i in nom:
    print(i)

i=0
while i<len(prenom):
    print(prenom[i])
    i+=1

maListe = [230,23,451,34,2]

i = 0
while i<len(maListe):
    print(maListe[i])
    i+=1


for i in maListe:
    print(i)

for i, element in enumerate(maListe):
    print("Indice {}, valeur {}".format(i, element))

NouvelleListe = []
for element in enumerate(maListe):
    NouvelleListe.append(element)
    print(element)


def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""
    
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
nb_fruits=[nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes]#if nb_fruits>qtt_a_retirer]
print(nb_fruits)


