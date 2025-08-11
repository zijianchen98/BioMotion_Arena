
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points = ax.plot([], [], 'o', color='white')[0]

# Define number of points and their initial positions
num_points = 15
# Sample initial positions, can be adjusted for clarity
initial_positions = np.array([
    [0, 3],    # Head
    [-1, 2],   # Left shoulder
    [1, 2],    # Right shoulder
    [-2, 1],   # Left elbow
    [2, 1],    # Right elbow
    [-1, 0],   # Left hand
    [1, 0],    # Right hand
    [-1, -1],  # Left hip
    [1, -1],   # Right hip
    [-1.5, -2],# Left knee
    [1.5, -2], # Right knee
    [-1, -3],  # Left foot
    [1, -3],   # Right foot
    [0, -4],   # Center of weight
    [0, 4],    # Weight anchor point
    [0, 2.5]   # Mid-body point for smooth movement
])

# Set the animation parameters
def update(frame):
    # Create wave-like motion for running effect
    y_offset = np.sin(frame / 10) * 0.5
    positions = initial_positions.copy()
    
    # Adjust Y values to simulate running action
    positions[:, 0] += y_offset
    positions[:, 1] += np.cos(frame / 10) * 0.2  # horizontal motion
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
