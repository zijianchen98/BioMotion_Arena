
import pyglet
import math

# Constants for the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Parameters for the walking motion
NUM_LIGHTS = 15
WALKING_PERIOD = 5.0  # seconds for one walking cycle
ARM_LENGTH = 50  # Length of the arm in pixels
LEG_LENGTH = 100  # Length of the leg in pixels

class WalkingMan:
    def __init__(self):
        self.lights = []
        self.init_lights()
        self.time = 0

    def init_lights(self):
        # Initialize lights in a circle to represent the upper and lower body
        for i in range(NUM_LIGHTS):
            angle = 2 * math.pi * i / NUM_LIGHTS
            self.lights.append({
                'x': WINDOW_WIDTH // 2 + ARM_LENGTH * math.cos(angle),
                'y': WINDOW_HEIGHT // 2 + ARM_LENGTH * math.sin(angle),
                'vx': 0,
                'vy': 0
            })

    def update(self, dt):
        self.time += dt
        t = self.time % WALKING_PERIOD

        # Positions for the left and right legs
        left_leg_angle = -math.pi / 2 + math.pi * 4 * t / WALKING_PERIOD
        right_leg_angle = math.pi / 2 - math.pi * 4 * t / WALKING_PERIOD

        # Positions for the left and right arms
        left_arm_angle = math.pi / 2 - math.pi * 4 * t / WALKING_PERIOD
        right_arm_angle = -math.pi / 2 + math.pi * 4 * t / WALKING_PERIOD

        # Update lights positions
        for i, light in enumerate(self.lights):
            angle = 2 * math.pi * i / NUM_LIGHTS
            if i < NUM_LIGHTS // 2:
                light['x'] = WINDOW_WIDTH // 2 + LEG_LENGTH * math.cos(left_leg_angle + angle * 0.5)
                light['y'] = WINDOW_HEIGHT // 2 + LEG_LENGTH * math.sin(left_leg_angle + angle * 0.5)
            else:
                light['x'] = WINDOW_WIDTH // 2 + LEG_LENGTH * math.cos(right_leg_angle + angle * 0.5)
                light['y'] = WINDOW_HEIGHT // 2 + LEG_LENGTH * math.sin(right_leg_angle + angle * 0.5)

class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__(WINDOW_WIDTH, WINDOW_HEIGHT, 'Walking Man Animation')
        self.walking_man = WalkingMan()
        pyglet.clock.schedule(self.update)

    def on_draw(self):
        self.clear()
        self.draw_lights()

    def draw_lights(self):
        for light in self.walking_man.lights:
            pyglet.windowgl.drawirect(
                light['x'] - 2, light['y'] - 2, 4, 4,
                color=(255, 255, 255, 255)
            )

    def update(self, dt):
        self.walking_man.update(dt)

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
