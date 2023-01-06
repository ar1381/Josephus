import pygame
import math
def kill(screen , j,n):
    i = 1
    pygame.draw.circle(screen,(255,0,0), (400 +260 * math.cos(2*math.pi/n*j + 2*math.pi/360*i), 400 +260 * math.sin(2*math.pi/n*j + 2*math.pi/360*i)), 10)
