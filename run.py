import pygame
import math
from functions import kill
import time

n = int(input("input n : "))
k = int(input("input k : "))

pygame.init()
screen = pygame.display.set_mode((800,800))
# pygame.draw.rect(screen, (100,200,150), pygame.Rect(0,0,800,800))
pygame.display.flip()
i = 1
for j in range(n + 1):
    pygame.draw.circle(screen, (0,255,0) , (400 +260 * math.cos(2*math.pi/n*j + 2*math.pi/360*i), 400 +260 * math.sin(2*math.pi/n*j + 2*math.pi/360*i)), 20)


# font = font.ren
# from functions import kill

active = True

def josephus(people, skip, screen, n):
    people_list = list(range(1, people + 1))
    index = skip - 1
    while len(people_list) > 1:
        o = people_list.pop(index)
        print("Person %d is killed" % o)
        print(str(o)+"\n")
        kill(screen,o-1,n)
        pygame.display.flip()
        time.sleep(3)
        index = (index + skip - 1) % len(people_list)
    print("The last survivor is Person %d" % people_list[0])
    active = False
    pygame.quit()
    quit()
 
# kill(screen,0,n)
# kill(screen,2,n)
# kill(screen,4,n)
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    josephus(n, k, screen, n)
    
    pygame.display.update()