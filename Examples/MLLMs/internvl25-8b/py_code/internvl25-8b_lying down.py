
import random
from time import sleep

class PointLightAnimator:
    def __init__(self):
        self.background = None
        self.lights = self.create_lights()

    def create_lights(self):
        lights = []
        for _ in range(15):
            x = random.randint(-50, 50)
            y = random.randint(-50, 50)
            light = {
                "x": x,
                "y": y,
                "speed": random.uniform(0.5, 2),
                "direction": random.choice(["up", "down", "left", "right"])
            }
            lights.append(light)
        return lights

    def draw(self):
        for light in self.lights:
            pos = f"({light['x']}, {light['y']})"
            direction = light["direction"]
            if direction == "up":
                yield f".{pos} "
            elif direction == "down":
                yield f"{pos}."
            elif direction == "left":
                yield "." * (light["x"] + 1) + " "
            elif direction == "right":
                yield " " * (light["x"] + 1) + "."

def animate():
    animator = PointLightAnimator()
    while True:
        print(animator.draw(), end="")
        sleep(0.1)
        print("\r".join(animator.draw()))

animate()
