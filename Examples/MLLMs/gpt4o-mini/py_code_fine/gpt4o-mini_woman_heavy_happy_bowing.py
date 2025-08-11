
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_points = 15

# Initial positions of point-lights arranged in a bowing posture
initial_positions = np.array([
    [0, 0],     # Head
    [-0.5, -1], # Shoulder Left
    [0.5, -1],  # Shoulder Right
    [-0.75, -2], # Elbow Left
    [0.75, -2],  # Elbow Right
    [-1, -3],   # Wrist Left
    [1, -3],    # Wrist Right
    [0, -4],    # Torso
    [-0.5, -5], # Hip Left
    [0.5, -5],  # Hip Right
    [-0.75, -6], # Knee Left
    [0.75, -6],  # Knee Right
    [-1, -7],   # Ankle Left
    [1, -7],    # Ankle Right
    [0, -8]     # Ground between feet
])

# Update function for animation
def update(frame):
    # Creating a bowing motion
    bow_angle = np.pi / 12 * np.sin(frame / 10)  # Angle for bowing
    bow_amount = 0.5 * np.sin(frame / 10)      # Amount of bending

    # Update positions to create a simple bowing motion
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] -= bow_amount  # Adjust vertical position downwards (bowing)
    updated_positions[:, 0] += (np.sin(bow_angle * np.arange(num_points)) * 0.2)  # Slight sway

    scat.set_offsets(updated_positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-9, 1)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Create scatter plot for the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Show the animation
plt.show()
