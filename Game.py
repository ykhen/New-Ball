"""
Fichier contenant le jeu
"""

from World import WindowGame, Sprite, Scene, RECT_WINDOW
from ListeNiveau import *
from Niveau import SceneLevel2, SceneLevel1
from Menu import *

MENU_TAG = 0
NIVEAU_1_TAG = 1
NIVEAU_2_TAG = 2
LISTE_TAG = 3

class MainWindow(WindowGame):
    """
    Class Contenant le jeu à lui
    """



    def __init__(self):
        WindowGame.__init__(self)

        #Instance du niveau 1
        self.scene_niveau_1 = SceneLevel1(self.window)

        #Instace du niveau 2
        self.scene_niveau_2 = SceneLevel2(self.window)

        #Instance de la liste des niveaux
        self.scene_liste_niveau = ListeNiveau(self.window)
        self.scene_liste_niveau.delegate = self

        #Instance du menu
        self.scene_menu = Menu(self.window)
        self.scene_menu.delegate = self
        self.change_scene(MENU_TAG)

    def change_scene(self, tag):
        """
        Change la scene avec le tag correspond
        :param tag: Tag correspondant à la scene
        :return:
        """

        if tag == MENU_TAG:
            self.scene = self.scene_menu
        elif tag == NIVEAU_2_TAG:
            self.scene = self.scene_niveau_2
        elif tag == LISTE_TAG:
            self.scene = self.scene_liste_niveau
        elif tag == NIVEAU_1_TAG:
            self.scene = self.scene_niveau_1

    def start_niveau_1(self):
        """
        Démarre le niveau 1
        :return:
        """
        self.change_scene(NIVEAU_1_TAG)

    def start_niveau_2(self):
        """
        Démarre le niveau 2
        """
        self.change_scene(NIVEAU_2_TAG)

    def show_liste_niveau(self):
        """
        Affiche la liste de niveau
        :return:
        """

        self.change_scene(LISTE_TAG)

