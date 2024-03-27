import random
import lecture_fichier
from joueur import *


questions, propositions, reponses = lecture_fichier.lire_fichier("reponses.txt")

class Questions:
    def __init__(self,questions,reponses,propositions):
        self.questions = questions
        self.reponses = reponses
        self.propositions = propositions

    def lireQuestion(self,nombreAleatoire):
        print(self.questions[nombreAleatoire])
    
    def lireReponse(self,nombreAleatoire):
        print(self.reponses[nombreAleatoire])

    def lireProposition(self,nombreAleatoire):
      print(self.propositions[nombreAleatoire])

    def inputJoueur(self):
        pass
    
    def verifReponse(self,nombreAleatoire,joueur):
        if input() ==  reponses[nombreAleatoire]: #remplacer input par l'input du buzzer à terme.
            joueur.ajouterScore()
            print("bonne réponse")
        else:
            print("mauvaise réponse")

    def poserQuestion(self,nombreAleatoire):
        
        self.lireQuestion(nombreAleatoire)
        self.lireProposition(nombreAleatoire)

        
            
"""
quizz = Questions(questions,reponses,propositions)
quizz.poserQuestion()
"""
