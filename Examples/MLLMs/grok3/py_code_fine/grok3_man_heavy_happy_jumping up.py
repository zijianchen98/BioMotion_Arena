
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights (simplified human figure)
# 15 points: head, torso (3 points), shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],    # head
    [0, 6],     # torso top
    [0, 2],     # torso bottom
    [-2, 6],    # left shoulder
    [-4, 4],    # left elbow
    [-6, 2],    # left wrist
    [2, 6],     # right shoulder
    [4, 4],     # right elbow
    [6, 2],     # right wrist
    [-1, 0],    # left hip
    [-1, -4],   # left knee
    [-1, -8],   # left ankle
    [1, 0],     # right hip
    [1, -4],    # right knee
    [1, -8]     # right ankle
])

# Number of frames for the animation
n_frames = 100

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Scatter plot for point-lights
points, = ax.plot([], [], 'w.', markersize=10)

# Function to update positions for waving motion
def update(frame):
    # Base positions with slight oscillation for natural movement
    positions = initial_positions.copy()
    
    # Waving motion for right arm (right wrist, elbow, shoulder)
    angle = np.sin(2 * np.pi * frame / n_frames) * 0.5  # Smooth waving
    positions[8] = [6 + 2 * angle, 2]  # right wrist
    positions[7] = [4 + 1.5 * angle, 4]  # right elbow
    positions[6] = [2 + 0.5 * angle, 6]  # right shoulder
    
    # Slight torso and leg movement for realism
    positions[1:3] += np.array([0, 0.1 * np.sin(2 * np.pi * frame / n_frames)])  # torso
    positions[9:15] += np.array([0, 0.05 * np.sin(2 * np.pi * frame / n_frames)])  # legs
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
