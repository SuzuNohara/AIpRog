import random

world = [random.randint(0,1) for _ in range(20)]
position = 0

def move_right():
    global position
    position = position + 1

def move_left():
    global position
    position = position - 1

def is_end():
    return position == 19

def is_start():
    return position == 0

def is_clean():
    return world[position] == 0

def clean():
    world[position] = 0
    
def position_start():
    while not is_start():
        move_left()

def verify_clean():
    position_start()
    while not is_end():
        if not is_clean():
            return False
        move_right()
    return is_clean()

def clean_world():
    while not is_end():
        clean()
        move_right()
    clean()

def create_world():
    global world
    concurrency = int(input("Number of dirty squares: "))
    world = [1] * concurrency + [0] * (20 - concurrency)
    random.shuffle(world)

def main():
    global position
    position = random.randint(0, 19)
    create_world()
    print(f"Initial world: {world}")
    while not verify_clean():
        position_start()
        clean_world()
    print(f"Final world: {world}")

main()