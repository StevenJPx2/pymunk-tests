import pygame
import pymunk
from pygame.color import *
from pygame.locals import *
from pymunk import Vec2d
from pymunk.pygame_util import DrawOptions


dim = (600,600)

win = pygame.display.set_mode(dim)
pygame.display.caption("Pymunk Test")
options = DrawOptions(win)

def flipy(p):
	""" Change chipmunk physics to pygame coordinates """
	return Vec2d((p[0], -p[1]+dim[0]))


class Enitity(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		

	def draw(self):
		pass

	def update(self):
		pass


space = pymunk.Space()
space.gravity = 0, -900

