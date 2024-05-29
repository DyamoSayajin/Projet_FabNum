# Projet_FabNum
Projet d'un quizz interactif sur Raspberry en collaboration avec la Gendarmerie (commandé par l'Education National) et dans le cadre de l'UE Fabrication Numérique. Ce quizz a pour but de sensibiliser les collégiens au harcèlement scolaire. 

Fonctionnalités : 
- Lecture d'un fichier texte contenant les questions, le fichier est formaté de manière à ce qu'il soit facilement remplissable.
- Quizz avec chrono, a deux joueurs, deux séries de trois buzzers (respectivement A,B,C)
- ESP32 auquel on a branché 6 fils pour faire des buzzers façon "Make Make" grâce à la fonction Touch de l'ESP32
- Fonction vocal grâce à la bibliothèque pyttsx3 (sur Windows) ou gTTS combiné à pydub (sur Raspberry Pi). 
