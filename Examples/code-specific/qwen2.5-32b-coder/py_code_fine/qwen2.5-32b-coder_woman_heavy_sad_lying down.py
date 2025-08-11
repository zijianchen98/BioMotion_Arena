
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 100
fps = 30
dt = 1 / fps

# Initialize positions
positions = np.zeros((num_lights, 2))

# Define initial positions of the point lights for a lying person
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left Shoulder
    [0.6, 0.8],  # Right Shoulder
    [0.3, 0.7],  # Left Elbow
    [0.7, 0.7],  # Right Elbow
    [0.2, 0.6],  # Left Wrist
    [0.8, 0.6],  # Right Wrist
    [0.5, 0.6],  # Chest
    [0.4, 0.5],  # Left Hip
    [0.6, 0.5],  # Right Hip
    [0.3, 0.4],  # Left Knee
    [0.7, 0.4],  # Right Knee
    [0.2, 0.3],  # Left Ankle
    [0.8, 0.3],  # Right Ankle
    [0.5, 0.4]   # Belly
])

# Scale and center the initial positions
scale = 0.3
center = np.array([0.5, 0.5])
positions = initial_positions * scale + center

# Define the animation function
def update(frame):
    t = frame * dt
    
    # Simple harmonic motion for breathing effect
    breath = 0.01 * np.sin(2 * np.pi * t)
    
    # Update positions with a simple model of lying down motion
    new_positions = initial_positions.copy()
    new_positions[:, 1] += breath  # Breathing effect
    
    # Apply a small oscillation to simulate natural movement
    oscillation = 0.005 * np.sin(4 * np.pi * t)
    new_positions[:, 0] += oscillation
    
    # Update the scatter plot data
    scatter.set_offsets(new_positions * scale + center)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=False, repeat=True)

# Show the animation
plt.show()
