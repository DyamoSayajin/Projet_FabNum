def lire_fichier(fichier):
    questions = []
    propositions = []
    reponses = []

    with open(fichier, 'r') as f:
        lignes = f.readlines()
        i = 0
        while i < len(lignes):
            if lignes[i].startswith("Question:"):
                questions.append(lignes[i].split(":", 1)[1].strip())
            elif lignes[i].startswith("Propositions:"):
                propositions_temp = []
                i += 1
                while not lignes[i].startswith("Reponse:"):
                    propositions_temp.append(lignes[i].strip())
                    i += 1
                propositions.append(propositions_temp)
                continue
            elif lignes[i].startswith("Reponse:"):
                reponses.append(lignes[i].split(":", 1)[1].strip())
            i += 1

    return questions, propositions, reponses


# Affichage des questions, propositions et réponses
"""for i, question in enumerate(questions):
    print("Question {}: {}".format(i+1, question))
    for j, proposition in enumerate(propositions[i]):
        print("  {}. {}".format(chr(97+j), proposition))
    print("Réponse: {}\n".format(reponses[i]))
"""