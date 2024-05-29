# Projet_FabNum
Projet d'un quizz interactif sur Raspberry en collaboration avec la Gendarmerie (commandé par l'Education National) et dans le cadre de l'UE Fabrication Numérique. Ce quizz a pour but de sensibiliser les collégiens au harcèlement scolaire. 

Fonctionnalités : 
- Lecture d'un fichier texte contenant les questions, le fichier est formaté de manière à ce qu'il soit facilement remplissable.
- Quizz avec chrono, a deux joueurs, deux séries de trois buzzers (respectivement A,B,C)
- ESP32 auquel on a branché 6 fils pour faire des buzzers façon "Make Make" grâce à la fonction Touch de l'ESP32
- Fonction vocal grâce à la bibliothèque pyttsx3 (sur Windows) ou gTTS combiné à pydub (sur Raspberry Pi). 

Note importante : Tous les commits jusqu'au 17ème ont été développé sur Windows et ne tiennent pas compte de modification avec gTTS et pydub sur Raspberry.

Ce projet a été developpé par Alan, Noa, Hichem, Theo.
En cas de reprise de ce projet par un autre groupe d'élève de l'UE FabNum vous pouvez contacter : noajuguera@hotmail.com pour des renseignements.
