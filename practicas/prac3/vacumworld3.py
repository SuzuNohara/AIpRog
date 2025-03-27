import random
import os
import time
import logging

from sympy import false
from tabulate import tabulate

logging.basicConfig(filename='vacuum.log', level=logging.INFO, format='%(asctime)s - %(message)s')
SLEEP_TIME = 0.05

class Vacum:

    charger = (0, 0)
    dragging_charger = False

    def __init__(self, x, y, battery_level):
        self.x = x
        self.y = y
        self.battery_level = battery_level
        self.movements = 0
        self.cleanings = 0
        self.recharges = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.movements += 1
        self.battery_level -= 1

    def clean(self):
        self.cleanings += 1
        self.battery_level -= 1

    def recharge(self):
        self.recharges += 1
        self.battery_level = 20  # Assuming full battery level is 100

    def set_random_position(self, n, m):
        self.x = random.randint(0, n-1)
        self.y = random.randint(0, m-1)
        self.charger = (self.x, self.y)

    def calculate_world_statistics(self, world):
        total_cells = len(world) * len(world[0])
        dirty_cells = sum(row.count('\u2591\u2591') + row.count('\u2592\u2592') for row in world)
        obstacle_cells = sum(row.count('\u2588\u2588') for row in world)
        clean_cells = total_cells - dirty_cells - obstacle_cells
        return {
            "Total Cells": total_cells,
            "Dirty Cells": dirty_cells,
            "Obstacle Cells": obstacle_cells,
            "Clean Cells": clean_cells
        }

    def __str__(self):
        return (f"Position: ({self.x}, {self.y}), Battery: {self.battery_level}, "
                f"Movements: {self.movements}, Cleanings: {self.cleanings}, Recharges: {self.recharges}")

    def print_statistics(self, world):
        headers = ["Statistic", "Value"]
        data = [
            ["Position", f"({self.x}, {self.y})"],
            ["Battery Level", self.battery_level],
            ["Movements", self.movements],
            ["Cleanings", self.cleanings],
            ["Recharges", self.recharges]
        ]
        world_stats = self.calculate_world_statistics(world)
        for key, value in world_stats.items():
            data.append([key, value])
        print(tabulate(data, headers, tablefmt="grid"))

def create_world(n, m, include_obstacles=True):
    total_cells = n * m
    num_dirty = total_cells // 8  # Number of dirty cells
    num_obstacles = total_cells // 24  # Number of obstacles
    remainder = total_cells - (num_dirty * 2 + num_obstacles)  # Adjust remainder for spaces

    if include_obstacles:
        world = (['  '] * remainder + ['\u2591\u2591'] * num_dirty + ['\u2592\u2592'] * num_dirty + ['\u2588\u2588'] * num_obstacles)
    else:
        world = (['  '] * (remainder + num_obstacles) + ['\u2591\u2591'] * num_dirty + ['\u2592\u2592'] * num_dirty)

    random.shuffle(world)
    return [world[i * m:(i + 1) * m] for i in range(n)]

def print_world(world, vacum, prompt = ''):
    os.system('clear')
    print(f"({vacum.x}, {vacum.y}), {prompt}")
    n = len(world)
    m = len(world[0])
    for i, row in enumerate(world):
        row_str = '|'.join(row)
        if i == vacum.x:
            row_str = row_str[:vacum.y * 3] + '\033[91m\u2588\033[0m' + row_str[vacum.y * 3 + 1:]
        print('|' + row_str + '|')
    vacum.print_statistics(world)

def check_obstacle(vacum, world, where = 'here'):
    if where == 'here':
        return world[vacum.x][vacum.y] == '\u2588\u2588'
    elif where == 'left' and vacum.y > 0:
        return world[vacum.x][vacum.y - 1] == '\u2588\u2588'
    elif where == 'right' and vacum.y < len(world[0]) - 1:
        return world[vacum.x][vacum.y + 1] == '\u2588\u2588'
    elif where == 'top' and vacum.x > 0:
        return world[vacum.x - 1][vacum.y] == '\u2588\u2588'
    elif where == 'bottom' and vacum.x < len(world) - 1:
        return world[vacum.x + 1][vacum.y] == '\u2588\u2588'
    return False

