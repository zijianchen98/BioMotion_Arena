
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 50],  # Head top
    [-5, 45],  # Left shoulder
    [5, 45],  # Right shoulder
    [-10, 35], # Left elbow
    [10, 35], # Right elbow
    [-10, 25],  # Left wrist
    [10, 25],  # Right wrist
    [0, 30],  # Center of torso
    [-5, 20],  # Left hip
    [5, 20],  # Right hip
    [-5, 10], # Left knee
    [5, 10], # Right knee
    [-7, 0],  # Left ankle
    [7, 0],  # Right ankle
    [0, 2] # Base
])


# Define the animation function
def animate(i):
    # Simulate sitting down motion
    y_offset =  10 * np.sin(i * 0.05) # Oscillating movement
    positions = initial_positions.copy()

    positions[:, 1] -= (i * 0.2) % 50 # Gradual downwards movement


    scatter.set_offsets(positions)
    return scatter,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black') # Set background to black
ax.set_aspect('equal')
ax.set_xlim([-20, 20])
ax.set_ylim([-10, 60])

# Create the scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=20, c='white')


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()

