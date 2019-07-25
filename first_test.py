import pygame
import pymunk
from pygame.color import *
from pygame.locals import *
from pymunk import Vec2d
from pymunk.pygame_util import DrawOptions

win = pygame.display.set_mode((600,600))
pygame.display.caption("Pymunk Test")
options = DrawOptions(win)

space = pymunk.Space()
space.gravity = 0, -900


