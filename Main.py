#import math
#import random
#from sys import exit
#import time

#import pygame as p  # TODO refactor imports ^_^
import pygame.draw as draw
import pygame.display as display
import pygame.font as f
import pygame.time as t
import pygame.locals as l
#import pygame.event as e
#from pygame.math import Vector2 as Vec


import Colors
from Game import game
#todo use dead time between frames to calculate next frame (unbind framerate from simulation accuracy)
my_clock = t.Clock()


screen = display.set_mode(game.settings.GAME_FIELD_SIZE, l.RESIZABLE)                

while 1:
    game.cam.handle_all_events()
    display.flip()
    my_clock.tick_busy_loop(game.settings.FPS)

