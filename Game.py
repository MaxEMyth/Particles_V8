from pygame import time as t
from pygame import image as i
from pygame import display as d
from pygame import event as e
from pygame import init
from pygame import locals as l
from pygame.math import Vector2 as Vec

from Bindings import binds
from Setup import Setup

init()


class Game:
    class Keyboard:
        def __init__(self) -> None:
            self.state = dict()
            for bind in binds.binds:
                self.state[bind] = False

        def handle_held_keys(self) -> None:  # for continuous actions, checked every frame.
            direction = (self.keyboard.state[binds.left],
                         self.keyboard.state[binds.right],
                         self.keyboard.state[binds.up],
                         self.keyboard.state[binds.down])
            self.cam.vel = Vec(
                    self.keyboard.state[binds.right] - self.keyboard.state[binds.left],
                    self.keyboard.state[binds.down] - self.keyboard.state[binds.up]
            )

    def __init__(self) -> None:
        self.keyboard = self.Keyboard()
        self.cam = self.Camera()
        self.settings = Setup()
        self.clock = t.Clock()
        self.screen = d.set_mode(self.settings.GAME_FIELD_SIZE, l.RESIZABLE)
        self.background = i.load("BG.png")
        # self.background = i.load("Particles_V8\BG.png")
        self.running = True
    
    def handle_all_events(self) -> None:
        for event in e.get():
            match event.type:
                case l.QUIT:
                    exit()
                case l.MOUSEWHEEL:
                    match event.y:  # value is 1 for wheelup, -1 for wheeldown
                        case binds.mouse.wheelup if self.running:
                            self.cam.pos += self.cam.size * 0.5 * (1. - self.cam.zoom_factor)  # center zooming action
                            self.cam.size *= self.cam.zoom_factor  # ? zoom camera out (?)
                        case binds.mouse.wheeldown if self.running:
                            self.cam.pos += self.cam.size * 0.5 * (
                                    1. - (self.cam.zoom_factor**-1))  # center zooming action
                            self.cam.size /= self.cam.zoom_factor  # ? zoom camera in (?)
                case l.KEYDOWN:
                    self.keyboard.state[event.key] = True  # update keystate
                    match event.key:  # for actions that execute once per keypress
                        case binds.pause:
                            self.running = not self.running
                            print("Unpaused" if self.running else "Paused")
                        case binds.quit:
                            quit()
                
                case l.KEYUP:
                    self.keyboard.state[event.key] = False
                case l.VIDEORESIZE:
                    pass  # self.settings.GAME_FIELD_SIZE = Vec(event.w, event.h)
                case l.WINDOWRESIZED | l.WINDOWSIZECHANGED:
                    self.settings.GAME_FIELD_SIZE = Vec(event.x, event.y)
                case l.MOUSEBUTTONDOWN:
                    pass
                case l.MOUSEBUTTONUP:
                    pass
                case l.MOUSEMOTION:
                    pass
                case l.WINDOWFOCUSLOST | l.WINDOWMINIMIZED:
                    self.running = False
                case l.WINDOWEXPOSED | l.WINDOWENTER | l.WINDOWLEAVE | l.WINDOWMOVED:
                    pass
                case l.TEXTINPUT:
                    pass  # TODO add command console (revealed to me in a dream)
                case l.ACTIVEEVENT:
                    pass
                case _:
                    print("Uncaught Event: ", event)  # e.event_name(event.type))
    
    
    class Camera:
        def __init__(self) -> None:
            self.pos, self.vel = Vec(0, 0), Vec(0, 0)
            self.size = Vec(500, 500)
            self.center = self.pos + self.size * 0.5
            self.max_vel = 150
            self.zoom_factor = 1.05
        
        def constrain(self) -> None:
            self.center = self.pos + self.size * 0.5
            if self.center.x <= 0:
                self.pos.x = -0.5 * self.size.x
            elif self.center.x >= game.settings.GAME_FIELD_SIZE.x:
                self.pos.x = -0.5 * self.size.x + game.settings.GAME_FIELD_SIZE.x
            if self.center.y <= 0:
                self.pos.y = -0.5 * self.size.y
            elif self.center.y >= game.settings.GAME_FIELD_SIZE.y:
                self.pos.y = -0.5 * self.size.y + game.settings.GAME_FIELD_SIZE.y
        
        def move(self) -> None:
            self.pos += self.vel * game.clock.get_time() * 0.001
            self.constrain()


game = Game()
