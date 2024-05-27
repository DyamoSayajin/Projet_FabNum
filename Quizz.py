from joueur import *
import time

class Quizz:
    def __init__(self,questions,reponses,propositions):
        self.questions = questions
        self.reponses = reponses
        self.propositions = propositions

    def lireQuestion(self,nombreAleatoire,engine):
        engine.say(self.questions[nombreAleatoire])
        engine.runAndWait()
    
    def lireReponse(self,nombreAleatoire,engine):
        lettre_to_num = {'a': 0, 'b': 1, 'c':2}
        engine.say("La bonne réponse est {} ".format(self.propositions[nombreAleatoire][lettre_to_num[self.reponses[nombreAleatoire]]]))
        engine.runAndWait()

    def lireProposition(self,nombreAleatoire,engine):
        tab=[]
        for i in self.propositions[nombreAleatoire]:
            tab.append(i)
        text_to_speech = ' '.join(tab)

        engine.say(text_to_speech)
        engine.runAndWait()

    def decoder(self,rep1,rep2):
        dico = {'x':'a','y':'b','z':'c'}
        if rep1 in ['x','y','z']:
            rep1,rep2 = rep2,rep1
        if rep2 in ['x','y','z']:
            rep2 = dico[rep2]
        return rep1,rep2
    
    def getReponse(self,ser):
        tempsDebut = time.time()
        chrono = 0
        ser.open()
        while chrono < 15:
            rep1 = ser.read().decode("utf-8")
            rep2 = ser.read().decode("utf-8")
            rep1,rep2 = self.decoder(rep1,rep2)
            tempsFin = time.time()
            chrono = tempsFin - tempsDebut
        ser.close()
        return rep1,rep2
    
    
    def verifReponse(self,nombreAleatoire,rep1,rep2,joueur1,joueur2,engine):
        if rep1 == self.reponses[nombreAleatoire]:
            joueur1.ajouterScore()
            engine.say("Joueur 1, bonne réponse !")
            engine.runAndWait()
        else:
            engine.say("Joueur 1, mauvaise réponse !")
            engine.runAndWait()

        if rep2 == self.reponses[nombreAleatoire]:
            joueur2.ajouterScore()
            engine.say("Joueur 2, bonne réponse !")
            engine.runAndWait()
        else:
            engine.say("Joueur 2, mauvaise réponse !")
            engine.runAndWait()

    def donnerScore(self,joueur1,joueur2,engine):
        engine.say("Le Joueur 1 à {} points ".format(joueur1.getScore()))
        engine.say("Le Joueur 2 à {} points ".format(joueur2.getScore()))
        engine.runAndWait()