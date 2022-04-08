from pygame import Vector2
class Setup: 
    def __init__(self, 
                VIEWPORT_SIZE      = Vector2(1000, 1000), 
                GAME_FIELD_SIZE    = Vector2(500 , 500 ), 
                FPS                = 60, 
                N                  = 12, 
                COZINESS_FACTOR    = 0.2,  # max should be ~0.9
                WALL_FACTOR        = 1, #.987,                # 0 - 0.985
                GRAVITY            = 0,                   # units - > px/s**2
                TOTAL_MOMENTUM     = 500) -> None:
        
        self.VIEWPORT_SIZE   = VIEWPORT_SIZE
        self.GAME_FIELD_SIZE = GAME_FIELD_SIZE
        self.FPS             = FPS
        self.N               = N
        self.COZINESS_FACTOR = COZINESS_FACTOR
        self.WALL_FACTOR     = WALL_FACTOR
        self.GRAVITY         = GRAVITY
        self.TOTAL_MOMENTUM  = TOTAL_MOMENTUM 