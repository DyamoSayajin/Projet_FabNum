import random
import serial
import pyttsx3

import lecture_fichier
from joueur import *
from Quizz import *

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM6'

engine = pyttsx3.init()
engine.setProperty('rate', 130)

questions, propositions, reponses = lecture_fichier.lire_fichier(r"Mettez ici le chemin absolue vers le fichier reponses")

quizz = Quizz(questions,reponses,propositions)
joueur1 = Joueur(0)
joueur2 = Joueur(0)

i = 0
while i<5:
    nombreAleatoire = random.randint(0,len(questions)-1)
    quizz.lireQuestion(nombreAleatoire,engine)
    time.sleep(1)
    quizz.lireProposition(nombreAleatoire,engine)
    time.sleep(1)
    rep1,rep2 = quizz.getReponse(ser)
    quizz.lireReponse(nombreAleatoire,engine)
    time.sleep(1)
    quizz.verifReponse(nombreAleatoire,rep1,rep2,joueur1,joueur2,engine)
    time.sleep(1)
    quizz.donnerScore(joueur1,joueur2,engine)
    i+=1
