"""
Code contenant le menu
"""
COLOR_BUTTON = (34, 167, 240)

import pygame
from World import Scene, Sprite, RECT_WINDOW

class Menu(Scene):
    """
    Class du menu
    """
    def __init__(self, window):
        Scene.__init__(self, window)
        #Instance du niveau 1
        self.niveau_1 = None

        #Instance du niveau 2
        self.niveau_2 = None

        #Delegate, mecanisme permettant d'appeler en arrière
        self.delegate = None


        #Instance du button play
        size_button = pygame.Rect(0, 0, 300, 100)
        size_button.x = RECT_WINDOW.width / 2 - size_button.width / 2
        size_button.y = RECT_WINDOW.height / 2 - size_button.height / 2

        self.button_play = ButtonPlay(size_button, self.window)
        self.sprites.append(self.button_play)

        self.button_play.action = self.start_niveau_action


    def start_niveau_action(self):
        if self.delegate:
            self.delegate.show_liste_niveau()

    def update_screen(self):
        Scene.update_screen(self)



class ButtonPlay(Sprite):
    """
    Class du bouton play
    """
    def __init__(self, rect, window):
        Sprite.__init__(self, rect, window)

        self.font = pygame.font.SysFont("Cooper Black", 80)

        #Action de callBack
        self.action = None

    def update_sprite(self):
        pygame.draw.circle(self.window, COLOR_BUTTON, (self.rect.centerx, self.rect.centery), self.rect.height + 5)
        label = self.font.render("Play", 1, (255, 255, 255))
        self.window.blit(label, (RECT_WINDOW.width / 2 - label.get_rect().width / 2, RECT_WINDOW.height / 2 - label.get_rect().height / 2))


    def mouse_down_left(self, coordinate_x, coordinate_y):
        if self.action:
            self.action()

    def mouse_entered(self):
        self.font = pygame.font.SysFont("Cooper Black", 85)

    def mouse_exited(self):
        self.font = pygame.font.SysFont("Cooper Black", 80)