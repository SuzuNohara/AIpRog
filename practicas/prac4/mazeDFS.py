import random
import time
import os

class Micromouse:
    def __init__(self):
        self.memory = []
        self.position = (0, 0)

    def move_left(self):
        self.memory.append('l')

    def move_right(self):
        self.memory.append('r')

    def move_up(self):
        self.memory.append('u')

    def move_down(self):
        self.memory.append('d')

    def pop_last_action(self):
        if self.memory:
            return self.memory.pop()
        return None

    def get_last_action(self):
        if self.memory:
            return self.memory[-1]
        return None

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def check_left(self, maze):
        x, y = self.position
        return y > 0 and maze[x][y - 1] == 1 and self.get_last_action() != 'r'

    def check_right(self, maze):
        x, y = self.position
        return y < len(maze[0]) - 1 and maze[x][y + 1] == 1 and self.get_last_action() != 'l'

    def check_up(self, maze):
        x, y = self.position
        return x > 0 and maze[x - 1][y] == 1 and self.get_last_action() != 'd'

    def check_down(self, maze):
        x, y = self.position
        return x < len(maze) - 1 and maze[x + 1][y] == 1 and self.get_last_action() != 'u'

def genMaze(n, m):
    def init_maze(n, m):
        return [[0 for _ in range(m * 2)] for _ in range(n * 2)]

    def carve_passages_from(cx, cy, maze, n, m):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for (dx, dy) in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n * 2 and 0 <= ny < m * 2 and maze[nx][ny] == 0:
                if sum(1 for (ddx, ddy) in directions if 0 <= nx + ddx < n * 2 and 0 <= ny + ddy < m * 2 and maze[nx + ddx][ny + ddy] == 1) < 2:
                    maze[cx][cy] = 1
                    maze[nx][ny] = 1
                    maze[cx + dx // 2][cy + dy // 2] = 1
                    carve_passages_from(nx, ny, maze, n, m)

    maze = init_maze(n, m)
    carve_passages_from(0, 0, maze, n, m)
    maze[0][0] = 1  # Start
    maze[n * 2 - 2][m * 2 - 2] = 1  # End
    maze[n * 2 - 2][m * 2 - 3] = 1
    maze[n * 2 - 3][m * 2 - 2] = 1
    maze[n * 2 - 3][m * 2 - 3] = 0
    return maze

def print_maze(maze, mouse):
    start_color = '\033[91m'  # Red
    end_color = '\033[92m'    # Green
    mouse_color = '\033[95m'  # Purple
    reset_color = '\033[0m'   # Reset
    os.system("clear")

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if i == 0 and j == 0:
                print(f'{start_color}\u2588\u2588{reset_color}', end='')
            elif i == len(maze) - 2 and j == len(row) - 2:
                print(f'{end_color}\u2588\u2588{reset_color}', end='')
            elif (i, j) == mouse.get_position():
                print(f'{mouse_color}\u2588\u2588{reset_color}', end='')
            else:
                print('  ' if cell == 1 else '\u2588\u2588', end='')
        print()

def solve_maze(maze, mouse):
    if mouse.get_position() == (len(maze) - 2, len(maze[0]) - 2):
        return True
    else:
        left = mouse.check_left(maze)
        right = mouse.check_right(maze)
        up = mouse.check_up(maze)
        down = mouse.check_down(maze)
        if left:
            mouse.move_left()
            mouse.set_position((mouse.get_position()[0], mouse.get_position()[1] - 1))
            print_maze(maze, mouse)
            time.sleep(0.05)
            if solve_maze(maze, mouse):
                return True
            else:
                mouse.pop_last_action()
                mouse.set_position((mouse.get_position()[0], mouse.get_position()[1] + 1))
        if right:
            mouse.move_right()
            mouse.set_position((mouse.get_position()[0], mouse.get_position()[1] + 1))
            print_maze(maze, mouse)
            time.sleep(0.05)
            if solve_maze(maze, mouse):
                return True
            else:
                mouse.pop_last_action()
                mouse.set_position((mouse.get_position()[0], mouse.get_position()[1] - 1))
        if up:
            mouse.move_up()
            mouse.set_position((mouse.get_position()[0] - 1, mouse.get_position()[1]))
            print_maze(maze, mouse)
            time.sleep(0.05)
            if solve_maze(maze, mouse):
                return True
            else:
                mouse.pop_last_action()
                mouse.set_position((mouse.get_position()[0] + 1, mouse.get_position()[1]))
        if down:
            mouse.move_down()
            mouse.set_position((mouse.get_position()[0] + 1, mouse.get_position()[1]))
            print_maze(maze, mouse)
            time.sleep(0.05)
            if solve_maze(maze, mouse):
                return True
            else:
                mouse.pop_last_action()
                mouse.set_position((mouse.get_position()[0] - 1, mouse.get_position()[1]))

def follow_path(maze, mouse, path):
    print_maze(maze, mouse)
    time.sleep(0.05)
    for action in path:
        x, y = mouse.get_position()
        if action == 'l':
            mouse.set_position((x, y - 1))
        elif action == 'r':
            mouse.set_position((x, y + 1))
        elif action == 'u':
            mouse.set_position((x - 1, y))
        elif action == 'd':
            mouse.set_position((x + 1, y))
        print_maze(maze, mouse)
        time.sleep(0.05)

n = 10
m = 10
mouse = Micromouse()
maze = genMaze(n, m)
print_maze(maze, mouse)
solve_maze(maze, mouse)
mouse.set_position((0, 0))
print(mouse.memory)
time.sleep(5)
follow_path(maze, mouse, mouse.memory)
