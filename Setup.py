from pygame import Vector2
class Setup: 
    def __init__(self) -> None:
        self.VIEWPORT_SIZE   	= Vector2(1000, 1000) #! These values should be flipped!
        self.GAME_FIELD_SIZE 	= Vector2(500 , 500 ) #!
        self.FPS             	= 60 
        self.N               	= 12 
        self.COZINESS_FACTOR 	= 0.2  # max should be ~0.9
        self.WALL_FACTOR     	= 1 #.987,                # 0 - 0.985
        self.GRAVITY         	= 0                   # units - > px/s**2
        self.TOTAL_MOMENTUM  	= 500
