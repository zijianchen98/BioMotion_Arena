
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
dt = 1 / fps

# Initial positions of the lights representing the 'sadman' lying down
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.7],  # Left Shoulder
    [0.6, 0.7],  # Right Shoulder
    [0.3, 0.6],  # Left Elbow
    [0.7, 0.6],  # Right Elbow
    [0.2, 0.5],  # Left Hand
    [0.8, 0.5],  # Right Hand
    [0.5, 0.6],  # Chest
    [0.4, 0.5],  # Left Hip
    [0.6, 0.5],  # Right Hip
    [0.3, 0.4],  # Left Knee
    [0.7, 0.4],  # Right Knee
    [0.2, 0.3],  # Left Foot
    [0.8, 0.3],  # Right Foot
    [0.5, 0.9]   # Additional point above head
])

# Generate smooth motion using sine waves with different frequencies and phases
def generate_motion(t):
    positions = initial_positions.copy()
    positions[:, 1] += 0.05 * np.sin(2 * np.pi * (0.5 + 0.1 * np.arange(num_lights)) * t)
    positions[:, 0] += 0.03 * np.cos(2 * np.pi * (0.5 + 0.1 * np.arange(num_lights)) * t)
    return positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_aspect('equal')

# Create scatter plot for the point lights
scat = ax.scatter([], [], s=100, c='white')

# Update function for the animation
def update(frame):
    t = frame * dt
    positions = generate_motion(t)
    scat.set_offsets(positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()
