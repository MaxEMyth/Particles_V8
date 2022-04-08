#import math
#import random
from sys import exit
#import time

#import pygame as p  # TODO refactor imports ^_^
import pygame.draw as draw
import pygame.display as display
import pygame.font as f
import pygame.time as t
import pygame.locals as l
#import pygame.event as e
from pygame.math import Vector2 as Vec


import Colors
from Camera import cam
from Bindings import binds
from Setup import settings
#todo use Vec.project() and reflect() for collisions

my_clock = t.Clock()


screen = display.set_mode(settings.GAME_FIELD_SIZE, l.RESIZABLE)                

while 1:
    cam.assess_inputs()
    display.flip()
    my_clock.tick_busy_loop(settings.FPS)

