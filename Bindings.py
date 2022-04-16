import pygame.locals as l


class MouseBinds:
    def __init__(self) -> None:
        self.lclick = 1
        self.rclick = 3
        self.mclick = 2
        self.wheelup = 1
        self.wheeldown = -1


class Binds:
    def __init__(self) -> None:
        self.up = l.K_w
        self.down = l.K_s
        self.left = l.K_a
        self.right = l.K_d
        self.pause = l.K_SPACE
        self.quit = l.K_ESCAPE
        self.binds = {
                self.up,
                self.down,
                self.left,
                self.right,
                self.pause,
                self.quit,
        }
        self.mouse = MouseBinds()


binds = Binds()
