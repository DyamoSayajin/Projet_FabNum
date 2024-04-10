from Joueur import *
from time import time

class Quizz:
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

    def verifReponse(self,nombreAleatoire,joueur1,joueur2):
        tempsDebut = time()
        chrono = 0
        booleen = False
        buzzers = ''
        while booleen and chrono < 15:
            buzzers = str(input('Entrez la réponse des deux joueurs : '))
            print(buzzers)
            tempsFin = time()
            chrono = tempsDebut - tempsFin
            if buzzers != '':
                booleen = True

        reponseJoueur1 = buzzers.split('_',0)
        reponseJoueur2 = buzzers.split('_',1)
        print(reponseJoueur1)
        print(reponseJoueur2)


        if reponseJoueur1 == self.reponses[nombreAleatoire]:
            joueur1.ajouterScore()
            print("J1: Bonne réponse")
        else:
            print("J1: Mauvaise réponse")

        if reponseJoueur2 == self.reponses[nombreAleatoire]:
            joueur2.ajouterScore()
            print("J2: Bonne réponse")
        else:
            print("J2: Mauvaise réponse")

        
        """if input() ==  self.reponses[nombreAleatoire]: #remplacer input par l'input du buzzer à terme.
            joueur.ajouterScore()
            print("bonne réponse")
        else:
            print("mauvaise réponse")"""

    def poserQuestion(self,nombreAleatoire):
        
        self.lireQuestion(nombreAleatoire)
        self.lireProposition(nombreAleatoire)