def move(vacum, world):
    if vacum.dragging_charger:
        vacum.dragging_charger = False
        vacum.recharge()

def move_right(vacum, world):
    original_x = vacum.x
    while vacum.y < len(world[0]) - 1:
        vacum.move(0, 1)
        print_world(world, vacum, 'Avoiding Obstacle...')
        time.sleep(SLEEP_TIME)
        if check_obstacle(vacum, world):
            vacum.move(0, -1)
            print_world(world, vacum, 'Avoiding Obstacle...')
            time.sleep(SLEEP_TIME)
            if vacum.x < len(world) - 1:
                vacum.move(1, 0)
                print_world(world, vacum, 'Avoiding Obstacle...')
                time.sleep(SLEEP_TIME)
                while vacum.y < len(world[0]) - 1:
                    vacum.move(0, 1)
                    print_world(world, vacum, 'Avoiding Obstacle...')
                    time.sleep(SLEEP_TIME)
                    if not check_obstacle(vacum, world):
                        while vacum.x > original_x:
                            vacum.move(-1, 0)
                            print_world(world, vacum, 'Avoiding Obstacle...')
                            time.sleep(SLEEP_TIME)
                        return True
                vacum.move(-1, 0)
                print_world(world, vacum, 'Avoiding Obstacle...')
                time.sleep(SLEEP_TIME)
            return False
        return True

def move_left(vacum, world):
    original_x = vacum.x
    while vacum.y > 0:
        vacum.move(0, -1)
        print_world(world, vacum, 'Avoiding Obstacle...')
        time.sleep(SLEEP_TIME)
        if check_obstacle(vacum, world):
            vacum.move(0, 1)
            print_world(world, vacum, 'Avoiding Obstacle...')
            time.sleep(SLEEP_TIME)
            if vacum.x < len(world) - 1:
                vacum.move(1, 0)
                print_world(world, vacum, 'Avoiding Obstacle...')
                time.sleep(SLEEP_TIME)
                while vacum.y > 0:
                    vacum.move(0, -1)
                    print_world(world, vacum, 'Avoiding Obstacle...')
                    time.sleep(SLEEP_TIME)
                    if not check_obstacle(vacum, world):
                        while vacum.x > original_x:
                            vacum.move(-1, 0)
                            print_world(world, vacum, 'Avoiding Obstacle...')
                            time.sleep(SLEEP_TIME)
                        return True
                vacum.move(-1, 0)
                print_world(world, vacum, 'Avoiding Obstacle...')
                time.sleep(SLEEP_TIME)
            return False
        return True

def move_down(vacum, world):
    if vacum.x < len(world) - 1:
        vacum.move(1, 0)
        if check_obstacle(vacum, world):
            vacum.move(-1, 0)
            return false

def move_up(vacum, world):
    original_y = vacum.y
    while vacum.x > 0:
        vacum.move(-1, 0)
        print_world(world, vacum, 'Avoiding Obstacle...')
        time.sleep(SLEEP_TIME)
        if check_obstacle(vacum, world):
            vacum.move(1, 0)
            print_world(world, vacum, 'Avoiding Obstacle...')
            time.sleep(SLEEP_TIME)
            if vacum.y < len(world[0]) - 1:
                vacum.move(0, 1)
                print_world(world, vacum, 'Avoiding Obstacle...')
                time.sleep(SLEEP_TIME)
                while vacum.x > 0:
                    vacum.move(-1, 0)
                    print_world(world, vacum, 'Avoiding Obstacle...')
                    time.sleep(SLEEP_TIME)
                    if not check_obstacle(vacum, world):
                        while vacum.y > original_y:
                            vacum.move(0, -1)
                            print_world(world, vacum, 'Avoiding Obstacle...')
                            time.sleep(SLEEP_TIME)
                        return True
                vacum.move(0, -1)
                print_world(world, vacum, 'Avoiding Obstacle...')
                time.sleep(SLEEP_TIME)
            return False
        return True

