
import random
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')  # Clear console

class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.animate = True

    def update_position(self):
        if self.animate:
            if self.x < 15:
                self.x += 1
                if self.y < 15 and self.y >= 0:
                    self.y = random.randint(0, 15)
            else:
                self.animate = False

def draw_point_lights(point_lights):
    for pl in point_lights:
        print("◯", end="")
        pl.update_position()
    print()

def movement_loop(point_lights):
    while len(point_lights) > 1:
        draw_point_lights(point_lights)
        time.sleep(0.2)
        if all(pl.animate == False for pl in point_lights):
            point_lights.pop(0)

def main():
    point_lights = [
        PointLight(0, random.randint(0, 15)) for _ in range(15)
    ]
    movement_loop(point_lights)

if __name__ == "__main__":
    main()
