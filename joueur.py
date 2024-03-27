class Joueur:
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score

    def ajouterScore(self):
        self.score += 1
    
    def donner_score(self):
        return self.score
    
    def gagnant(self,joueur1,joueur2):
        if joueur1.score > joueur2.score:
            return "Le gagnant est " + joueur1.nom
        elif joueur1.score < joueur2.score:
            return "Le gagnant est" + joueur2.nom
        else:
            return "Egalité"




# Création des joueurs
joueur1 = Joueur("Equipe 1", 0)
joueur2 = Joueur("Equipe 2", 0)