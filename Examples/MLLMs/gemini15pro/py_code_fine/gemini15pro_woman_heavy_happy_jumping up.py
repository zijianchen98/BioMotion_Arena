
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 100], [-10, 80], [10, 80],  # Head
    [-20, 60], [20, 60],  # Shoulders
    [-15, 40], [15, 40], # Elbows
    [-30, 40], [-10, 40], [10, 20], [30, 40], # Hands 
    [-15, 20], [15, 20],  # Hips
    [-20, 0], [20, 0],  # Knees
    [-25, -20], [25, -20] # Feet
])


# Define the jump motion function
def jump_motion(t, initial_positions):
    positions = initial_positions.copy()
    # Vertical jump motion
    y_offset = 50 * np.sin(np.pi * t / 20)  # Smooth jump curve
    positions[:, 1] += y_offset


    return positions

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)
ax.set_ylim(-30, 120)
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set black background
ax.set_xticks([]) #Turn off the axis
ax.set_yticks([]) #Turn off the axis
# Create the point light scatter plot
scatter = ax.scatter([], [], s=20, c='white')  # Initialize with empty data

# Define the animation update function
def update(frame):
    positions = jump_motion(frame, initial_positions)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=40, interval=50, blit=True)
plt.show()

