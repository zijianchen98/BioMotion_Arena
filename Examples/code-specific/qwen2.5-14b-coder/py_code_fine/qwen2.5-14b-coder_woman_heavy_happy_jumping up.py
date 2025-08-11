
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for the point lights (approximation of jumping motion)
target_positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    # Randomly distribute the points around a central point
    angle = 2 * np.pi * i / num_lights
    radius = np.random.uniform(0.1, 0.4)
    target_positions[i] = [np.cos(angle) * radius, np.sin(angle) * radius]

# Define the animation function
def animate(frame):
    # Calculate the current position of each point light
    t = frame / 100.0  # Time parameter from 0 to 1
    current_positions = (1 - t) * initial_positions + t * target_positions
    
    # Update the scatter plot
    sc.set_offsets(current_positions)
    
    return sc,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot
sc = ax.scatter([], [], color='white', s=10)

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
