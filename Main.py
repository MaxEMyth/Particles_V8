# import math
# import random
# from sys import exit
# import time

# import pygame as p  # TODO refactor imports ^_^
from pygame import Color

import pygame.display as display
import pygame.font as f
# import pygame.locals as l
# import pygame.event as e
# from pygame.math import Vector2 as Vec


from Game import game
from Colors import BLACK

# todo use dead time between frames to calculate next frame (unbind framerate from simulation accuracy)


# ?for calculation of cam movement in first 2 frames(?):
# game.clock.tick(game.settings.FPS)
# game.clock.tick(game.settings.FPS)
f.init()


while 1:
    # game.screen.fill(BLACK)
    input_time = game.handle_all_events()
    
    if game.running:
        game.cam.move()
        background_time = game.show_background()
    else:
        game.screen.fill(BLACK)
    game.render_texts()
    display.flip()
    # print(f"inputs time: {input_time}")
    print(f"Bckgrnd time: {background_time}")
    # print(pygame.display.Info())
    
    if game.settings.precise:   game.clock.tick_busy_loop(game.settings.FPS)
    else:                       game.clock.tick(game.settings.FPS)
