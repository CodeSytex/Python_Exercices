# -*-coding:Latin-1 -*
def tableMultiplication(nb,max=12):
    i = 0

    while i < max:
        print(i+1,"*", nb, "=", (i+1)*nb)
        i += 1

# test de la fonction
# Code pas exécuter si appellé d'un autre programme

if __name__ == "__main__":
    tableMultiplication(4)
