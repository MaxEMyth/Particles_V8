from numpy import mat
from pygame.math import Vector2 as Vec
from Setup import Setup
settings = Setup()
class Camera:
    def __init__(self) -> None:
        self.pos = Vec(0,0)
        self.size = Vec(500,500)
        self.vel = Vec(0,0)
        self.max_vel = 150
        self.zoom_factor = 1.05
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
