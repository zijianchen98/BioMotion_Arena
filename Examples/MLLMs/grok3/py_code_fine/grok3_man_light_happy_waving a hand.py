
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a human figure (waving hand)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, and hand points
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8],  # left shoulder
    [2, 8],   # right shoulder
    [-3, 6],  # left elbow
    [3, 6],   # right elbow
    [-4, 4],  # left wrist
    [4, 4],   # right wrist (waving hand starts here)
    [-1, 7],  # left hip
    [1, 7],   # right hip
    [-1, 4],  # left knee
    [1, 4],   # right knee
    [-1, 1],  # left ankle
    [1, 1],   # right ankle
    [4.5, 3], # right hand extra point 1
    [4.5, 5]  # right hand extra point 2
]) * 10  # Scale up for visibility

# Number of frames for the animation
n_frames = 100

# Function to update positions for waving motion
def update(frame):
    positions = initial_positions.copy()
    # Waving motion for right hand (wrist and extra points)
    angle = np.sin(frame * 0.1) * 0.5  # Smooth waving motion
    rot = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle), np.cos(angle)]])
    hand_offset = np.array([4, 4]) * 10
    positions[5] = hand_offset + rot.dot(initial_positions[5] - hand_offset)  # right wrist
    positions[13] = hand_offset + rot.dot(initial_positions[13] - hand_offset)  # hand point 1
    positions[14] = hand_offset + rot.dot(initial_positions[14] - hand_offset)  # hand point 2
    
    # Slight natural movement for other joints
    for i in range(len(positions)):
        if i not in [5, 13, 14]:  # Exclude waving hand points
            positions[i] += np.array([0, 0.1 * np.sin(frame * 0.05 + i)])  # Subtle up-down motion
    
    scat.set_offsets(positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-60, 60)
ax.set_ylim(-10, 110)
ax.axis('off')

# Plot the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