def is_dirty(vacum, world):
    return world[vacum.x][vacum.y] == '\u2591\u2591' or world[vacum.x][vacum.y] == '\u2592\u2592'

def clean(vacum, world):
    if world[vacum.x][vacum.y] == '\u2592\u2592':
        world[vacum.x][vacum.y] = '\u2591\u2591'
    elif world[vacum.x][vacum.y] == '\u2591\u2591':
        world[vacum.x][vacum.y] = '  '
    vacum.clean()

def drag_charger(vacum, world):
    if vacum.x == vacum.charger[0] and vacum.y == vacum.charger[1]:
        vacum.dragging_charger = True

def left_blocked(vacum, world):
    return vacum.y == 0 or check_obstacle(vacum, world, 'left')

def top_blocked(vacum, world):
    return vacum.x == 0 or check_obstacle(vacum, world, 'top')

def right_blocked(vacum, world):
    return vacum.y == len(world[0]) - 1 or check_obstacle(vacum, world, 'right')

def is_end_right(vacum, world):
    return vacum.y == len(world[0]) - 1

def is_end_left(vacum, world):
    return vacum.y == 0

def is_end_bottom(vacum, world):
    return vacum.x == len(world) - 1

def is_end_top(vacum, world):
    return vacum.x == 0

def bottom_blocked(vacum, world):
    return vacum.x == len(world) - 1 or check_obstacle(vacum, world, 'bottom')

def go_start(vacum, world):
    while vacum.x != 0 or vacum.y != 0:
        if top_blocked(vacum, world) and left_blocked(vacum, world):
            logging.info("Top and left blocked")
            drag_charger(vacum, world)
            move_down(vacum, world)
            print_world(world, vacum)
            time.sleep(SLEEP_TIME)
            drag_charger(vacum, world)
            move_left(vacum, world)
            print_world(world, vacum)
            time.sleep(SLEEP_TIME)
        drag_charger(vacum, world)
        if move_up(vacum, world):
            continue
        drag_charger(vacum, world)
        if move_left(vacum, world):
            continue
        print_world(world, vacum)
        time.sleep(SLEEP_TIME)

def main(vacum, world):
    go_start(vacum, world)
    direction=True
    while True:
        if vacum.battery_level <= 10:  # Check if battery is low
            print_world(world, vacum, 'Recharging...')
            vacum.recharge()
            print_world(world, vacum, 'Recharged')
            time.sleep(SLEEP_TIME)

        if is_dirty(vacum, world):
            clean(vacum, world)
            print_world(world, vacum, 'Cleaning...')
            time.sleep(SLEEP_TIME)
        else:
            if right_blocked(vacum, world) and ~is_end_right(vacum, world) and direction == True:
                move_right(vacum, world)

            if left_blocked(vacum, world) and ~is_end_left(vacum, world) and direction == False:
                move_left(vacum, world)

            if right_blocked(vacum, world) and direction == True:
                if is_end_bottom(vacum, world):
                    break
                print_world(world, vacum, 'Finishing line to the right...')
                time.sleep(SLEEP_TIME)
                move_down(vacum, world)
                direction=False
            elif left_blocked(vacum, world) and direction == False:
                if is_end_bottom(vacum, world):
                    break
                while bottom_blocked(vacum, world):
                    move_right(vacum, world)
                print_world(world, vacum, 'Finishing line to the left...')
                time.sleep(SLEEP_TIME)
                move_down(vacum, world)
                direction=True
            else:
                if direction:
                    move_right(vacum, world)
                    print_world(world, vacum, 'Moving right...')
                else:
                    move_left(vacum, world)
                    print_world(world, vacum, 'Moving left...')
                time.sleep(SLEEP_TIME)
    vacum.print_statistics(world)

m = 40
n = 20

world = create_world(n, m, True)
vacum = Vacum(0, 0, 20)
vacum.set_random_position(n, m)
print_world(world, vacum)
vacum.print_statistics(world)
main(vacum, world)