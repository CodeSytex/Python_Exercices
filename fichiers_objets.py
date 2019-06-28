# -*- coding:Latin-1 -*-

import pickle

score = {
    "joueur 1": 5,
    "joueur 2": 3,
    "joueur 3": 54,
    "joueur 4": 22,
    "joueur 5": 51,
    }

with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

with open('donnees', 'rb') as fichier:
    mon_unpickler = pickle.Unpickler(fichier)
    score_recupere = mon_unpickler.load()

print(score_recupere)
