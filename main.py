import random
import serial

import lecture_fichier
from joueur import *
from Quizz import *

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM6'

nombreAleatoire = random.randint(0,2)
questions, propositions, reponses = lecture_fichier.lire_fichier(r"D:\Users\Noa\Documents\GitHub\Projet_FabNum\reponses.txt")

quizz = Quizz(questions,reponses,propositions)
joueur1 = Joueur()
joueur2 = Joueur()

quizz.poserQuestion(nombreAleatoire)
quizz.getReponse(nombreAleatoire,ser,joueur1,joueur2)
print(joueur1.get_score())
print(joueur2.get_score())
