import pygame as pg
import pymunk as pm
from pygame.color import *
from pygame.locals import *
from pymunk import Vec2d
from pymunk.pygame_util import DrawOptions


""" 
I'm using SO_Circles as an example on how to integrate physics into my pygame sprites.
"""

dim = (600,600)

win = pg.display.set_mode(dim)
pg.display.caption("Pymunk Test")
options = DrawOptions(win)

def flipy(p):
	""" Change chipmunk physics to pg coordinates """
	return Vec2d((p[0], -p[1]+dim[0]))


class Entity(pg.sprite.Sprite):
	def __init__(self, pos, space, mass=1):
		super().__init__()

		# pygame stuff

		self.orig_image = pg.image.load('data/adventurer-run3-00.png')
		self.image = self.orig_image
		self.rect = self.image.get_rect(topleft=pos)
		vs = 

		# pymunk stuff

		moment = pm.moment_for_box(mass, self.rect.size)
		self.body = pm.Body(mass, moment)
		self.shape = pm.Poly(self.body)

	def update(self):
		pass


class Game:
	def __init__(self):
		pass

	def run(self):
		pass

	def handle_events(self):
		pass
	
	def run_logic(self):
		pass

	def draw(self):
		pass
		
space = pm.Space()
space.gravity = 0, -900

