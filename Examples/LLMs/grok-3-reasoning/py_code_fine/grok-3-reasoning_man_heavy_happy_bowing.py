
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Define the initial positions (standing pose)
# For simplicity, we'll approximate positions. In a real scenario, these might be based on actual human proportions.
# Let's assume points: head, neck, left shoulder, left elbow, left wrist, right shoulder, right elbow, right wrist,
#                     spine base, left hip, left knee, left ankle, right hip, right knee, right ankle
initial_positions = np.array([
    [0, 1.8],  # head
    [0, 1.6],  # neck
    [-0.2, 1.5],  # left shoulder
    [-0.3, 1.3],  # left elbow
    [-0.4, 1.1],  # left wrist
    [0.2, 1.5],  # right shoulder
    [0.3, 1.3],  # right elbow
    [0.4, 1.1],  # right wrist
    [0, 1.4],  # spine base
    [-0.1, 1.2],  # left hip
    [-0.1, 0.8],  # left knee
    [-0.1, 0.4],  # left ankle
    [0.1, 1.2],  # right hip
    [0.1, 0.8],  # right knee
    [0.1, 0.4]   # right ankle
])

# Define the bowed positions
# For bowing, the upper body bends forward. We'll rotate the upper body points around the spine base.
bow_angle = np.pi / 4  # 45 degrees
rotation_center = initial_positions[8]  # spine base

# Function to rotate points
def rotate_points(points, angle, center):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    return center + (points - center) @ rotation_matrix.T

# Upper body points: head, neck, shoulders, elbows, wrists
upper_body_indices = [0, 1, 2, 3, 4, 5, 6, 7]
bowed_positions = initial_positions.copy()
bowed_positions[upper_body_indices] = rotate_points(initial_positions[upper_body_indices], bow_angle, rotation_center)

# Number of frames for the animation
num_frames = 30

# Interpolate positions between standing and bowed
def interpolate_positions(frame):
    t = frame / (num_frames - 1)
    return (1 - t) * initial_positions + t * bowed_positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Update function for animation
def update(frame):
    positions = interpolate_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
anim = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()
