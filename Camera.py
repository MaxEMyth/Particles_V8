from numpy import mat
from pygame.math import Vector2 as Vec
class Camera:
    def __init__(self) -> None:
        self.pos = Vec(0,0)
        self.size = Vec(500,500)
        self.vel = Vec(0,0)
        self.max_vel = 150
        self.zoom_factor = 1.05