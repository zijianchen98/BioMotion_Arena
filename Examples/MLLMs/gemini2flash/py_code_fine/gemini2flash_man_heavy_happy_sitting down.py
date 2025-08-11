
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (standing position)
initial_positions = np.array([
    [0, 10],  # Head
    [-2, 9],  # Left shoulder
    [2, 9],  # Right shoulder
    [-4, 6],  # Left elbow
    [4, 6],  # Right elbow
    [-5, 3],  # Left wrist
    [5, 3],  # Right wrist
    [-1, 7],  # Left hip
    [1, 7],  # Right hip
    [-2, 4],  # Left knee
    [2, 4],  # Right knee
    [-2, 1],  # Left ankle
    [2, 1],  # Right ankle
    [-3, -1], # Left foot
    [3, -1]   # Right foot
])

# Define the positions of the points when sitting down
sitting_positions = np.array([
    [0, 8],  # Head
    [-2, 7],  # Left shoulder
    [2, 7],  # Right shoulder
    [-3, 5],  # Left elbow
    [3, 5],  # Right elbow
    [-4, 4],  # Left wrist
    [4, 4],  # Right wrist
    [-1, 5],  # Left hip
    [1, 5],  # Right hip
    [-1, 3],  # Left knee
    [1, 3],  # Right knee
    [-1, 2],  # Left ankle
    [1, 2],  # Right ankle
    [-1, 1], # Left foot
    [1, 1]   # Right foot
])

# Number of frames for the animation
num_frames = 100

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(-6, 6)
ax.set_ylim(-3, 11)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=8)  # White points

# Interpolate between the initial and sitting positions for a smooth animation
def animate(i):
    # Calculate the interpolation factor
    t = i / num_frames

    # Interpolate the positions of the points
    positions = (1 - t) * initial_positions + t * sitting_positions

    # Update the scatter plot data
    points.set_data(positions[:, 0], positions[:, 1])

    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
