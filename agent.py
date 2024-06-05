from model import QModel
from display import display
import torch


class Agent():
    def __init__(self, map, pos = (0,0), num_steps=10) -> None:
        self.model = QModel()
        self.pos = pos
        self.num_steps = num_steps
        self.map = map
    
    def move_left(self):
        if self.pos[0] - 1 >= 0:
            self.pos = (self.pos[0] - 1, self.pos[1])
    
    def move_right(self):
        if self.pos[0] + 1 < self.map.shape[0]:
            self.pos = (self.pos[0] + 1, self.pos[1])
    
    def move_down(self):
        if self.pos[1] + 1 < self.map.shape[1]:
            self.pos = (self.pos[0], self.pos[1] + 1)
    
    def move_up(self):
        if self.pos[1] - 1 >= 0:
            self.pos = (self.pos[0], self.pos[1] - 1)
    
    def step(self, done=False):
        input_tensor = torch.tensor(self.pos, dtype=torch.float)
        output = self.model(input_tensor)
        previous_pos = self.pos
        action = None

        max = torch.max(output)

        if max == output[0]:
            self.move_up()
            action = 0
        elif max == output[1]:
            self.move_down()
            action = 1
        elif max == output[2]:
            self.move_right()
            action = 2
        elif max == output[3]:
            self.move_left()
            action = 3
        
        reward = self.map[self.pos[0], self.pos[1]]

        if self.pos != previous_pos:
            self.model.train_step(previous_pos, action, reward, self.pos, done)
        else:
            self.model.train_step(previous_pos, action, -5, self.pos, done)
        return reward
    
    def show(self, screen):
        display(screen, self.map, self.pos)



