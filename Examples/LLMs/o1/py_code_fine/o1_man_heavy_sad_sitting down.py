import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 30

# Define 15 keypoints for a standing posture (x, y)
start_points = np.array([
    [0.00,  0.40],  # Head
    [0.00,  0.30],  # Neck
    [0.00,  0.20],  # Chest
    [-0.10, 0.18],  # Left Shoulder
    [0.10,  0.18],  # Right Shoulder
    [-0.20, 0.10],  # Left Elbow
    [0.20,  0.10],  # Right Elbow
    [-0.30, 0.00],  # Left Hand
    [0.30,  0.00],  # Right Hand
    [0.00,  0.10],  # Mid-spine
    [0.00, -0.10],  # Pelvis
    [-0.05, -0.30], # Left Knee
    [0.05,  -0.30], # Right Knee
    [-0.05, -0.50], # Left Foot
    [0.05,  -0.50], # Right Foot
])

# Define 15 keypoints for a sitting posture (x, y), with a slight forward slump for a "sad" appearance
end_points = np.array([
    [0.05,  0.18],  # Head
    [0.05,  0.10],  # Neck
    [0.00,  0.00],  # Chest
    [-0.10, 0.00],  # Left Shoulder
    [0.10,  0.00],  # Right Shoulder
    [-0.20, -0.05], # Left Elbow
    [0.20,  -0.05], # Right Elbow
    [-0.30, -0.10], # Left Hand
    [0.30,  -0.10], # Right Hand
    [0.00,  -0.10], # Mid-spine
    [0.00,  -0.30], # Pelvis
    [-0.05, -0.45], # Left Knee
    [0.05,  -0.45], # Right Knee
    [-0.05, -0.60], # Left Foot
    [0.05,  -0.60], # Right Foot
])

# Generate a linear interpolation between start_points and end_points
def interpolate_points(start, end, t):
    return start + t * (end - start)

# Prepare the figure
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.7, 0.5)
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], c='white', s=50)

# Update function for animation
def update(frame):
    t = frame / (num_frames - 1)
    current_positions = interpolate_points(start_points, end_points, t)
    scatter.set_offsets(current_positions)
    return scatter,

# Create animation
ani = FuncAnimation(
    fig, update, frames=num_frames, interval=100, blit=True, repeat=True
)

plt.show()