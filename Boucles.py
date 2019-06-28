def tableMultiplication(nb,max=12):
    i = 0

    while i < 12:
        print(i+1,"*", nb, "=", (i+1)*nb)
        i += 1
nb = 1

while nb !=0:
    
    nb = input("Donnez un chiffre : ")
    nb = int(nb)
    if nb !=0:
        tableMultiplication(nb)
    else:
        print("Fin du programme")
