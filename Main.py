#import math
#import random
from sys import exit
#import time

import pygame as p  # TODO refactor imports ^_^
import pygame.draw as draw
import pygame.display as display
import pygame.font as f
import pygame.time as t
import pygame.locals as l
import pygame.event as e
from pygame.math import Vector2 as Vec

import Colors
from Camera import Camera
from Bindings import Binds
from Setup import Setup
#todo use Vec.project() and reflect() for collisions
binds = Binds()
my_clock = t.Clock()
settings = Setup()

class Camera(Camera):
    def constrain(self):
        self.center = self.pos + self.size/2
        if self.center.x <= 0:
            self.pos.x = -0.5*self.size.x
        elif self.center.x >= settings.GAME_FIELD_SIZE.x:
            self.pos.x = -0.5*self.size.x + settings.GAME_FIELD_SIZE.x
        if self.center.y <= 0:
            self.pos.y = -0.5*self.size.y
        elif self.center.y >= settings.GAME_FIELD_SIZE.y:
            self.pos.y = -0.5*self.size.y + settings.GAME_FIELD_SIZE.y
    def assess_inputs(self):
        for event in e.get():
            match event.type:
                case l.QUIT:
                    exit()
                case l.MOUSEWHEEL:
                    match event.y:
                        case 1:
                            pass
                        case -1:
                            pass
                case l.KEYDOWN:
                    match event.key:
                        case binds.quit: exit()
                        case binds.pause:
                            paused = not paused
                            if paused: print("Paused")
                            else: print("Unpaused")
                        case binds.up:pass
                        case binds.down:pass
                        case binds.left:pass
                        case binds.right:pass
                case l.VIDEORESIZE: 
                    settings.GAME_FIELD_SIZE = Vec(event.w, event.h)
                    print("resized to: ", settings.GAME_FIELD_SIZE)
                # case l.KEYUP #if _listening_:  pass
                # case l.MOUSEBUTTONUP:  pass
                # case l.MOUSEBUTTONDOWN:pass
                # case l.MOUSEMOTION:    pass
screen = display.set_mode(settings.GAME_FIELD_SIZE, l.RESIZABLE)                
cam = Camera()
while 1:
    cam.assess_inputs()
    display.flip()
    my_clock.tick_busy_loop(settings.FPS)
