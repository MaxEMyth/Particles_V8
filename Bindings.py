import pygame.locals
class Binds:
    def __init__(self,
                binding_dict=
                {
                    'up':       pygame.K_w,
                    'down':     pygame.K_s,
                    'left':     pygame.K_a,
                    'right':    pygame.K_d,
                    'pause':    pygame.K_SPACE,
                    'quit':     pygame.K_ESCAPE,
                    'm_click':  1
                }
                ) -> None:
        for bind in binding_dict:
            setattr(self, bind, binding_dict[bind])


