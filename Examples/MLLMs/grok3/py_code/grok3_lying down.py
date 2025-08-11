
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define initial positions and structure for a lying down human (15 points)
# Approximate joint positions for a side view of a lying person
initial_positions = np.array([
    [0, 0],    # Head
    [1, 0.5],  # Neck
    [2, 0.5],  # Right shoulder
    [3, 0.5],  # Right elbow
    [4, 0.5],  # Right wrist
    [2, 1],    # Right hip
    [3, 1],    # Right knee
    [4, 1],    # Right ankle
    [2, -0.5], # Left shoulder
    [3, -0.5], # Left elbow
    [4, -0.5], # Left wrist
    [2, 0],    # Left hip
    [3, 0],    # Left knee
    [4, 0],    # Left ankle
    [1.5, 0]   # Chest
]) * 10  # Scale up for visibility

# Breathing and slight limb movement for realism
def update(frame, points, scat):
    # Small breathing motion (chest and abdomen)
    breath_amplitude = 0.2 * np.sin(frame * 0.1)
    points[14] = initial_positions[14] + [0, breath_amplitude]  # Chest movement
    
    # Slight limb oscillation for natural motion
    for i in [2, 3, 4, 8, 9, 10]:  # Arms
        angle = 0.05 * np.sin(frame * 0.1)
        x, y = points[i] - initial_positions[i]
        length = np.sqrt(x**2 + y**2) or 1
        points[i] = initial_positions[i] + [length * np.cos(angle), length * np.sin(angle)]
    for i in [6, 7, 13, 14]:  # Legs
        angle = 0.03 * np.sin(frame * 0.1)
        x, y = points[i] - initial_positions[i]
        length = np.sqrt(x**2 + y**2) or 1
        points[i] = initial_positions[i] + [length * np.cos(angle), length * np.sin(angle)]
    
    scat.set_offsets(points)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 50)
ax.set_ylim(-20, 20)
ax.axis('off')

# Initialize scatter plot
points = initial_positions.copy()
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), fargs=(points, scat), interval=50, blit=True)

plt.show()
