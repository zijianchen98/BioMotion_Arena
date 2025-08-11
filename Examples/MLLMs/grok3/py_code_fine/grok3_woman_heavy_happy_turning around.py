
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human figure)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 10], [2, 8], [-2, 8], [4, 6], [-4, 6], [6, 4], [-6, 4],  # head, shoulders, elbows, wrists
    [0, 2], [1, 0], [-1, 0], [2, -2], [-2, -2], [3, -4], [-3, -4], [0, -6]  # hips, knees, ankles, torso
])

# Number of frames for one full turn (e.g., 360 degrees over 100 frames)
n_frames = 100
theta = np.linspace(0, 2 * np.pi, n_frames, endpoint=False)

# Function to update positions for turning motion
def update(frame):
    angle = theta[frame]
    # Rotate around origin for turning motion
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    new_positions = np.dot(initial_positions, rotation_matrix)
    # Add slight biomechanical adjustments for realism (e.g., arm swing)
    if angle < np.pi:
        new_positions[3:5] += np.array([0.5 * np.sin(angle), 0])  # wrists forward
        new_positions[5:7] += np.array([-0.5 * np.sin(angle), 0])  # elbows back
    else:
        new_positions[3:5] += np.array([-0.5 * np.sin(angle), 0])  # wrists back
        new_positions[5:7] += np.array([0.5 * np.sin(angle), 0])  # elbows forward
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Plot the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
