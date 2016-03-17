"""
Fichier qui gère la vue de la liste des niveaux
"""


from World import *
import pygame
COLOR_NIVEAU_1_BUTTON = (34, 167, 240)
SIZE_BUTTON = 50

class ListeNiveau(Scene):
    """
    Liste de tous les niveaux
    """

    def __init__(self, window):
        Scene.__init__(self, window)
        self.button_level_1 = ButtonNiveau(pygame.Rect(RECT_WINDOW.width / 2 - SIZE_BUTTON / 2, (RECT_WINDOW.height / 2 - 100) - SIZE_BUTTON, SIZE_BUTTON, SIZE_BUTTON), self.window, COLOR_NIVEAU_1_BUTTON,  pygame.font.SysFont("Cooper Black", 80), "1")
        self.button_level_1.action = self.show_niveau_1
        self.sprites.append(self.button_level_1)

        self.button_level_2 = ButtonNiveau(pygame.Rect(RECT_WINDOW.width / 2 - SIZE_BUTTON / 2 , (RECT_WINDOW.height / 2 + 100) - SIZE_BUTTON, SIZE_BUTTON, SIZE_BUTTON), self.window, COLOR_NIVEAU_1_BUTTON,  pygame.font.SysFont("Cooper Black", 80), "2")
        self.button_level_2.action = self.show_niveau_2
        self.sprites.append(self.button_level_2)

        self.delegate = None

    def show_niveau_1(self):
        """
        Affiche le niveau par l'intermédiare du delegate
        :return:
        """
        if self.delegate:
            self.delegate.start_niveau_1()

    def show_niveau_2(self):
        """
        Affiche le niveau 2 par l'intermédiare du delegate
        :return:
        """
        if self.delegate:
            self.delegate.start_niveau_2()

class ButtonNiveau(Sprite):
    """
    Class du bouton play
    """
    def __init__(self, rect, window, color, font, string):
        Sprite.__init__(self, rect, window)

        self.font = font
        self.color = color
        self.string = string

        #Action de callBack
        self.action = None

    def update_sprite(self):
        pygame.draw.circle(self.window, self.color, (self.rect.centerx, self.rect.centery), self.rect.height + 5)
        label = self.font.render(self.string, 1, (255, 255, 255))
        self.window.blit(label, (((self.rect.x - self.rect.width / 2) + self.rect.width) - label.get_rect().width / 2, ((self.rect.y - self.rect.height / 2) + self.rect.height) -  label.get_rect().height / 2))


    def mouse_down_left(self, coordinate_x, coordinate_y):
        print("Je march sur mes pieds")
        if self.action:
            self.action()

