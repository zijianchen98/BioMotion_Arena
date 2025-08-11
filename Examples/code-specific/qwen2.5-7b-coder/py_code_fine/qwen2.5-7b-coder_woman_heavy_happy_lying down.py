
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2) * 8 - 4  # Random positions between -4 and 4

# Define the target positions for the point lights
target_positions = np.array([
    [-3, -3], [-2, -3], [-1, -3], [0, -3], [1, -3],
    [-2, -2], [-1, -2], [0, -2], [1, -2], [2, -2],
    [-1, -1], [0, -1], [1, -1],
    [-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]
])

# Define the time steps for the animation
time_steps = np.linspace(0, 1, len(target_positions))

# Define the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create scatter plot for the point lights
point_lights = ax.scatter([], [], color='white', s=100)

def update(frame):
    t = time_steps[frame]
    current_positions = initial_positions + t * (target_positions - initial_positions)
    point_lights.set_offsets(current_positions)
    return point_lights,

# Create the animation
animation = FuncAnimation(fig, update, frames=len(time_steps), interval=100, blit=True)

plt.show()
