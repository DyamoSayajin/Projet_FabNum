# coding: utf-8
# module requis pour convertir le texte en vocale
from gtts import gTTS
import os  
# Ce module est importé pour que nous puissions
# lire l'audio converti
 
  
# Le texte que vous souhaitez convertir en audio
mytext = 'Test je suis un texte converti en audio'
  
# Choisir le langage vocale
language = 'fr'
  
# Passer le texte et la langue au moteur de convertion gTTS,
# ici nous avons marqué slow=False. Qui marque que l'audio 
#doit avoir une vitesse non ralentie
textSpeech = gTTS(text=mytext, lang=language, slow=False)
  
# Enregistrer l'audio converti dans un fichier nommé bienvenue.mp3 
textSpeech.save("bienvenue.mp3")
  
# lire le fichier audio
os.popen("bienvenue.mp3")