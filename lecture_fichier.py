def lire_fichier(fichier):
    questions = []
    propositions = []
    reponses = []

    
    with open(fichier, 'r') as f:
        lignes = f.readlines() #Ajout de chaque lignes du fichier dans un tableau
        i = 0

        #Parcours de chaque ligne pour trier les questions, propositions et réponses.
        while i < len(lignes):
            #Si la ligne commence par le mot "Question" suivi de ":" alors on découpe la ligne pour placer la phrase dans le bon tableau
            if lignes[i].startswith("Question:"):
                questions.append(lignes[i].split(":", 1)[1].strip())

            #Cas ou la ligne commence par "Propositions:"
            #Les 3 prochaines lignes seront des propositions.
            elif lignes[i].startswith("Propositions:"):

                #On creer un autre tableau temporaire pour regrouper les 3 propositions dans une sous-liste.
                #La liste des propositions sera un tableau à deux dimensions ("une liste rempli de sous-liste").
                propositions_temp = []
                i += 1
                while not lignes[i].startswith("Reponse:"):
                    propositions_temp.append(lignes[i].strip())
                    i += 1
                propositions.append(propositions_temp)
                continue

            #De meme si la ligne commence par "Reponse:"
            elif lignes[i].startswith("Reponse:"):
                reponses.append(lignes[i].split(":", 1)[1].strip())
            i += 1

    return questions, propositions, reponses


# Affichage des questions, propositions et réponses (pour verifier)
"""for i, question in enumerate(questions):
    print("Question {}: {}".format(i+1, question))
    for j, proposition in enumerate(propositions[i]):
        print("  {}. {}".format(chr(97+j), proposition))
    print("Réponse: {}\n".format(reponses[i]))
"""
