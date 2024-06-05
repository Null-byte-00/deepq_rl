import torch
from torch import nn


class QModel(nn.Module):
    def __init__(self, state_dim=2, action_dim=4):
        super(QModel, self).__init__()
        self.stack = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
        )
        self.criterion = nn.MSELoss()
        self.optimizer = torch.optim.SGD(self.parameters(), lr=0.001)
        self.gamma = 0.5
    
    def forward(self, x):
        return self.stack(x)
    
    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        done = torch.tensor(done, dtype=torch.float)

        q_values = self.forward(state)
        q_value = q_values[action] # Q(s, a)

        next_q_value = self.forward(next_state)
        next_q_value = torch.max(next_q_value)  # max_a Q(s', a)
        target = reward + self.gamma * (1 - done) * next_q_value # r + gamma * max_a Q(s', a)

        loss = self.criterion(q_value, target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()
        
        
