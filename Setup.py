from pygame import Vector2


class Setup:
    def __init__(self) -> None:
        self.VIEWPORT_SIZE = Vector2(500, 500)
        self.GAME_FIELD_SIZE = Vector2(1000, 1000)
        self.FPS = 60
        self.N = 12
        self.WALL_FACTOR = 1  # .987,                # 0 - 0.985
        self.GRAVITY = 0  # units - > px/s**2
        self.precise = False
        self.zoom_limit = Vector2(10,10)
