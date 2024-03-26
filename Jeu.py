class Jeu:

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur_actuel = 0


    def changer_joueur(self):
        if self.joueur_actuel == 0:
            self.joueur_actuel = 1
        else:
            self.joueur_actuel = 0  

