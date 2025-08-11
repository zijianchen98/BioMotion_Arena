
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human body in sitting posture)
# Points: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-3, 6], [3, 6],  # elbows
    [-4, 4], [4, 4],  # wrists
    [0, 2],  # hips
    [-1, 0], [1, 0],  # knees
    [-2, -2], [2, -2]  # ankles
])

# Number of frames for the animation
n_frames = 60
positions = np.zeros((n_frames, 15, 2))

# Simulate sitting down motion (simplified biomechanically plausible movement)
for i in range(n_frames):
    t = i / (n_frames - 1)  # Normalized time (0 to 1)
    # Head moves slightly down
    positions[i, 0] = [0, 10 - 2 * t]
    # Shoulders move down and slightly inward
    positions[i, 1] = [-2 + t, 8 - 4 * t]
    positions[i, 2] = [2 - t, 8 - 4 * t]
    # Elbows follow shoulders and bend
    positions[i, 3] = [-3 + 0.5 * t, 6 - 3 * t]
    positions[i, 4] = [3 - 0.5 * t, 6 - 3 * t]
    # Wrists follow elbows
    positions[i, 5] = [-4 + t, 4 - 2 * t]
    positions[i, 6] = [4 - t, 4 - 2 * t]
    # Hips move down
    positions[i, 7] = [0, 2 - 6 * t]
    # Knees bend and move down
    positions[i, 8] = [-1 + 0.5 * t, 0 - 4 * t]
    positions[i, 9] = [1 - 0.5 * t, 0 - 4 * t]
    # Ankles follow knees
    positions[i, 10] = [-2 + t, -2 - 2 * t]
    positions[i, 11] = [2 - t, -2 - 2 * t]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-6, 6)
ax.set_ylim(-4, 12)
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
