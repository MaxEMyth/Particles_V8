from pygame.math import Vector2 as Vec
from pygame import locals as l
from pygame import event as e
from pygame import key as k
from pygame import init
from Bindings import binds
from Setup import settings
init()
class Camera:
    def __init__(self) -> None:
        self.pos            = Vec(0,0)
        self.size           = Vec(500,500)
        self.vel            = Vec(0,0)
        self.max_vel        = 150
        self.zoom_factor    = 1.05
        self.keystate = dict()
        #* unnecesary: for bind in binds.binds: self.keystate[bind] = k.get_pressed()[bind] #create a MUTABLE copy of keystate 
        
    def constrain(self) -> None:
        self.center = self.pos + self.size/2
        if self.center.x    <= 0                             : self.pos.x = -0.5*self.size.x
        elif self.center.x  >= settings.GAME_FIELD_SIZE.x    : self.pos.x = -0.5*self.size.x + settings.GAME_FIELD_SIZE.x
        if self.center.y    <= 0                             : self.pos.y = -0.5*self.size.y
        elif self.center.y  >= settings.GAME_FIELD_SIZE.y    : self.pos.y = -0.5*self.size.y + settings.GAME_FIELD_SIZE.y
        
    def assess_inputs(self) -> None:
        for event in e.get():
            match event.type:
                case l.QUIT: exit()
                case l.MOUSEWHEEL:
                    match event.y: # value is 1 for wheelup, -1 for wheeldown
                        case binds.m_wheelup:pass
                        case binds.m_wheeldown:pass
                case l.KEYDOWN: 
                    self.keystate[event.key] = True
                    print(event.key, " set to True")
                    print(self.keystate)
                case l.KEYUP: 	
                    self.keystate[event.key] = False
                    print(event.key, " set to False")
                    print(self.keystate)
                case l.VIDEORESIZE:
                    settings.GAME_FIELD_SIZE = Vec(event.w, event.h) #print("resized to: ", settings.GAME_FIELD_SIZE)
                # case l.MOUSEBUTTONUP:  pass
                # case l.MOUSEBUTTONDOWN:pass
                # case l.MOUSEMOTION:    pass
                
                
                
cam = Camera()
settings.paused = True