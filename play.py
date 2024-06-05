import pygame
from agent import Agent
import numpy as np


train_map = np.full((10, 10), -1)
train_map[4,4] = -5
train_map[5,9] = -5
train_map[3, 8] = 5
train_map[6, 9] = 5

agent = Agent(train_map, pos=(3,4))

pygame.init()
screen = pygame.display.set_mode((500, 500))

loop = True
while loop:
    agent.show(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                agent.move_up()
            if event.key == pygame.K_DOWN:
                agent.move_down()
            if event.key == pygame.K_RIGHT:
                agent.move_right()
            if event.key == pygame.K_LEFT:
                agent.move_left()