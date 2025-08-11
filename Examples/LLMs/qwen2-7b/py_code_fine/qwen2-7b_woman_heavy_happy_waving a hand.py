
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
WHITE = ( 255, 245, 220)
BLACK = ( 15, 15, 15)
FPS = 60
DURATION = 10
NUM_LIGHTS = 15
WAVE_SPEED = 0.1
WAVE_AMPLITUDE = 100
WAVE_FREQUENCY = 0.05
WAVE_PERIOD = 1 / WAVE_FREQUENCY

def wave_position(t):
    x = t * WAVE_SPEED
    y = WAVE_AMPLITUDE * np.sin(WAVE_FREQUENCY * x)
    return x, y

fig, ax = plt.subplots()
ax.set_xlim((-1, 1)
ax.set_ylim (-1, 1)
ax.set_aspect('equal')
ax.axis('off')

lights = []
for i in range(NUM_LIGHTS):
    x, y = wave_position(i * WAVE_PERIOD / NUM_LIGHTS)
    light = plt.Circle((x, y), radius=5, color=WHITE)
    ax.add_patch(light)
    lights.append(light)

def update(frame):
    for i, light in enumerate(lights):
        x, y = wave_position(i * WAVE_PERIOD / NUM_LIGHTS)
        light.set_center((x, y))

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, DURATION * FPS, interval=1000 / FPS, repeat=True)

plt.show()

