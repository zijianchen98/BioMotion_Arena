
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified humanoid structure)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-3, 6], [3, 6],  # elbows
    [-4, 4], [4, 4],  # wrists
    [0, 2], [-1, 2], [1, 2],  # hips
    [-1, 0], [0, 0], [1, 0],  # knees
    [-1, -2], [0, -2], [1, -2]  # ankles
])

# Number of frames for the animation
frames = 60
positions = np.zeros((frames, 15, 2))

# Simulate sitting down motion (simplified biomechanical movement)
for f in range(frames):
    t = f / frames  # Normalized time
    # Head and torso lowering
    positions[f, 0] = [0, 10 - 6 * t]  # Head
    positions[f, 1:3] = [[-2, 8 - 6 * t], [2, 8 - 6 * t]]  # Shoulders
    # Arms bending slightly
    positions[f, 3:5] = [[-3 + t, 6 - 2 * t], [3 - t, 6 - 2 * t]]  # Elbows
    positions[f, 5:7] = [[-4 + 1.5 * t, 4 - 2 * t], [4 - 1.5 * t, 4 - 2 * t]]  # Wrists
    # Hips lowering and legs bending
    positions[f, 7:10] = [[0, 2 - 6 * t], [-1, 2 - 6 * t], [1, 2 - 6 * t]]  # Hips
    positions[f, 10:13] = [[-1 + 0.5 * t, 0 - 4 * t], [0, 0 - 4 * t], [1 - 0.5 * t, 0 - 4 * t]]  # Knees
    positions[f, 13:] = [[-1, -2 - 2 * t], [0, -2 - 2 * t], [1, -2 - 2 * t]]  # Ankles

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 15)
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Display animation
plt.show()
