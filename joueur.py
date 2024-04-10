class Joueur:
    def __init__(self):
        self.score = 0

    def ajouterScore(self):
        self.score += 1
    
    def get_score(self):
        return self.score
    
    """
    def gagnant(self,joueur1,joueur2):
        if joueur1.score > joueur2.score:
            return "Le gagnant est " + joueur1.nom
        elif joueur1.score < joueur2.score:
            return "Le gagnant est" + joueur2.nom
        else:
            return "Egalité"
    """