
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.axis('off')  # Hide axes for a clean look

# Number of points
num_points = 15

# Initial positions of the point-lights
positions = np.array([
    [0, 8],  # Head
    [-1, 7], [1, 7],  # Shoulders
    [-2, 6], [2, 6],  # Upper arms
    [-1, 5], [1, 5],  # Hands
    [0, 5],  # Torso center
    [-1.5, 4], [1.5, 4],  # Upper legs
    [-1.5, 2], [1.5, 2],  # Lower legs
    [-1, 1], [0, 1], [1, 1],  # Feet
])

# Scatter plot for point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=20)

def update(frame):
    """Update the positions of points for sitting down animation."""
    global positions

    # Modify positions to represent a sitting down animation
    # The movement is simplified and biomechanical plausibility is simulated
    if frame < 30:  # Sitting down phase
        shift = frame / 30
        positions[:, 1] = positions[:, 1] - shift
        positions[13:15, 1] += shift / 2  # Simulating foot reposition
    else:  # Hold sitting position
        positions[:, 1] = positions[:, 1]

    scatter.set_offsets(positions)
    return scatter,

# Animation
ani = animation.FuncAnimation(
    fig, update, frames=60, interval=100, blit=True, repeat=True
)

plt.show()
