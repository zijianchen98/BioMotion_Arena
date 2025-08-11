
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define point locations for skeleton
# The points represent major joints of the human body
# Define keypoints of a human figure turning around (biological motion)
initial_positions = np.array([
    [0, 4],  # Head
    [-0.5, 3], [0.5, 3],  # Shoulders Left & Right
    [-1, 2], [1, 2],  # Elbow Left & Right
    [-1.5, 1], [1.5, 1],  # Hand Left & Right
    [0, 2],  # Spine
    [-0.5, 0], [0.5, 0],  # Hip Left & Right
    [-1, -1], [1, -1],  # Knee Left & Right
    [-1, -2], [1, -2],  # Foot Left & Right
    [0, 3]  # Center of Chest
])

# Function to simulate turning around motion
def generate_animation_frame(frame_number, positions, total_frames):
    angle = (frame_number / total_frames) * 2 * np.pi  # Full rotation over total_frames
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_positions = np.dot(positions, rotation_matrix.T)
    return rotated_positions

# Parameters for animation
frames = 150  # Number of frames for a full turn
frame_interval = 50  # Duration between frames in milliseconds

# Plotting the animation
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 5)
ax.set_facecolor('black')
ax.axis('off')  # Turn off axis lines for better visibility

# Initialize scatter plot for points
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

def update(frame):
    updated_positions = generate_animation_frame(frame, initial_positions, frames)
    points.set_offsets(updated_positions)
    return points, 

ani = FuncAnimation(fig, update, frames=frames, interval=frame_interval, blit=True)
plt.show()
