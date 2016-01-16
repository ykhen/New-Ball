"""
Fichier contenant le monde ainsi.
"""

import pygame
from pygame.locals import *


class WindowGame:
    """
    Class Gérant la fenêtre ainsi que les events du jeu
    """

    def __init__(self):
        """
        Fonction init
        :return:
        """

        # Initialisation de Pygame
        pygame.init()

        # Permet de savoir si la fenêtre doit être fermée
        self.is_run_loop = True




        # Initialisation des paramètres de la fenêtre
        self.window = pygame.display.set_mode((640, 480))

         # Scène principale
        self.scene = None


    def run_Loop(self):
        """
        Fonction principale. Elle permet de maintenir la fenêtre en "vie"
        :return:
        """

        while self.is_run_loop:
            #Event
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.is_run_loop = False

                if self.scene is not None:
                    #Il se peut que la position de la souris soit null, la souris n'est pas sur la fenêtre
                    try:
                        self.scene.mouse_dragg(event.pos[0], event.pos[1])
                    except AttributeError:
                        pass
                    #Clique sur le boutton
                    if event.type == MOUSEBUTTONDOWN:
                        #Clic droit
                        if event.button == 3:
                            self.scene.mouse_down_right(event.pos[0], event.pos[1])
                        #Clic gauche
                        if event.button == 1:
                            self.scene.mouse_down_left(event.pos[0], event.pos[1])
                        #Scroll en bas
                        if event.button == 5:
                            self.scene.scroll_down(event.pos[0], event.pos[1])
                        #Scroll en haut
                        if event.button == 4:
                            self.scene.scroll_up(event.pos[0], event.pos[1])
                    #Appuie sur une touche du clavier
                    if event.type == KEYDOWN:
                        self.scene.key_down(event.key)

            #Mis à jour de la scène et des sprites de la scène
            if self.scene is not None:
                self.scene.update_screen()
            #Met à jour l'écran
            pygame.display.flip()






class Scene:
    """
    Répresentation d'une scène
    """

    def __init__(self, window):
        """
        Initialiseur de la scène

        :param window: Fenêtre principale
        :return:
        """

        self.window = window

        self.sprites = []



    def update_screen(self):
        """
        A chaque fois que l'écran doit être mise à jour, cette fonction est appelé.
        :return:
        """

        for sprite in self.sprites:
            sprite.update_sprite()

    def mouse_dragg(self, coordinate_x, coordinate_y):
        """
        Est appelée à chaque fois update du screen pour savoir les coordonnées de la souris


        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre
        :return:
        """

        sprite = self.sprite_for_coordinate(coordinate_x, coordinate_y)
        if sprite is not None:
            sprite.mouse_dragg(coordinate_x, coordinate_y)

    def mouse_down_right(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur clic sur le boutton droit de la souris sur le sprite la fonction est appelée

        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre

        :return:
        """

        sprite = self.sprite_for_coordinate(coordinate_x, coordinate_y)
        if sprite is not None:
            sprite.mouse_down_right(coordinate_x, coordinate_y)


    def mouse_down_left(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur clic sur le boutton gauche de la souris, la fonction est appelée


        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre
        :return:
        """



        sprite = self.sprite_for_coordinate(coordinate_x, coordinate_y)
        if sprite is not None:
            sprite.mouse_down_left(coordinate_x, coordinate_y)


    def scroll_down(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur scroll en bas avec sa souris la fonction est appelée

        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre
        :return:
        """
        sprite = self.sprite_for_coordinate(coordinate_x, coordinate_y)
        if sprite is not None:
            sprite.scroll_down(coordinate_x, coordinate_y)

    def scroll_up(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur scroll en haut avec sa souris la fonction est appelée

        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre
        :return:
        """
        sprite = self.sprite_for_coordinate(coordinate_x, coordinate_y)
        if sprite is not None:
            sprite.scroll_up(coordinate_x, coordinate_y)



    def key_down(self, key_code):
        """
        Quand on clique sur une lettre, la fonction est appelée

        :param key_code: Code de la lettre
        :return:
        """
        pass

    def position_in_sprite(self, sprite, coordinate_x, coordinate_y):
        """
        Détermine si le sprite est bien dans les coordonnées pour les events comme la souris

        :param sprite: Sprite
        :param coordinate_x: Coordonnée de l'event
        :param coordinate_y: Coordonnée de l'event
        :return: bool
        """

        return sprite.rect.collidepoint(coordinate_x, coordinate_y)

    def sprite_for_coordinate(self, coordinate_x, coordinate_y):
        """
        Renvoie un sprite en fonction des bonnes coordonnées

        :param coordinate_x: x
        :param coordinate_y: y
        :return: Sprite
        """

        #Parcoure tous les sprites
        for sprite in self.sprites:

            #Verfie les positions
            if self.position_in_sprite(sprite, coordinate_x, coordinate_y):
                return sprite
        return None



class Sprite:
    """
    Répresentation d'un objet comme une balle ou un ennemi
    """

    def __init__(self, rect, window):
        """
        Initaliseur

        :param rect: Rectangle (pygame.Rect)
        :param window: Fenêtre principale
        :return:
        """

        self.rect = rect
        self.window = window



    def update_sprite(self):
        """
        Si on doit mettre à jour son sprite
        Ex : Le dessin d'une balle
        :return:

        """
        self.window.blit(self.image, (1, 1))


    def mouse_down_right(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur clic sur le boutton droit de la souris sur le sprite la fonction est appelée

        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre

        :return:
        """

        pass




    def mouse_down_left(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur clic sur le boutton gauche de la souris, la fonction est appelée


        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre
        :return:
        """

        pass

    def scroll_down(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur scroll en bas avec sa souris la fonction est appelée

        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre
        :return:
        """
        pass

    def scroll_up(self, coordinate_x, coordinate_y):
        """
        Quand l'utilisateur scroll en haut avec sa souris la fonction est appelée

        :param coordinate_x: Coordonnée x de la souris sur la fenêtre
        :param coordinate_y: Coordonnée y de la souris sur la fenêtre
        :return:
        """
        pass


    def mouse_dragg(self, coordinate_x, coordinate_y):
        """
        Si la souris passe dans le sprite, alors la fonction est appelée

        :param coordinate_x:  Coordonnée x de la souris sur la fenêtre
        :param coordinate_y:  Coordonnée y de la souris sur la fenêtre
        :return:
        """
        pass

    def key_down(self, key_code):
        """
        Quand on clique sur une lettre, la fonction est appelée

        :param key_code: Code de la lettre
        :return:
        """

        pass