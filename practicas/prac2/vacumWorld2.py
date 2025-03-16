import random

world = [random.randint(0,1) for _ in range(20)]
position = 0
initial = 0
actions = 0
battery = 25
recharge = 0

def move_right():
    global position
    position = position + 1
    global actions
    actions = actions + 1
    global battery
    battery = battery - 1

def move_left():
    global position
    position = position - 1
    global actions
    actions = actions + 1
    global battery
    battery = battery - 1

def is_end():
    return position == 19

def is_start():
    return position == 0

def is_clean():
    global actions
    actions = actions + 1
    return world[position] == 0

def clean():
    world[position] = world[position] - 1
    global actions
    actions = actions + 1
    global battery
    battery = battery - 1

def position_start():
    while not is_start():
        move_left()

def battery_rannout():
    global battery
    return battery <= 0

def return_initial():
    global position
    position = initial
    global battery
    battery = 20
    global recharge
    recharge = recharge + 1

def create_world(dirt, obst):
    global world
    concurrency = dirt # int(input("Number of dirty squares: "))
    obstacles = obst # int(input("Number of obstacles: "))
    clean_squares = 20 - concurrency - obstacles
    world = [1] * concurrency + [0] * clean_squares + [-1] * obstacles
    random.shuffle(world)
    ones_indices = [i for i, x in enumerate(world) if x == 1]
    num_twos = len(ones_indices) // 2
    for i in random.sample(ones_indices, num_twos):
        world[i] = 2

def clean_left():
    while not is_start():
        # print_world()
        if battery_rannout():
            return_initial()
        elif world[position] == -1:
            move_right()
            break
        elif is_clean():
            if is_start():
                return_initial()
                break
            move_left()
        elif not is_clean():
            clean()
        
def clean_right():
    while not is_end():
        # print_world()
        if battery_rannout():
            return_initial()
        elif world[position] == -1:
            move_left()
            break
        elif is_clean():
            if is_end():
                return_initial()
                break
            move_right()
        elif not is_clean():
            clean()

def print_world():
    # print(f"Position: {position}")
    global battery
    global actions
    display_world = world.copy()
    print(f"{display_world}")
    display_world[position] = 'X'
    print(f"{display_world} b = {battery}, a = {actions}")
    

def main():
    tests = 100
    global position
    global actions
    global battery
    global recharge
    while tests > 0:
        actions = 0
        battery = 20
        recharge = 0
        create_world(5, 0)
        while True:
            position = random.randint(0, 19)
            if world[position] == -1:
                continue
            else:
                break
        global initial
        initial = position
        print("Initial::")
        print_world()
        clean_left()
        clean_right()
        print("Final::")
        print_world()
        print(f"Total actions: {actions}")
        print(f"Battery remaining: {battery}")
        print(f"Recharges: {recharge}")
        tests = tests - 1
    tests = 100
    while tests > 0:
        actions = 0
        battery = 20
        recharge = 0
        create_world(5, 1)
        while True:
            position = random.randint(0, 19)
            if world[position] == -1:
                continue
            else:
                break
        initial
        initial = position
        print("Initial::")
        print_world()
        clean_left()
        clean_right()
        print("Final::")
        print_world()
        print(f"Total actions: {actions}")
        print(f"Battery remaining: {battery}")
        print(f"Recharges: {recharge}")
        tests = tests - 1
    tests = 100
    while tests > 0:
        actions = 0
        battery = 20
        recharge = 0
        create_world(5, 2)
        while True:
            position = random.randint(0, 19)
            if world[position] == -1:
                continue
            else:
                break
        initial
        initial = position
        print("Initial::")
        print_world()
        clean_left()
        clean_right()
        print("Final::")
        print_world()
        print(f"Total actions: {actions}")
        print(f"Battery remaining: {battery}")
        print(f"Recharges: {recharge}")
        tests = tests - 1
    

main()