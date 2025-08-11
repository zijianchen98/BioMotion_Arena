
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of 15 point-lights (simplified human skeleton for sitting motion)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [-2, 8],  # left shoulder, right shoulder
    [-4, 6], [0, 6],  # left elbow, right elbow
    [-6, 4], [2, 4],  # left wrist, right wrist
    [0, 0], [0, 0],  # left hip, right hip
    [-2, -2], [2, -2],  # left knee, right knee
    [-2, -4], [2, -4],  # left ankle, right ankle
    [0, 4], [0, 2]   # torso points
])

# Number of frames for the animation
frames = 60
positions = np.zeros((frames, 15, 2))

# Simulate sitting down motion (simplified biomechanical movement)
for f in range(frames):
    t = f / frames  # Normalize time from 0 to 1
    # Head and torso move slightly down
    positions[f, 0] = [0, 10 - 6 * t]  # head
    positions[f, 9] = [0, 4 - 3 * t]  # torso upper
    positions[f, 10] = [0, 2 - 2 * t]  # torso lower
    # Shoulders follow torso
    positions[f, 1] = [-2, 8 - 3 * t]  # left shoulder
    positions[f, 2] = [2, 8 - 3 * t]   # right shoulder
    # Arms bend naturally
    positions[f, 3] = [-4 + 2 * t, 6 - 2 * t]  # left elbow
    positions[f, 4] = [4 - 2 * t, 6 - 2 * t]   # right elbow
    positions[f, 5] = [-6 + 3 * t, 4 - 2 * t]  # left wrist
    positions[f, 6] = [6 - 3 * t, 4 - 2 * t]   # right wrist
    # Hips move down and slightly back
    positions[f, 7] = [-2 * t, -2 * t]  # left hip
    positions[f, 8] = [2 * t, -2 * t]   # right hip
    # Knees bend
    positions[f, 11] = [-2 - 1 * t, -2 - 2 * t]  # left knee
    positions[f, 12] = [2 + 1 * t, -2 - 2 * t]   # right knee
    # Ankles move down
    positions[f, 13] = [-2, -4 - 2 * t]  # left ankle
    positions[f, 14] = [2, -4 - 2 * t]   # right ankle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-6, 12)
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
