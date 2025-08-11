
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Define initial positions for 15 point-lights (simplified human model)
# Head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 0.8],  # Head
    [-0.2, 0.6], [0.2, 0.6],  # Shoulders
    [-0.4, 0.4], [0.4, 0.4],  # Elbows
    [-0.6, 0.2], [0.6, 0.2],  # Wrists
    [0, 0],  # Hips
    [-0.2, -0.2], [0.2, -0.2],  # Knees
    [-0.3, -0.5], [0.3, -0.5],  # Ankles
    [-0.1, 0.3], [0.1, 0.3],  # Torso points
    [0, 0.5], [0, 0.1]  # Additional torso points
])

# Normalize positions to fit within [-1, 1]
positions = initial_positions / np.max(np.abs(initial_positions))

# Scatter plot for point-lights
scatter = ax.scatter(positions[:, 0], positions[:, 15], c='white', s=50)

# Animation function
def update(frame):
    # Simulate turning around (simple rotation)
    angle = np.radians(frame * 5)  # 5 degrees per frame
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    new_positions = np.dot(positions - [0, 0], rotation_matrix) + [0, 0]
    
    # Ensure biomechanical plausibility (keep limbs proportional)
    # Adjust for natural movement (e.g., arms and legs swing)
    if frame % 20 < 10:
        new_positions[4:6] += [0.1 * np.sin(angle), 0]  # Wrists swing
        new_positions[6:8] += [-0.1 * np.sin(angle), 0]  # Knees swing
    else:
        new_positions[4:6] += [-0.1 * np.sin(angle), 0]  # Reverse swing
        new_positions[6:8] += [0.1 * np.sin(angle), 0]
    
    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(72), interval=50, blit=True)

# Save or display animation
plt.show()
# ani.save('biological_motion.gif', writer='pillow')
