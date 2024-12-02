import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600 

display_surface= pygame.display.set_mode((WIDTH,HEIGHT))

bg = pygame.image.load('bg.jpg')
car = pygame.image.load("spaceship.png")

bg_2 = pygame.transform.scale(bg,(WIDTH,HEIGHT))
car= pygame.transform.scale(car,(150,150))

car_x = 100
car_y = 10


keys = [False,False,False,False]


while car_y < 500 :
    display_surface.blit(bg_2,(0,0))
    display_surface.blit(car,(car_x,car_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0]=True
            if event.key == pygame.K_DOWN:
                keys[2]=True
            if event.key == pygame.K_LEFT:
                keys[1]=True 
            if event.key == pygame.K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0]=False
            if event.key == pygame.K_DOWN:
                keys[2]=False
            if event.key == pygame.K_LEFT:
                keys[1]=False
            if event.key == pygame.K_RIGHT:
                keys[3]=False
    if keys[0]:
        if car_y>0:
            car_y -= 7
    if keys[1]:
        if car_x>0 :
            car_x -=3
    if keys[2]:
        if car_y< 499:
            car_y += 3 
    if keys [3]:
        if car_x < 499:
            car_x +=3
    car_y += 5
    time.sleep(0.05)

print('game over')