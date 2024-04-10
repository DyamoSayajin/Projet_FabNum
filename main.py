import random

import lecture_fichier
from Joueur import *
from Quizz import *


nombreAleatoire = random.randint(0,2)
questions, propositions, reponses = lecture_fichier.lire_fichier("reponses.txt")

quizz = Quizz(questions,reponses,propositions)
joueur1 = Joueur()
joueur2 = Joueur()

quizz.poserQuestion(nombreAleatoire)
quizz.verifReponse(nombreAleatoire,joueur1,joueur2)
print(joueur1.get_score())
print(joueur2.get_score())
