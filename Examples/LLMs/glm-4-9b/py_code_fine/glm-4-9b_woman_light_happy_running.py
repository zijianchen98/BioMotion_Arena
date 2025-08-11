
import pyglet
import math
import random

# Constants for the simulation
WIDTH, HEIGHT = 800, 600
NUM_LIGHTS = 15
FPS = 60
WALK周期 = 10  # Duration of one walk cycle in seconds

# Create a window
window = pyglet.window.Window(WIDTH, HEIGHT)
batch = pyglet.graphics.Batch()

# Class for a point-light representing part of the body
class PointLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)  # White light

    def update(self, dt):
        # Apply a simple sinusoidal motion to simulate running
        self.x = WIDTH // 2 + int(math.cos(pyglet.clock.time * 2 * math.pi / WALK周期) * WIDTH * 0.4)
        self.y = HEIGHT // 2 + int(math.sin(pyglet.clock.time * 2 * math.pi / WALK周期) * HEIGHT * 0.2)

# Create point-lights representing key points of a running person
lights = [PointLight(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_LIGHTS)]

@window.event
def on_draw():
    window.clear()
    
    for light in lights:
        light.draw()

@window.event
def update(dt):
    for light in lights:
        light.update(dt)

    pyglet.clock.schedule_once(update, 1/FPS)

pyglet.app.run()
