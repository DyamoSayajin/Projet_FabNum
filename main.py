import random
import serial

import lecture_fichier
from joueur import *
from Quizz import *

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM5'




questions, propositions, reponses = lecture_fichier.lire_fichier(r"C:\Users\hiche\OneDrive\Documents\S2\FabNum\Stop_bullying\Projet_FabNum\reponses.txt")

quizz = Quizz(questions,reponses,propositions)
joueur1 = Joueur()
joueur2 = Joueur()
while True:
    nombreAleatoire = random.randint(0,2)
    quizz.poserQuestion(nombreAleatoire)
    time.sleep(5)
    quizz.getReponse(nombreAleatoire,ser,joueur1,joueur2)
    quizz.lireReponse(nombreAleatoire)
    time.sleep(5)
    print(joueur1.get_score())
    print(joueur2.get_score())
