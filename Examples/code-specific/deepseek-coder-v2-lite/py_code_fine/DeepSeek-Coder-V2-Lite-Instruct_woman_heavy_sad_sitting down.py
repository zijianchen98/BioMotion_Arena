
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 5  # seconds
fps = 30
num_frames = duration * fps

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(5, 10, num_lights)
positions[:, 1] = 5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights, = ax.plot([], [], 'wo', markersize=10)

def init():
    lights.set_data([], [])
    return lights,

def animate(i):
    # Update positions
    for j in range(num_lights):
        positions[j, 1] = 5 - 0.5 * np.sin(2 * np.pi * i / (fps / 2))
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
