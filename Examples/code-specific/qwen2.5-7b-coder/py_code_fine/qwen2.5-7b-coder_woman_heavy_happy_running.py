
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each light
target_positions = np.array([
    [0.1, 0.8], [0.2, 0.7], [0.3, 0.6], [0.4, 0.5], [0.5, 0.4],
    [0.6, 0.3], [0.7, 0.2], [0.8, 0.1], [0.9, 0.8], [1.0, 0.7],
    [0.1, 0.6], [0.2, 0.5], [0.3, 0.4], [0.4, 0.3], [0.5, 0.2]
])

# Define the speed of each light
speeds = np.random.uniform(0.01, 0.05, num_lights)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot for the point lights
scatter = ax.scatter([], [], color='white', s=50)

def update(frame):
    # Update the positions of the point lights
    initial_positions += speeds * frame / 100
    
    # Wrap around the positions if they go out of bounds
    initial_positions[initial_positions > 1] -= 1
    initial_positions[initial_positions < 0] += 1
    
    # Set the new positions of the point lights
    scatter.set_offsets(initial_positions)
    
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 1000), interval=50, blit=True)

plt.show()
