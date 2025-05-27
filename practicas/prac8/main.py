import random
import os
import time

ascii_map = {
        0: '    ',  # Empty space
        1: {
            0: 'W',  # Wampus
            1: '~',  # Odor
            2: 'G',  # Gold
            3: '░',  # Wind
            4: '▓'   # Pit
        }
    }

def create_world(n, m):
    # Initialize the world with all zeros
    world = [[[0, 0, 0, 0, 0] for _ in range(m)] for _ in range(n)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    # Place Wampus
    while True:
        wampus_x, wampus_y = random.randint(0, n-1), random.randint(0, m-1)
        if (wampus_x, wampus_y) != (0, 0):
            world[wampus_x][wampus_y][0] = 1  # Wampus
            # Add odor around Wampus
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = wampus_x + dx, wampus_y + dy
                if is_valid(nx, ny):
                    world[nx][ny][1] = 1  # Odor
            break

    # Place Gold
    while True:
        gold_x, gold_y = random.randint(0, n-1), random.randint(0, m-1)
        if (gold_x, gold_y) != (0, 0) and (gold_x, gold_y) != (wampus_x, wampus_y):
            world[gold_x][gold_y][2] = 1  # Gold
            break

    # Place Pits
    pits_to_place = n - 1
    while pits_to_place > 0:
        pit_x, pit_y = random.randint(0, n-1), random.randint(0, m-1)
        if (pit_x, pit_y) != (0, 0) and (pit_x, pit_y) != (wampus_x, wampus_y) and (pit_x, pit_y) != (gold_x, gold_y) and world[pit_x][pit_y][4] == 0:
            world[pit_x][pit_y][4] = 1  # Pit
            # Add wind around Pit
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = pit_x + dx, pit_y + dy
                if is_valid(nx, ny):
                    world[nx][ny][3] = 1  # Wind
            pits_to_place -= 1

    return world

def cell_to_ascii(cell):
    # Convert a cell's binary indicators to ASCII characters
    ascii_cell = []
    for i, value in enumerate(cell):
        if value == 1:
            ascii_cell.append(ascii_map[1][i])
    return ascii_cell if ascii_cell else ['    ']

def print_world(world, agent_position):
    import os
    os.system('clear')

    def create_border_line(columns):
        return '+' + ('----+' * columns)

    for row_index, row in enumerate(world):
        # Print the top border for the row
        print(create_border_line(len(row)))
        # Each row will be printed as 4 lines
        row_lines = ['' for _ in range(4)]
        for col_index, cell in enumerate(row):
            ascii_cell = cell_to_ascii(cell)
            # Check if the agent is in the current cell
            if (row_index, col_index) == agent_position:
                ascii_cell = [' A  ']  # Represent the agent
            # Format the cell into 4 lines
            for i in range(4):
                if i < len(ascii_cell):
                    row_lines[i] += f"|{ascii_cell[i]:<4}"
                else:
                    row_lines[i] += "|    "
        # Print the 4 lines for the row
        for line in row_lines:
            print(line + '|')
    # Print the bottom border for the last row
    print(create_border_line(len(world[0])))

class Agent:
    def __init__(self):
        self.position = (0, 0)  # Start at the top-left corner
        self.memory = {}  # Memory to store discovered cells
        self.has_gold = False  # Track if the agent has taken the gold

    def perceive(self, world):
        x, y = self.position
        self.memory[(x, y)] = world[x][y]  # Store the current cell in memory

    def evaluate_proposition(self, n, m):
        # Logical propositions: Check for gold, Wampus, or pit
        x, y = self.position
        cell = self.memory[(x, y)]
        if cell[2] == 1:  # Check if there's gold in the current cell
            self.has_gold = True
            print("Gold found and taken! Game over.")
            return True
        if cell[0] == 1:  # Check if there's a Wampus
            self.is_alive = False
            print("Encountered the Wampus! The agent has died. Game over.")
            return True
        if cell[4] == 1:  # Check if there's a pit
            self.is_alive = False
            print("Fell into a pit! The agent has died. Game over.")
            return True
            # Logical rule: If wind is perceived and only one adjacent unexplored cell remains, deduce the pit's location
        if cell[3] == 1:  # Wind
            unexplored_cells = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Adjacent cells
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in self.memory:
                    unexplored_cells.append((nx, ny))

            if len(unexplored_cells) == 1:  # Only one unexplored cell
                pit_x, pit_y = unexplored_cells[0]
                print(f"Based on the wind, deducing a pit at ({pit_x}, {pit_y}).")
                self.memory[(pit_x, pit_y)] = [0, 0, 0, 0, 1]  # Mark as pit in memory

        # Logical rule: If a cell is adjacent to a visited cell where no wind was perceived, mark it as safe
        for (visited_x, visited_y), visited_cell in list(self.memory.items()):  # Create a static copy of items
            if visited_cell[3] == 0:  # No wind perceived
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Adjacent cells
                    safe_x, safe_y = visited_x + dx, visited_y + dy
                    if 0 <= safe_x < n and 0 <= safe_y < m and (safe_x, safe_y) not in self.memory:
                        print(
                            f"Marking cell ({safe_x}, {safe_y}) as safe based on no wind at ({visited_x}, {visited_y}).")
                        self.memory[(safe_x, safe_y)] = [0, 0, 0, 0, 0]  # Mark as safe in memory


        return False

    def move(self, n, m):
        # Move to the nearest safe cell
        x, y = self.position
        safe_cells = [(sx, sy) for (sx, sy), cell in self.memory.items() if cell == [0, 0, 0, 0, 0]]

        if safe_cells:
            # Find the closest safe cell (Manhattan distance)
            safe_cells.sort(key=lambda pos: abs(pos[0] - x) + abs(pos[1] - y))
            self.position = safe_cells[0]
            print(f"Moving to safe cell: {self.position}")
            return True
        else:
            print("No safe cells available to move.")
            return False

def print_agent_memory(agent, n, m):
    def create_border_line(columns):
        return '+' + ('----+' * columns)
    for row_index in range(n):
        # Print the top border for the row
        print(create_border_line(m))
        # Each row will be printed as 4 lines
        row_lines = ['' for _ in range(4)]
        for col_index in range(m):
            if (row_index, col_index) in agent.memory:
                cell = agent.memory[(row_index, col_index)]
                if cell == [0, 0, 0, 0, 0]:  # Safe cell
                    ascii_cell = [' S  ']
                else:
                    ascii_cell = cell_to_ascii(cell)
            else:
                ascii_cell = ['    ']  # Empty cell for unexplored areas
            # Format the cell into 4 lines
            for i in range(4):
                if i < len(ascii_cell):
                    row_lines[i] += f"|{ascii_cell[i]:<4}"
                else:
                    row_lines[i] += "|    "
        # Print the 4 lines for the row
        for line in row_lines:
            print(line + '|')
    # Print the bottom border for the last row
    print(create_border_line(m))

def main():
    n, m = 5, 5
    world = create_world(n, m)
    agent = Agent()

    while not agent.has_gold:
        print_world(world, agent.position)
        print_agent_memory(agent, n, m)
        time.sleep(1)
        agent.perceive(world)
        if agent.evaluate_proposition(n, m):
            break
        if not agent.move(n, m):
            print("Agent couldn't find the gold. Game over.")
            break

main()