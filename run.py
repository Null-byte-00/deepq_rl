import pygame
from agent import Agent
import numpy as np
import random
from matplotlib import pyplot as plt


NUM_RUNS = 30
NUM_STEPS = 10
INITIAL_POS = (5,6)

train_map = np.full((10, 10), -1)

for i in range(10):
    for j in range(10):
        if i % 2 == j % 2:
            if i % 2 == 1:
                if bool(random.getrandbits(1)):
                    train_map[i][j] = 5
            else:
                if bool(random.getrandbits(1)):
                    train_map[i][j] = -5


agent = Agent(train_map, pos=INITIAL_POS)

pygame.init()
screen = pygame.display.set_mode((500, 500))

loop = True
rewards = []
reward = 0
for step in range(NUM_RUNS * NUM_STEPS):
    agent.show(screen)
    pygame.display.update()
    reward += agent.step()

    if step % NUM_STEPS == 0:
        print(f"step: {step % NUM_STEPS} reward: {reward}")
        rewards.append(reward)
        reward = 0
        agent.pos = INITIAL_POS
    pygame.time.wait(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

plt.plot(rewards)
plt.show()