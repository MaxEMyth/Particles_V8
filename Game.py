from math import sqrt
from pygame import *
from pygame.gfxdraw import textured_polygon
from pygame import locals as l

from Bindings import binds
from Setup import Setup

init()


class Game:
    class Keyboard:
        def __init__(self) -> None:
            print("Initializing Keyboard")
            self.state = dict()
            for bind in binds.binds:
                self.state[bind] = False
    class Camera:
        pass

    def __init__(self) -> None:
        print("Initializing Game")
        self.keyboard = self.Keyboard()
        self.settings = Setup()
        self.cam = self.Camera()
        self.clock = time.Clock()
        self.screen = display.set_mode(self.settings.VIEWPORT_SIZE, l.RESIZABLE )
        self.background = image.load("Particles_V8\BG.png")
        self.scaled_background = self.background.copy()  # to be scaled later 
        self.running = True
    
    def handle_all_events(self) -> int:
        """
        Sorts through all events in the queue and handles their respective actions.

        Returns:
            int: Elapsed input-processing time in milliseconds (ms).
        """
        start_time = time.get_ticks()
        for recieved_event in event.get():
            match recieved_event.type:
                case l.QUIT:
                    exit()
                case l.MOUSEWHEEL:
                    match recieved_event.y:  
                        # recieved_event.y value is 1 for wheelup, -1 for wheeldown
                        case binds.mouse.wheelup if self.running:
                            # self.cam.inflate_ip(Vector2(-100, -100)/self.cam.relative_size_fraction)
                            self.cam.inflate_ip(Vector2(-10, -10))
                            print("Zoom in")
                        case binds.mouse.wheeldown if self.running:
                            # self.cam.inflate_ip(Vector2(100, 100)/self.cam.relative_size_fraction)
                            self.cam.inflate_ip(Vector2(10, 10))
                            print("Zoom out")
                case l.KEYDOWN:
                    # Update keystate:
                    self.keyboard.state[recieved_event.key] = True
                      
                    # For actions that execute once per keypress:
                    match recieved_event.key: 
                        case binds.pause:
                            self.running = not self.running
                            print("Unpaused" if self.running else "Paused")
                        case binds.quit:
                            quit()
                case l.KEYUP:  
                    # Remove no longer held keys from keyboard.state
                    self.keyboard.state[recieved_event.key] = False
                case l.WINDOWRESIZED | l.WINDOWSIZECHANGED:
                    self.settings.GAME_FIELD_SIZE = math.Vector2(recieved_event.x, recieved_event.y)
                # case l.VIDEORESIZE:
                #     pass  # self.settings.GAME_FIELD_SIZE = math.Vector2(event.w, event.h)
                # case l.MOUSEBUTTONDOWN:
                #     pass
                # case l.MOUSEBUTTONUP:
                #     pass
                # case l.MOUSEMOTION:
                #     pass
                # case l.WINDOWFOCUSLOST | l.WINDOWMINIMIZED:
                #     self.running = False
                # case l.WINDOWEXPOSED | l.WINDOWENTER | l.WINDOWLEAVE | l.WINDOWMOVED:
                #     pass
                # case l.TEXTINPUT:
                #     pass  # TODO add command console (revealed to me in a dream)
                # case l.ACTIVEEVENT:
                #     pass
                # case l.WINDOWEXPOSED:
                #     pass
                # case _:
                    print("Uncaught Event: ", recieved_event)  # event.event_name(event.type))
        return (time.get_ticks() - start_time)
    
    def handle_held_keys(self) -> None:  # for continuous actions, checked every frame.
        self.cam.vel = self.cam.max_vel * math.Vector2(
                self.keyboard.state[binds.right] - self.keyboard.state[binds.left],
                self.keyboard.state[binds.down] - self.keyboard.state[binds.up]
        )
    def show_background(self) -> int:
        """
        Scales the background image, then applies it to the screen (with corresponding corrections).
        
        Returns:
            int: Elapsed background transformation time in milliseconds (ms).
        """
        start_time = time.get_ticks()
        game_field_rect = Rect((0,0), self.settings.GAME_FIELD_SIZE)
        if Vector2.magnitude(Vector2(self.cam.size)) <= Vector2.magnitude(self.settings.VIEWPORT_SIZE):
            
            cropped_background = self.background.subsurface(Rect(self.cam).clip(game_field_rect))
            transform.scale(cropped_background, self.settings.VIEWPORT_SIZE, self.screen)
            
        return (time.get_ticks() - start_time)
    
    class Camera(Rect):
        def __init__(self) -> None:
            Rect.__init__(self, (0, 0) , (500, 500))
            print("Initializing Camera")
            self.vel =Vector2(0, 0)
            self.max_vel = 150
            self.zoom_factor = 1.1
            self.relative_size_fraction = 1.
        
        def constrain(self) -> None:
            self.clamp_ip(Rect(
                -self.width,
                -self.height,
                display.get_window_size()[0] + 2*self.width,
                display.get_window_size()[1] + 2*self.height
                # game.settings.VIEWPORT_SIZE.x + 2*self.width,
                # game.settings.VIEWPORT_SIZE.y + 2*self.height
                ))
        def update(self) -> None:
            # self.center = Vector2(self.topleft) + Vector2(self.size) * 0.5
            self.relative_size_fraction = sqrt(
                math.Vector2.magnitude_squared(game.settings.GAME_FIELD_SIZE)
                / math.Vector2.magnitude_squared(Vector2(self.size))
            )
            
        def move(self) -> None:
            self.move_ip(self.vel * game.clock.get_time() * 0.001)
            self.update()
            self.constrain()


game = Game()
