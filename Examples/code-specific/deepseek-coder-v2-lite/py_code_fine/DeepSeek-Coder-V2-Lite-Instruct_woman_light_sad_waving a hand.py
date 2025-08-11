
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100

# Initialize positions
positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    positions[i, 0] = np.cos(2 * np.pi * i / num_lights)
    positions[i, 1] = np.sin(2 * np.pi * i / num_lights)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal', 'box')
ax.set_facecolor('black')

# Initialize lights
lights, = ax.plot([], [], 'wo', markersize=10)

def init():
    lights.set_data([], [])
    return lights,

def update(frame):
    # Update positions
    for i in range(num_lights):
        positions[i, 0] += 0.02 * np.cos(2 * np.pi * i / num_lights + frame / 10)
        positions[i, 1] += 0.02 * np.sin(2 * np.pi * i / num_lights + frame / 10)
    
    # Update light positions
    lights.set_data(positions[:, 0], positions[:, 1])
    return lights,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, num_frames), init_func=init, blit=True, repeat=True)

# Display animation
plt.show()
