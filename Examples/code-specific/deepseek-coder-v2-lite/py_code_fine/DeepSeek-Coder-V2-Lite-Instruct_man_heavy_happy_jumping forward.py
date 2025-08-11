
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 2  # seconds
fps = 30
num_frames = duration * fps

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights, = ax.plot([], [], 'wo', markersize=10)

def init():
    lights.set_data([], [])
    return lights,

def animate(i):
    # Update positions
    positions[:, 1] = 0.5 + 0.2 * np.sin(2 * np.pi * (i / fps) / 0.5)
    positions[:, 0] = np.roll(positions[:, 0], -1)
    positions[-1, 0] = positions[-2, 0] + 0.05 + 0.05 * np.random.rand()
    
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
