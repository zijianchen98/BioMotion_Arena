
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100

# Initial positions of the lights
positions = np.zeros((num_lights, 2))
positions[:, 0] = np.linspace(0, 1, num_lights)
positions[:, 1] = 0.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the lights
lights, = ax.plot([], [], 'wo', markersize=10)

def init():
    lights.set_data([], [])
    return lights,

def update(frame):
    # Update positions for the rolling motion
    angle = 2 * np.pi * frame / num_frames
    positions[:, 0] = 0.5 + 0.4 * np.sin(angle) * np.linspace(0, 1, num_lights)
    positions[:, 1] = 0.5 + 0.4 * np.cos(angle) * np.linspace(0, 1, num_lights)
    
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
