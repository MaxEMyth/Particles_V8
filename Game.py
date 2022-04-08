from pygame.math import Vector2 as Vec
from pygame import locals as l
from pygame import event as e
#from pygame import key as k
from pygame import init
from Bindings import binds
from Setup import Setup
init()

class Keystate:
    def __init__(self) -> None:
        self.state = dict()
        for bind in binds.binds: self.state[bind] = False
class Camera: pass
class Game:
    def __init__(self) -> None:
        self.keyboard = Keystate()
        self.cam = Camera()
        self.settings = Setup()
        
    def handle_all_events(self) -> None:
        for event in e.get():
            match event.type:
                case l.QUIT: exit()
                case l.MOUSEWHEEL:
                    match event.y: # value is 1 for wheelup, -1 for wheeldown
                        case binds.m_wheelup:pass
                        case binds.m_wheeldown:pass
                case l.KEYDOWN: 
                    self.keyboard.state[event.key] = True
                case l.KEYUP:
                    self.keyboard.state[event.key] = False
                case l.VIDEORESIZE:
                    self.settings.GAME_FIELD_SIZE = Vec(event.w, event.h) 
                case l.WINDOWRESIZED | l.WINDOWSIZECHANGED:
                    self.settings.GAME_FIELD_SIZE = Vec(event.x, event.y)
                case l.MOUSEBUTTONUP:
                    pass
                case l.MOUSEBUTTONDOWN:
                    pass
                case l.MOUSEMOTION:
                    pass
                case l.WINDOWFOCUSLOST | l.WINDOWMINIMIZED:
                    self.settings.paused = True
                case l.WINDOWEXPOSED | l.WINDOWENTER | l.WINDOWLEAVE | l.WINDOWMOVED:
                    pass
                case l.TEXTINPUT:
                    pass
                case _: print("Uncaught Event: ", e.event_name(event.type))


class Camera:
    def __init__(self) -> None:
        self.pos,self.vel   = Vec(0,0)
        self.size           = Vec(500,500)
        self.max_vel        = 150
        self.zoom_factor    = 1.05
        
    def constrain(self) -> None:
        self.center = self.pos + self.size/2
        if self.center.x    <= 0                             : self.pos.x = -0.5*self.size.x
        elif self.center.x  >= game.settings.GAME_FIELD_SIZE.x    : self.pos.x = -0.5*self.size.x + game.settings.GAME_FIELD_SIZE.x
        if self.center.y    <= 0                             : self.pos.y = -0.5*self.size.y
        elif self.center.y  >= game.settings.GAME_FIELD_SIZE.y    : self.pos.y = -0.5*self.size.y + game.settings.GAME_FIELD_SIZE.y
    
game = Game()