"""
Fichier contenant le jeu
"""

from World import WindowGame, Sprite, Scene, RECT_WINDOW
from Niveau import SceneLevel2


class MainWindow(WindowGame):
    """
    Class Contenant le jeu à lui
    """
    def __init__(self):
        WindowGame.__init__(self)
        self.scene = SceneLevel2(self.window)


