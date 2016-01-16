"""
Fichier contenant le jeu
"""

from World import WindowGame, Sprite, Scene, RECT_WINDOW
from Niveau import SceneLevel1


class MainWindow(WindowGame):
    """
    Class Contenant le jeu à lui
    """
    def __init__(self):
        WindowGame.__init__(self)
        self.scene = SceneLevel1(self.window)


