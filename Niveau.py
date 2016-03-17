"""
Fichier où il y a tous les niveaux
"""

from World import WindowGame, Sprite, Scene, RECT_WINDOW
import pygame
from pygame.locals import *
import random

SIZE_BALL = 20
BAR_COLOR = (207, 0, 15)
BACKGROUND_COLOR = (44, 62, 80)
LINE_COLOR = BAR_COLOR
LABEL_SCORE_COLOR = LINE_COLOR
BALL_COLORS = ((191, 191, 191), (154, 18, 179), (249, 191, 59), (148, 62, 84), (0, 150, 0))
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




    def mouse_dragg(self, coordinate_x, coordinate_y):
        #Modifie la bar
        self.bar.rect.x = coordinate_x - self.bar.rect.width / 2




    def update_screen(self):
        #Appèle de la super class
        Scene.update_screen(self)

        pygame.time.delay(8)

        now_time = pygame.time.get_ticks()
        if now_time - self.last_time_show_balle >= self.show_ball_time:
            self.last_time_show_balle = now_time
            self.sprites.append(Ball(pygame.Rect(random.randint(SIZE_BALL, RECT_WINDOW.width - SIZE_BALL), 0, SIZE_BALL, SIZE_BALL), self.window))

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



#-----------------------------------------------------------------------------------------------------------------------
#                                                           Niveau 2
#-----------------------------------------------------------------------------------------------------------------------
class SceneLevel2(Scene):
    """
    Scène du niveau 1
    """
    def __init__(self, window):
        Scene.__init__(self, window)

        #Bar principale
        self.bar = Bar(pygame.Rect(100, RECT_WINDOW.height / 2 - 20 / 2, 75, 20), self.window)
        self.sprites.append(self.bar)

         #Ajout de la line pour séparer les zones
        self.sprites.append(LineLimite(pygame.Rect(0, RECT_WINDOW.height / 2, RECT_WINDOW.width, 2), self.window))

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
        #pygame.mouse.set_visible(False)

        #Boolean qui permet de savoir si on affiche la ball en haut ou en bas
        self.show_ball_up = True

        #Scores
        self.scores = 0

        #Police de caractère du label scores
        self.font_scores = pygame.font.SysFont("Colibri", 50)






    def mouse_dragg(self, coordinate_x, coordinate_y):
        #Modifie la bar

        self.bar.rect.x = coordinate_x - self.bar.rect.width / 2


    def update_screen(self):
        pygame.draw.rect(self.window, BACKGROUND_COLOR, pygame.Rect(0, 0, RECT_WINDOW.width, RECT_WINDOW.height))
        #Appèle de la super class
        Scene.update_screen(self)


        pygame.time.delay(8)

        now_time = pygame.time.get_ticks()
        #Ajoute la ball
        if now_time - self.last_time_show_balle >= self.show_ball_time:
            self.last_time_show_balle = now_time

            #Si la ball doit être envoyé dans haut puis descendre
            if self.show_ball_up:
                self.sprites.append(TopBall(pygame.Rect(random.randint(10, RECT_WINDOW.width - SIZE_BALL), 0, SIZE_BALL, SIZE_BALL), self.window))
            else:
                self.sprites.append(BottomBall(pygame.Rect(random.randint(10, RECT_WINDOW.width - SIZE_BALL), RECT_WINDOW.height - 10, SIZE_BALL, SIZE_BALL), self.window))
            self.show_ball_up = not self.show_ball_up


        #Augmente la difficultée
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
                    sprite.move_up = not sprite.move_up
                    self.scores += 1


                #Si la class est une instance d'une ball qui part vers le haut
                if isinstance(sprite, TopBall):
                    #Détermine quand on perd pour la ball qui démarre en haut
                    if sprite.rect.y + sprite.rect.width >= RECT_WINDOW.height / 2:
                        self.sprites.remove(sprite)
                        self.scores = 0
                        self.difficulties = 1
                        self.show_ball_time = 1000

                        #-------------------
                        #      Game Over
                        #-------------------
                    else:
                        if sprite.move_up:
                            sprite.rect.y -= self.difficulties + 3
                        else:
                            sprite.rect.y += self.difficulties

                elif isinstance(sprite, BottomBall):
                    #Détermine quand on perd pour la ball qui démarre en bas
                    if sprite.rect.y <= RECT_WINDOW.height / 2:
                        self.sprites.remove(sprite)
                        self.scores = 0
                        self.difficulties = 1
                        self.show_ball_time = 1000

                        #-------------------
                        #      Game Over
                        #-------------------

                    else:
                        if sprite.move_up:
                            sprite.rect.y -= self.difficulties
                        else:
                            sprite.rect.y += self.difficulties + 3

                #Quand la barre sort de la fenêtre
                if not sprite.rect.colliderect(RECT_WINDOW):
                    #La ball sort de l'écran
                    self.sprites.remove(sprite)

        #Affiche le score
        self.window.blit(self.font_scores.render("{}".format(self.scores), 1, LABEL_SCORE_COLOR), (20, 20))






class Bar(Sprite):
    """
    Bar qui fait rebondir les balles
    """


    def update_sprite(self):
        pygame.draw.rect(self.window, BAR_COLOR, self.rect)


class Ball(Sprite):
    """
    Balles
    """

    def __init__(self, rect, window):
        Sprite.__init__(self, rect, window)

        self.ball_color = random.choice(BALL_COLORS)

        #Permet de savoir si la balle va en haut ou en bas
        self.move_up = False


    def update_sprite(self):
        pygame.draw.circle(self.window, self.ball_color, self.rect.center, int(self.rect.width / 2))



class TopBall(Ball):
    """
    Ball qui est envoyé dans haut
    """
    pass

class BottomBall(Ball):
    """
    Ball qui est envoyé dans bas
    """

    def __init__(self, rect, window):
        Ball.__init__(self, rect, window)
        self.move_up = True

class LineLimite(Sprite):
    """Class délimitant les 2 zones pour le niveau 2"""

    def update_sprite(self):
        pygame.draw.rect(self.window, LINE_COLOR, self.rect)

