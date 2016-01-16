"""
Fichier où il y a tous les niveaux
"""

from World import WindowGame, Sprite, Scene, RECT_WINDOW
import pygame
from pygame.locals import *
import random

#-----------------------------------------------------------------------------------------------------------------------
#                                                           Niveau 1
#-----------------------------------------------------------------------------------------------------------------------

class SceneLevel1(Scene):
    """
    Scène du niveau 1
    """
    def __init__(self, window):
        Scene.__init__(self, window)

        #Bar principale
        self.bar = Bar(pygame.Rect(100, 450, 75, 20), self.window)
        self.sprites.append(self.bar)

        #Timer pour les apparitions des balles
        self.last_time_show_balle = pygame.time.get_ticks()

        #Les balles apparaissent toutes les self.show_ball_time en milliseconde
        self.show_ball_time = 1000

        #Timer pour avancer la difficulter
        self.last_time_advance_difficult = pygame.time.get_ticks()

        #Difficulté du niveau 1
        #Elle représente l'avancement des balles
        self.difficulties = 1

        #Cache la souris
        pygame.mouse.set_visible(False)


    def mouse_dragg(self, coordinate_x, coordinate_y):
        #Modifie la bar
        if coordinate_x >= 1 and coordinate_x <= RECT_WINDOW.width - self.bar.rect.width:
            self.sprites[0].rect.x = coordinate_x


    def update_screen(self):
        #Appèle de la super class
        Scene.update_screen(self)

        now_time = pygame.time.get_ticks()
        if now_time - self.last_time_show_balle >= self.show_ball_time:
            self.last_time_show_balle = now_time
            self.sprites.append(Ball(pygame.Rect(random.randint(10, RECT_WINDOW.width - 10), 0, 10, 10), self.window))

        if now_time - self.last_time_advance_difficult >= 10000:
            self.last_time_advance_difficult = now_time
            if self.difficulties <= 10:
                self.show_ball_time -= 65
                self.difficulties += 1




        #Fais descendre les bales
        for sprite in self.sprites:
            if isinstance(sprite, Ball):

                #Collision avec la bar
                if self.bar.rect.colliderect(sprite.rect):
                    sprite.move_up = True
                if sprite.move_up:
                    sprite.rect.y -= self.difficulties + 2
                else:
                    sprite.rect.y += self.difficulties
                #Quand la barre sort de la fenêtre
                if sprite.rect.colliderect(RECT_WINDOW) != True:
                    #La ball sort du haut de l'écran
                    if sprite.rect.y <= 0:
                        self.sprites.remove(sprite)
                    else:
                        #On perd
                        print("Je perds une 1 ball")
                        self.sprites.remove(sprite)
                        pass



class Bar(Sprite):
    """
    Bar qui fait rebondir les balles
    """


    def update_sprite(self):
        pygame.draw.rect(self.window, (46, 204, 113), self.rect)


class Ball(Sprite):
    """
    Balles
    """

    def __init__(self, rect, window):
        Sprite.__init__(self, rect, window)

        #Permet de savoir si la balle va en haut ou en bas
        self.move_up = False


    def update_sprite(self):
        pygame.draw.circle(self.window, (46, 204, 113), (self.rect.x, self.rect.y), self.rect.width)
