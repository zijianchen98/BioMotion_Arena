
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Define initial positions for 15 point-lights (simplified human figure with waving hand)
# Head, torso, shoulders, elbows, wrists, hips, knees, ankles, and waving hand
initial_positions = np.array([
    [0, 2],    # Head
    [0, 1.5],  # Torso top
    [0, 1],    # Torso bottom
    [-0.5, 1.5], [-0.5, 1],  # Left shoulder, elbow
    [0.5, 1.5], [0.5, 1],    # Right shoulder, elbow
    [-0.5, 0.5], [0.5, 0.5],  # Left hip, right hip
    [-0.5, 0], [0.5, 0],      # Left knee, right knee
    [-0.5, -0.5], [0.5, -0.5], # Left ankle, right ankle
    [0.7, 1], [0.9, 1.2], [1.1, 0.9]  # Right hand (waving)
])

# Create scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation function
def update(frame):
    positions = initial_positions.copy()
    # Simulate waving motion for the right hand (points 10, 11, 12)
    angle = np.sin(frame * 0.2) * 0.3  # Smooth waving motion
    positions[10] = [0.7 + np.cos(angle) * 0.2, 1 + np.sin(angle) * 0.2]
    positions[11] = [0.9 + np.cos(angle + 0.5) * 0.2, 1.2 + np.sin(angle + 0.5) * 0.2]
    positions[12] = [1.1 + np.cos(angle + 1) * 0.2, 0.9 + np.sin(angle + 1) * 0.2]
    
    # Slight natural movement for other joints
    for i in range(len(positions)):
        if i not in [10, 11, 12]:  # Exclude waving hand points
            positions[i, 1] += np.sin(frame * 0.1 + i * 0.2) * 0.05  # Subtle up-down motion
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
