
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights (simplified human figure with joints)
# Head, shoulders, elbows, wrists, hips, knees, ankles, and hand points
initial_positions = np.array([
    [0, 10],  # Head
    [-2, 8],  # Left shoulder
    [2, 8],   # Right shoulder
    [-3, 6],  # Left elbow
    [3, 6],   # Right elbow
    [-4, 4],  # Left wrist
    [4, 4],   # Right wrist
    [0, 0],   # Left hip
    [0, 0],   # Right hip
    [-1, -2], # Left knee
    [1, -2],  # Right knee
    [-1, -4], # Left ankle
    [1, -4],  # Right ankle
    [4.5, 4], # Right hand (waving)
    [-4.5, 4] # Left hand (static)
])

# Number of frames for the animation
n_frames = 100

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Function to update the animation
def update(frame):
    positions = initial_positions.copy()
    
    # Simulate waving motion for the right hand (point 13)
    angle = np.sin(frame * 0.1) * 0.5  # Smooth waving motion
    positions[13] = [4.5 + angle, 4 + 0.2 * np.cos(frame * 0.1)]  # Right hand moves
    
    # Slight body sway to indicate heavy weight and sadness
    sway = 0.1 * np.sin(frame * 0.05)
    positions[0] += [sway, 0]  # Head sway
    positions[1:3] += [sway * 0.8, 0]  # Shoulders sway less
    positions[7:9] += [sway * 0.6, 0]  # Hips sway
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
