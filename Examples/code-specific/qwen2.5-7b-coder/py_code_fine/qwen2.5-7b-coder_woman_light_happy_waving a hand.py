
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2)

# Define the speed and direction of each light
speeds = np.random.uniform(0.05, 0.1, num_lights)
directions = np.random.randn(num_lights, 2)
directions /= np.linalg.norm(directions, axis=1, keepdims=True)

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for the point lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

def update(frame):
    global initial_positions, speeds, directions
    
    # Update the positions of the point lights
    initial_positions += speeds * directions
    
    # Apply boundary conditions to make the lights bounce off the edges
    initial_positions[initial_positions > 1] = 2 - initial_positions[initial_positions > 1]
    initial_positions[initial_positions < -1] = -initial_positions[initial_positions < -1]
    
    # Update the scatter plot with the new positions
    scat.set_offsets(initial_positions)
    
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
