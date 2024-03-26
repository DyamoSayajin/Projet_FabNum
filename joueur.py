class Joueur:
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score

    def ajouterScore(self):
        self.score += 1
    
    def donner_score(self):
        return self.score
    
    




# Création des joueurs
joueur1 = Joueur("Equipe 1", 0)
joueur2 = Joueur("Equipe 2", 0)