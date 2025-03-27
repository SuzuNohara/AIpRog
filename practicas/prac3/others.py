def clean_left(vacum, world):
    while vacum.y >= 0:
        if left_blocked(vacum, world):
            if vacum.y == 0:
                break
            print_world(world, vacum, 'CLeaning left, Left Blocked...')
            time.sleep(1)
            if top_blocked(vacum, world) and bottom_blocked(vacum, world):
                break
            if top_blocked(vacum, world):
                move_down(vacum, world)
                print_world(world, vacum, 'Cleaning left, Left Blocked, Top Blocked...')
                time.sleep(1)
                if left_blocked(vacum, world):
                    break
                move_left(vacum, world)
                print_world(world, vacum, 'Cleaning left, Left Blocked, Top Blocked, evading...')
                time.sleep(1)
                while top_blocked(vacum, world) and ~left_blocked(vacum, world):
                    move_left(vacum, world)
                    print_world(world, vacum, 'Cleaning left...')
                    time.sleep(1)
                move_up(vacum, world)
                print_world(world, vacum, 'Cleaning left...')
                time.sleep(1)
            elif bottom_blocked(vacum, world):
                move_up(vacum, world)
                print_world(world, vacum, 'Cleaning left...')
                time.sleep(1)
                if left_blocked(vacum, world):
                    break
                move_left(vacum, world)
                print_world(world, vacum, 'Cleaning left, Left Blocked, Top Blocked, evading...')
                time.sleep(1)
                while bottom_blocked(vacum, world) and ~left_blocked(vacum, world):
                    move_left(vacum, world)
                    print_world(world, vacum, 'Cleaning left...')
                    time.sleep(1)
                move_down(vacum, world)
                print_world(world, vacum, 'Cleaning left...')
                time.sleep(1)
            else:
                move_up(vacum, world)
                print_world(world, vacum, 'Cleaning left...')
                time.sleep(1)
                if left_blocked(vacum, world):
                    break
                move_left(vacum, world)
                print_world(world, vacum, 'Cleaning left, Left Blocked, Top Blocked, evading...')
                time.sleep(1)
                while bottom_blocked(vacum, world) and ~left_blocked(vacum, world):
                    move_left(vacum, world)
                    print_world(world, vacum, 'Cleaning left...')
                    time.sleep(1)
                move_down(vacum, world)
                print_world(world, vacum, 'Cleaning left...')
                time.sleep(1)
        if is_dirty(vacum, world):
            clean(vacum, world)
            print_world(world, vacum, 'Cleaning left...')
            time.sleep(1)
        else:
            move_left(vacum, world)
            print_world(world, vacum, 'Cleaning left...')
            time.sleep(1)

def clean_right(vacum, world):
    while vacum.y < n:
        if right_blocked(vacum, world):
            logging.info("Right blocked")
            if top_blocked(vacum, world) and bottom_blocked(vacum, world):
                break
            if top_blocked(vacum, world):
                move_down(vacum, world)
                if right_blocked(vacum, world):
                    break
                while top_blocked(vacum, world) and ~right_blocked(vacum, world):
                    move_right(vacum, world)
                move_up(vacum, world)
            elif bottom_blocked(vacum, world):
                move_up(vacum, world)
                if right_blocked(vacum, world):
                    break
                while bottom_blocked(vacum, world) and ~right_blocked(vacum, world):
                    move_right(vacum, world)
                move_down(vacum, world)
            else:
                break
        if is_dirty(vacum, world):
            clean(vacum, world)
            print_world(world, vacum)
            time.sleep(1)
        else:
            move_right(vacum, world)

def clean_line(vacum, world):
    clean_left(vacum, world)
    clean_right(vacum, world)

def main(vacum, world):
    print_world(world, vacum)
    # go_start(vacum, world)
    clean_line(vacum, world)
