from question import *
import lecture_fichier
from joueur import *

nombreAleatoire = random.randint(0,2)
questions, propositions, reponses = lecture_fichier.lire_fichier("reponses.txt")

quizz = Questions(questions,reponses,propositions)
joueur1 = Joueur("Equipe 1", 0)
joueur2 = Joueur("Equipe 2", 0)

quizz.poserQuestion(nombreAleatoire)
quizz.verifReponse(nombreAleatoire,joueur1)
quizz.verifReponse(nombreAleatoire,joueur2)
print(joueur1.donner_score())
print(joueur2.donner_score())
