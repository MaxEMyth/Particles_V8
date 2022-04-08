from numpy import mat
from pygame.math import Vector2 as Vec
from pygame import locals as l
from pygame import event as e
from Bindings import binds
from Setup import settings
class Camera:
    def __init__(self) -> None:
        self.pos = Vec(0,0)
        self.size = Vec(500,500)
        self.vel = Vec(0,0)
        self.max_vel = 150
        self.zoom_factor = 1.05
    def constrain(self) -> None:
        self.center = self.pos + self.size/2
        if self.center.x <= 0:
            self.pos.x = -0.5*self.size.x
        elif self.center.x >= settings.GAME_FIELD_SIZE.x:
            self.pos.x = -0.5*self.size.x + settings.GAME_FIELD_SIZE.x
        if self.center.y <= 0:
            self.pos.y = -0.5*self.size.y
        elif self.center.y >= settings.GAME_FIELD_SIZE.y:
            self.pos.y = -0.5*self.size.y + settings.GAME_FIELD_SIZE.y
    def assess_inputs(self) -> None:
        for event in e.get():
            match event.type:
                case l.QUIT:
                    exit()
                case l.MOUSEWHEEL:
                    match event.y:
                        case binds.m_wheelup:
                            pass
                        case binds.m_wheeldown:
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
                
                
                
cam = Camera()