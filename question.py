import random
import lecture_fichier

questions, propositions, reponses = lecture_fichier.lire_fichier("reponses.txt")

class Questions:
    def __init__(self,questions,reponses,propositions):
        self.questions = questions
        self.reponses = reponses
        self.propositions = propositions

    def lireQuestion(self):
        print(self.questions[random.randint(0,2)])
    
    def lireReponse(self):
        pass

    def lireProposition(self):
        for i in range(0,3):
            print(self.propositions[i])

quizz = Questions(questions,reponses,propositions)
quizz.lireQuestion()
quizz.lireProposition()
quizz.lireReponse()