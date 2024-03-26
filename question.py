import random
import lecture_fichier

questions, propositions, reponses = lecture_fichier.lire_fichier("reponses.txt")
nombre_aleatoire = random.randint(0,2)
class Questions:
    def __init__(self,questions,reponses,propositions,bonne_reponse):
        self.questions = questions
        self.reponses = reponses
        self.propositions = propositions
        self.bonne_reponse = bonne_reponse

    def lireQuestion(self):
        print(self.questions[nombre_aleatoire])
    
    def lireReponse(self):
        print(self.reponses[nombre_aleatoire])

    def lireProposition(self):
      print(self.propositions[nombre_aleatoire])

    

    def verifier_reponse(self,reponses):
        return reponses == self.bonne_reponse

quizz = Questions(questions,reponses,propositions,0)
quizz.lireQuestion()
quizz.lireProposition()
quizz.lireReponse()