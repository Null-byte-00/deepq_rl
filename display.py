import pygame
import numpy as np


def display(screen, map,player, x_blocks = 10, y_blocks= 10):
    #pygame.init()
    #screen = pygame.display.set_mode((500,500))
    
    for i in range(x_blocks):
        for j in range(y_blocks):
            state = map[i][j]
            color = (255, 255, 255)
            pos = ((i+1) * 50 - 27, (j+1) * 50 - 27)
            
            if state > 1:
                color = (0, 255, 0)
            elif state < -1:
                color = (255, 0, 0)

            pygame.draw.rect(screen, color, pygame.Rect(i * 50 + 3, j * 50 + 3,
                                                              (screen.get_size()[0] * 0.8) / x_blocks  ,
                                                              (screen.get_size()[1] * 0.8) / y_blocks  ))

            if player[0] == i and player[1] == j:
                pygame.draw.circle(screen, (0, 0, 255), pos, 20)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500,500))

    map = np.full((10, 10), -1)
    map[2,2] = -5
    map[3,4] = 5

    loop = True
    while loop:
        display(screen, map, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False