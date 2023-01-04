import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800,800))
people = []

for i in range(4):
    people.append(pygame.image.load("small_spartan.png"))
pygame.draw.circle(screen,(255,255,255), (360,360), 360)
for i in range(4):
    for j in range(4):
        screen.blit(people[j],(360 +360 * math.cos(2*math.pi/4*j + 2*math.pi/360*i), 360 +360 * math.sin(2*math.pi/4*j + 2*math.pi/360*i)))
    pygame.display.flip()
    running = True
while running:
    for event in pygame.event.get():
        if event.type == quit:
            running = False
pygame.quit()