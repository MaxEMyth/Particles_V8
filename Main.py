# import math
# import random
# from sys import exit
# import time

# import pygame as p  # TODO refactor imports ^_^
import pygame.draw as draw
import pygame.display as display
import pygame.font as f
import pygame.locals as l
# import pygame.event as e
# from pygame.math import Vector2 as Vec


from Game import game
from Colors import BLACK

# todo use dead time between frames to calculate next frame (unbind framerate from simulation accuracy)


# ?for calculation of cam movement in first 2 frames(?):
# game.clock.tick(game.settings.FPS)
# game.clock.tick(game.settings.FPS)
while 1:
    game.screen.fill(BLACK)
    input_time = game.handle_all_events()
    game.handle_held_keys()
    game.cam.move()
    game.show_background()
    display.flip()
    
    match game.settings.precise:
        case True:
            game.clock.tick_busy_loop(game.settings.FPS)
        case False:
            game.clock.tick	(game.settings.FPS)
