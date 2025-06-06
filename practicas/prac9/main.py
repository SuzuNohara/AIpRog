import random
import time
import os

class LogicAgent:
    def __init__(self, n=5, m=5):
        self.position = (0, 0)
        self.memory = [['' for _ in range(m)] for _ in range(n)]
        self.has_gold = False
        self.is_alive = True

    def perceive(self, world):
        perceptions = world.get_perceptions(self.position)
        return perceptions

    def get_position(self):
        return self.position

    def mark_safe(self, x, y):
        self.save_memory("s")

    def evaluate(self, a, b):
        x, y = self.position

    def print_memory(self):
        for row in self.memory:
            print(' '.join(cell if cell else '.' for cell in row))

    def move(self, direction, world):
        x, y = self.position
        if direction == 'up' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'down' and x < len(world) - 1:
            self.position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.position = (x, y - 1)
        elif direction == 'right' and y < len(world[0]) - 1:
            self.position = (x, y + 1)
        else:
            print("Invalid move")

    def save_memory(self, value):
        x, y = self.position
        if 0 <= x < len(self.memory) and 0 <= y < len(self.memory[0]):
            for v in value if isinstance(value, list) else [value]:
                if v not in self.memory[x][y]:
                    self.memory[x][y] += v

class WampusWorld:
    def __init__(self, n=5, m=5, use_default=True):
        self.n = n
        self.m = m
        if use_default:
            self.grid = self.create_default_world()
        else:
            self.grid = self.create_world(n, m)

    def create_default_world(self):
        return [
            [[0,0,0,0,0], [0,0,0,0,0], [1,0,0,0,0], [0,0,0,0,0], [0,0,1,0,0]],
            [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
            [[0,0,0,0,0], [0,0,0,0,1], [0,0,0,0,1], [0,0,0,0,0], [0,0,0,0,0]],
            [[0,0,0,0,1], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
            [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,1], [0,0,0,0,0]],
        ]

    def create_world(self, n, m):
        import random
        world = [[[0, 0, 0, 0, 0] for _ in range(m)] for _ in range(n)]
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m
        # Place Wampus
        while True:
            wx, wy = random.randint(0, n-1), random.randint(0, m-1)
            if (wx, wy) != (0, 0):
                world[wx][wy][0] = 1
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = wx+dx, wy+dy
                    if is_valid(nx, ny):
                        world[nx][ny][1] = 1
                break
        # Place Gold
        while True:
            gx, gy = random.randint(0, n-1), random.randint(0, m-1)
            if (gx, gy) not in [(0, 0), (wx, wy)]:
                world[gx][gy][2] = 1
                break
        # Place Pits
        pits = n - 1
        while pits > 0:
            px, py = random.randint(0, n-1), random.randint(0, m-1)
            if (px, py) not in [(0,0), (wx,wy), (gx,gy)] and world[px][py][4] == 0:
                world[px][py][4] = 1
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = px+dx, py+dy
                    if is_valid(nx, ny):
                        world[nx][ny][3] = 1
                pits -= 1
        return world

    def print_world(self, agent_pos):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if (i, j) == agent_pos:
                    print('A', end=' ')
                elif cell[2] == 1:
                    print('G', end=' ')
                elif cell[0] == 1:
                    print('W', end=' ')
                elif cell[4] == 1:
                    print('P', end=' ')
                else:
                    print('.', end=' ')
            print()

    def print_wind_odor(self):
        for row in self.grid:
            for cell in row:
                has_wind = cell[3] == 1
                has_odor = cell[1] == 1
                if has_wind and has_odor:
                    print('WO', end=' ')
                elif has_wind:
                    print('W ', end=' ')
                elif has_odor:
                    print('O ', end=' ')
                else:
                    print('. ', end=' ')
            print()

    def get_perceptions(self, position):
        x, y = position
        cell = self.grid[x][y]
        perceptions = []
        if cell[0]: perceptions.append('w')
        if cell[1]: perceptions.append('o')
        if cell[2]: perceptions.append('g')
        if cell[3]: perceptions.append('w')
        if cell[4]: perceptions.append('p')
        return perceptions

def explore(agent, world):
    while agent.is_alive and not agent.has_gold:
        os.system('clear')
        perceptions = agent.perceive(world)
        agent.save_memory(perceptions)
        print(f"Senses: {perceptions}")
        print("______________________________")
        world.print_world(agent.get_position())
        print("______________________________")
        agent.print_memory()
        if 'g' in perceptions:
            agent.has_gold = True
            print("Agent victory! Gold found.")
            break
        elif 'p' in perceptions or 'w' in perceptions:
            agent.is_alive = False
            print("Agent death! Fell into a pit or met the Wampus.")
            break
        else:
            x, y = agent.get_position()
            agent.mark_safe(x, y)
            n, m = len(world.grid), len(world.grid[0])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            accessible_positions = []
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    accessible_positions.append((nx, ny))
            print(f"Accessible positions: {accessible_positions}")
        time.sleep(1)
        break

def main():
    n, m = 5, 5
    world = WampusWorld(n, m, use_default=True)
    agent = LogicAgent()
    explore(agent, world)

if __name__ == "__main__":
    main()