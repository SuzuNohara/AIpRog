import random
import time
import os

SLEEP_TIME = 0.05

def create_world(n, m):
    total_cells = n * m
    alive_cells = total_cells // 4
    remainder = total_cells - alive_cells  # Adjust remainder for spaces

    world = (['  '] * remainder + ['\u2588\u2588'] * alive_cells)

    random.shuffle(world)
    print(f"total_cells: {total_cells}, alive: {alive_cells}, death cells: {remainder}")
    return [world[i * m:(i + 1) * m] for i in range(n)]

def print_world(world):
    os.system('clear')
    n = len(world)
    m = len(world[0])
    for i, row in enumerate(world):
        row_str = '|'.join(row)
        print('|' + row_str + '|')
        # if i < n - 1:
        #     print('-' * (m * 2 + (m + 1)))

def check_neibourgh(world_copy, x, y):
    alive = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if i < 0 or j < 0 or i >= len(world_copy) or j >= len(world_copy[0]):
                continue
            if world_copy[i][j] == '\u2588\u2588':
                alive += 1
    return alive

def update_world(world):
    world_copy = [row[:] for row in world]
    for i in range(n):
        for j in range(m):
            alive = check_neibourgh(world_copy, i, j)
            if world_copy[i][j] == '\u2588\u2588':
                if alive < 2 or alive > 3:
                    world[i][j] = '  '
                else:
                    world[i][j] = '\u2588\u2588'
            else:
                if alive == 3:
                    world[i][j] = '\u2588\u2588'
                else:
                    world[i][j] = '  '

def main(world):
    times = 5000
    time.sleep(2)
    while times > 0:
        print_world(world)
        time.sleep(SLEEP_TIME)
        # inst = input()
        update_world(world)
        times -= 1

n = 100
m = 100

world = create_world(n, m)
main(world)

