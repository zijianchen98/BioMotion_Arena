
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100
light_radius = 0.1

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(-1, 1, num_lights)
positions[:, 1] = 1

# Define the forward rolling motion
def forward_rolling(t):
    amplitude = 0.5
    frequency = 2
    phase = 0
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

lights, = ax.plot([], [], 'wo', markersize=light_radius*50)

def init():
    lights.set_data([], [])
    return lights,

def update(frame):
    t = frame / num_frames
    y_offset = forward_rolling(t)
    positions[:, 1] = 1 - y_offset
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=True)

plt.show()
