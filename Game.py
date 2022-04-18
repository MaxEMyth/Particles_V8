from math import sqrt
from numpy import mat
from pygame import *
from pygame.gfxdraw import textured_polygon
from pygame import locals as l

from Bindings import binds
from Setup import Setup
from Colors import *
init()

# TODO add a Show() class that lets me append values to show, accompanied with text, INSIDE the game screen.
# example: Show(frametime, "total frametime: ") will create the text, append it to the list of things to render, 
#           AND give it corresponding coordinates so as to not superpose other preceding text.
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
        self.screen = display.set_mode(self.settings.VIEWPORT_SIZE)
        self.background = image.load("Particles_V8\BG.png")
        self.scaled_background = self.background.copy()  # to be scaled later 
        self.game_field_rect = Rect((0,0), self.settings.GAME_FIELD_SIZE)
        self.text_size1 = font.Font(None, 40)
        self.text_size0 = font.Font(None, 20)
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
                    print(self.cam.size)
                    match recieved_event.y:  
                        # recieved_event.y value is 1 for wheelup, -1 for wheeldown
                        case binds.mouse.wheelup if self.running:
                            if self.cam.height > self.settings.zoom_limit.y:
                                self.cam.inflate_ip(-10, -10)
                            else:
                                self.cam.size = self.settings.zoom_limit
                        case binds.mouse.wheeldown if self.running:
                            if self.cam.height < self.settings.GAME_FIELD_SIZE.y:
                                self.cam.inflate_ip(10, 10)
                            # self.cam.inflate_ip(Vector2(10, 10))
                            else:
                                self.cam.size = self.settings.GAME_FIELD_SIZE
                case l.KEYDOWN:
                    # Update keystate:
                    self.keyboard.state[recieved_event.key] = True
                      
                    # For actions that execute once per keypress:
                    match recieved_event.key: 
                        case binds.pause:
                            self.running = not self.running
                            print("Unpaused" if self.running else "Paused")
                        case binds.quit:
                            exit()
                            # event.post(event.Event(l.QUIT))
                case l.KEYUP:  
                    # Remove no longer held keys from keyboard.state
                    self.keyboard.state[recieved_event.key] = False
                case l.WINDOWRESIZED | l.WINDOWSIZECHANGED:
                    pass  #self.settings.VIEWPORT_SIZE = math.Vector2(recieved_event.x, recieved_event.y) #! not compatible with fast-background-blit
                case l.VIDEORESIZE:
                    pass  # self.settings.GAME_FIELD_SIZE = math.Vector2(event.w, event.h)
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
                case l.WINDOWEXPOSED:
                    pass
                case _:
                    pass  # print("Uncaught Event: ", recieved_event)  # event.event_name(event.type))
            self.handle_held_keys()
        return (time.get_ticks() - start_time)
    
    def handle_held_keys(self) -> None:  # for continuous actions, checked every frame.
        """Used for handling events that require checking multiple keys at once \n
        (Which therefore use the keystate).
        """
        if self.running:
            direction = math.Vector2(
                    self.keyboard.state[binds.right] - self.keyboard.state[binds.left],   
                    self.keyboard.state[binds.down] - self.keyboard.state[binds.up]
            )
            # True - True == 0, True - False == 1, False - true == -1.
            if direction != Vector2():
                cam_view_scale = math.Vector2.magnitude(math.Vector2(self.cam.size)) / math.Vector2.magnitude(self.settings.VIEWPORT_SIZE)
                self.cam.vel = (self.cam.base_vel * cam_view_scale) * direction.normalize()
            else: 
                self.cam.vel = Vector2()
                # print("no velocity") 
            # print(f"corrected velocity = {self.cam.base_vel/self.cam.relative_size_fraction}    relative size = {self.cam.relative_size_fraction}")
        
    def show_background(self) -> int:
        """
        Scales the background image, then applies it to the screen (with corresponding corrections).
        
        Returns:
            int: Elapsed background transformation time in milliseconds (ms).
        """
        start_time = time.get_ticks()
        # if Vector2.magnitude(Vector2(self.cam.size)) <= Vector2.magnitude(self.settings.VIEWPORT_SIZE):
            
        cropped_background = self.background.subsurface(Rect(self.cam).clip(self.game_field_rect))
        # transform.scale(cropped_background, self.settings.VIEWPORT_SIZE, self.screen)
        cropped_background = transform.scale(cropped_background, self.settings.VIEWPORT_SIZE)
        self.screen.blit(cropped_background, (0,0))
        return (time.get_ticks() - start_time)
    def render_texts(self) -> None:
        frames_per_second = self.text_size1.render(
            f"FPS: {game.clock.get_fps():.1f}",
            False,
            BLACK)
        calc_time = self.text_size0.render(
            f"Calculation time (ms): {game.clock.get_rawtime()}",
            False,
            BLACK)
        game.screen.blits((
            (frames_per_second, (10, 0)),
            (calc_time, (10, 30)), 
            ))    

    class Camera(Rect):
        def __init__(self) -> None:
            Rect.__init__(self, (0, 0) , (500, 500))
            print("Initializing Camera")
            self.vel =Vector2()
            self.base_vel = 200
            self.zoom_factor = 1.1
            self.relative_size_fraction = 1
            self.cumulative_motion = Vector2()
            # self.minimum_size = game.settings.zoom_limit
        
        def constrain(self) -> None:
            self.clamp_ip(Rect(
                0,
                0,
                game.settings.GAME_FIELD_SIZE.x,
                game.settings.GAME_FIELD_SIZE.y
                # -self.width*0.5,
                # -self.height*0.5,
                # self.width  + display.get_window_size()[0] + self.width,
                # self.height + display.get_window_size()[1] + self.height
                # game.settings.GAME_FIELD_SIZE.x + 1.5*self.width,
                # game.settings.GAME_FIELD_SIZE.y + 1.5*self.height
                ))
        def update(self) -> None:
            # self.center = Vector2(self.topleft) + Vector2(self.size) * 0.5
            self.relative_size_fraction = sqrt(  # *how many times bigger than the camera the gamefield is*
                math.Vector2.magnitude_squared(game.settings.GAME_FIELD_SIZE)
                / math.Vector2.magnitude_squared(Vector2(self.size))
            )
            
        def move(self) -> None:
            motion = self.vel * game.clock.get_time()*0.001
            if abs(motion.x) > 1 or abs(motion.y) > 1:
                self.move_ip(self.cumulative_motion + motion)
                print(self.cumulative_motion + motion)
                self.cumulative_motion = Vector2()
            else:
                self.cumulative_motion += motion
                if abs(self.cumulative_motion.x) > 1 or abs(self.cumulative_motion.y) > 1:
                    self.move_ip(self.cumulative_motion)
                    self.cumulative_motion = Vector2()
            
            self.update()
            self.constrain()


game = Game()
