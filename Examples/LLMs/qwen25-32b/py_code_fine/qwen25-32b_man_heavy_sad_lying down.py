
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 100

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.axis('off')  # Hide the axes

# Initial positions for the point-lights representing a lying down sadman with heavy weight
positions = np.array([
    [0.4, 0.6], [0.5, 0.6], [0.6, 0.6],  # Head
    [0.35, 0.5], [0.45, 0.5], [0.55, 0.5], [0.65, 0.5],  # Torso
    [0.3, 0.4], [0.4, 0.4], [0.6, 0.4], [0.7, 0.4],  # Legs
    [0.35, 0.3], [0.45, 0.3], [0.55, 0.3], [0.65, 0.3]  # Heavy weight
])

# Scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Function to update the position of the points
def update(frame):
    global positions
    
    # Simulate a lying down motion with heavy weight
    amplitude = 0.05
    frequency = 0.05
    time = frame / frames * 2 * np.pi
    
    # Apply a sine wave motion to simulate breathing and weight compression
    positions[:, 1] += amplitude * np.sin(frequency * time + positions[:, 0] * 10)
    
    # Ensure the points don't move out of the range
    positions = np.clip(positions, 0, 1)
    
    scat.set_offsets(positions)

# Create the animation
animation = FuncAnimation(fig, update, frames=frames, interval=50, repeat=True)

plt.show()
