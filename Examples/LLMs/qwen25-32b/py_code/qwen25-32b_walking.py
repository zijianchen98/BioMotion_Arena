
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis.
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide the axes.

# Number of points
num_points = 15

# Initial positions for the points (these can be adjusted based on desired starting position)
positions = np.array([
    [4, 5], [5, 5], [6, 5],  # Head and shoulders
    [3, 6], [7, 6],          # Arms
    [3, 4], [7, 4],          # Shoulders
    [4, 3], [6, 3],          # Hips
    [2, 2], [8, 2],          # Legs
    [2, 1], [8, 1],          # Feet
    [4, 1], [6, 1]           # Ankles
])

# Scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Walking cycle parameters
cycle_length = 200
step_size = 0.05

def update(frame):
    global positions
    
    # Simulating walking by shifting the legs and arms
    if frame % cycle_length < cycle_length / 2:
        positions[9][0] += step_size  # Right leg forward
        positions[10][0] += step_size  # Right foot forward
        positions[11][0] -= step_size  # Left leg backward
        positions[12][0] -= step_size  # Left foot backward
        positions[4][0] -= step_size  # Left arm forward
        positions[3][0] += step_size  # Right arm backward
    else:
        positions[9][0] -= step_size  # Right leg backward
        positions[10][0] -= step_size  # Right foot backward
        positions[11][0] += step_size  # Left leg forward
        positions[12][0] += step_size  # Left foot forward
        positions[4][0] += step_size  # Left arm backward
        positions[3][0] -= step_size  # Right arm forward

    # Update the scatter plot with new positions
    scat.set_offsets(positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=cycle_length * 10, interval=50, repeat=True)

plt.show()
