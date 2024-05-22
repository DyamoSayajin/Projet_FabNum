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
joueur1 = Joueur(0)
joueur2 = Joueur(0)
i = 0
while i<5:
    nombreAleatoire = random.randint(0,len(questions)-1)
    quizz.poserQuestion(nombreAleatoire)
    time.sleep(5)
    quizz.getReponse(nombreAleatoire,ser,joueur1,joueur2)
    quizz.lireReponse(nombreAleatoire)
    time.sleep(5)
    engine = pyttsx3.init()
    engine.say("le joueur 1 à " + joueur1.getScore())
    engine.say("le joueur 2  à " + joueur2.getScore())
    engine.runAndWait()
    i+=1
