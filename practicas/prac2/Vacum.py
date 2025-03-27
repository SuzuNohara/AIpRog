import random

class Vacuum:
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
        self.battery_level = 100  # Assuming full battery level is 100

    def set_random_position(self, n, m):
        self.x = random.randint(0, n-1)
        self.y = random.randint(0, m-1)

    def __str__(self):
        return (f"Position: ({self.x}, {self.y}), Battery: {self.battery_level}, "
                f"Movements: {self.movements}, Cleanings: {self.cleanings}, Recharges: {self.recharges}")