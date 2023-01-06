import pygame
import math
from functions import kill
n = int(input("input n : "))
k = int(input("input k : "))
pygame.init()
screen = pygame.display.set_mode((800,800))
people = []
for i in range(n+1):
    people.append(pygame.image.load("small_spartan.png"))
# pygame.draw.circle(screen,(255,255,255), (360,360), 360)
for i in range(1):
    for j in range(n+1):
        screen.blit(people[j],(400 +260 * math.cos(2*math.pi/n*j + 2*math.pi/360*i), 400 +260 * math.sin(2*math.pi/n*j + 2*math.pi/360*i)))
        pygame.display.flip()
running = True
# screen.blit(people[1],(260 +60 * math.cos(2*math.pi/n*j + 2*math.pi/360*i), 260 +60 * math.sin(2*math.pi/n*j + 2*math.pi/360*i)))
# kill(screen, 0,n)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()