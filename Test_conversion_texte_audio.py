# coding: utf-8
# module requis pour convertir le texte en vocale
from gtts import gTTS
import os  
from question import *
import lecture_fichier
questions, propositions, reponses = lecture_fichier.lire_fichier("reponses.txt")

# Ce module est importé pour que nous puissions
# lire l'audio converti
 
  
# Le texte que vous souhaitez cronvertir en audio
#mytext = "Bienvenue sur le quizz de StopBulliyng. Vous allez répondre à 3 questions. Pour chaque question, vous aurez 3 propositions. A la fin du quizz, vous aurez votre score. Bonne chance !"
question = ''.join(questions)


  
# Choisir le langage vocale
language = 'fr'
  
# Passer le texte et la langue au moteur de convertion gTTS,
# ici nous avons marqué slow=False. Qui marque que l'audio 
#doit avoir une vitesse non ralentie
textSpeech1 = gTTS(text=question, lang=language, slow=False)

# Enregistrer l'audio converti dans un fichier nommé bienvenue.mp3 
textSpeech1.save("question.mp3")

# lire le fichier audio
os.popen("question.mp3")