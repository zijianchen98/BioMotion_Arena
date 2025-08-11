
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the coordinates for 15 point-lights representing a running woman
# Initial positions based on a simplified biomechanical model
initial_positions = np.array([
    [0, 10],  # Head
    [0, 8],   # Neck
    [0, 6],   # Chest
    [-1, 4],  # Left shoulder
    [1, 4],   # Right shoulder
    [-2, 2],  # Left elbow
    [2, 2],   # Right elbow
    [-3, 0],  # Left wrist
    [3, 0],   # Right wrist
    [0, 4],   # Hip
    [-1, 2],  # Left hip
    [1, 2],   # Right hip
    [-2, 0],  # Left knee
    [2, 0],   # Right knee
    [-2, -2], # Left ankle
    [2, -2]   # Right ankle
]) / 2  # Scale down for better visualization

# Define motion parameters for running
frames = 100
t = np.linspace(0, 2 * np.pi, frames)
amplitude = 1.0  # Vertical bounce
speed = 0.5      # Horizontal speed

# Function to update point positions for each frame
def update(frame):
    # Horizontal movement
    x_offset = speed * frame
    # Vertical bounce (sinusoidal motion for natural running)
    y_offset = amplitude * np.sin(t[frame])
    
    # Update positions with biomechanical constraints
    positions = initial_positions.copy()
    positions[:, 0] += x_offset  # Move horizontally
    positions[:, 1] += y_offset  # Add vertical bounce
    
    # Add limb movement (simplified sinusoidal for arms and legs)
    positions[7, 1] += 0.5 * np.sin(t[frame])  # Left wrist
    positions[8, 1] += 0.5 * np.sin(t[frame])  # Right wrist
    positions[14, 1] += 0.5 * np.cos(t[frame]) # Left ankle
    positions[15, 1] += 0.5 * np.cos(t[frame]) # Right ankle
    
    scatter.set_offsets(positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 10)
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter([], [], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
