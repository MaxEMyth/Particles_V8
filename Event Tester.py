import pygame
import pygame.locals as l
import pygame.event as e
from sys import exit
pygame.init
pygame.display.set_mode((500, 500))
while 1:
    for event in e.get():
        match event.type:
            case l.QUIT:
                exit()
            case l.MOUSEBUTTONDOWN:	print(event)
            case l.MOUSEWHEEL:		print(event)
            case l.KEYDOWN:			print(event)
            case l.KEYUP:			print(" ",event)
            case l.MOUSEBUTTONUP:	print(" ",event)
            case l.MOUSEMOTION:		pass
