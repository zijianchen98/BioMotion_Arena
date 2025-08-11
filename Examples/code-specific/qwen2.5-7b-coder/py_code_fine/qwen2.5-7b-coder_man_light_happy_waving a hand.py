
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2)

# Define the speed and direction of each point light
speeds = np.random.rand(num_lights)
directions = np.random.rand(num_lights, 2) * 2 - 1

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
point_lights = ax.scatter([], [], color='white')

def update(frame):
    global initial_positions, speeds, directions
    
    # Update the positions of the point lights
    initial_positions += speeds[:, np.newaxis] * directions
    initial_positions %= 1  # Wrap around the edges of the screen
    
    # Update the scatter plot
    point_lights.set_offsets(initial_positions)
    
    return point_lights,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
