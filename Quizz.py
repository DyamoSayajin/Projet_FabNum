from joueur import *
import time
import serial
from gtts import gTTS
import os 


class Quizz:
    def __init__(self,questions,reponses,propositions):
        self.questions = questions
        self.reponses = reponses
        self.propositions = propositions

    def lireQuestion(self,nombreAleatoire):
        #print(self.questions[nombreAleatoire])
        q = gTTS(text = self.questions[nombreAleatoire], lang = 'fr', slow = False)
        q.save("question.mp3")
        os.popen("question.mp3")
    
    def lireReponse(self,nombreAleatoire):
        #print(self.reponses[nombreAleatoire])
        r = gTTS(text = "la réponse est " + self.reponses[nombreAleatoire], lang = 'fr', slow = True)
        r.save("reponse.mp3")
        os.popen("reponse.mp3")

    def lireProposition(self,nombreAleatoire):
        #print(self.propositions[nombreAleatoire])
        tab=[]
        for i in self.propositions[nombreAleatoire]:
            tab.append(i)
        print(tab)
        text_to_speak = ' '.join(tab)
        p = gTTS(text = text_to_speak, lang = 'fr', slow = False)

        p.save("proposition.mp3")
        os.popen("proposition.mp3")

    def decoder(self,rep1,rep2):
        dico = {'x':'a','y':'b','z':'c'}
        if rep1 in ['x','y','z']:
            rep1,rep2 = rep2,rep1
        if rep2 in ['x','y','z']:
            rep2 = dico[rep2]
        return rep1,rep2
    
    def getReponse(self,nombreAleatoire,ser,joueur1,joueur2):
        tempsDebut = time.time()
        chrono = 0
        ser.open()
        while chrono < 15:
            rep1 = ser.read().decode("utf-8")
            rep2 = ser.read().decode("utf-8")
            rep1,rep2 = self.decoder(rep1,rep2)
            #time.sleep(1)
            #print(rep1,rep2)
            tempsFin = time.time()
            chrono = tempsFin - tempsDebut
        ser.close()
        self.verifReponse(nombreAleatoire,rep1,rep2,joueur1,joueur2)
    
    
    def verifReponse(self,nombreAleatoire,rep1,rep2,joueur1,joueur2):

        if rep1 == self.reponses[nombreAleatoire]:
            joueur1.ajouterScore()
            print("J1: Bonne réponse")
        else:
            print("J1: Mauvaise réponse")

        if rep2 == self.reponses[nombreAleatoire]:
            joueur2.ajouterScore()
            print("J2: Bonne réponse")
        else:
            print("J2: Mauvaise réponse")

    def poserQuestion(self,nombreAleatoire):
        self.lireQuestion(nombreAleatoire)
        time.sleep(5)
        self.lireProposition(nombreAleatoire)
