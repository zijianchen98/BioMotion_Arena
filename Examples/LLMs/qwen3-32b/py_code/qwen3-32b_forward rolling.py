
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Define the joints of a human body for biological motion
joint_names = [
    "Pelvis", "Left Hip", "Right Hip", "Spine", "Left Knee", "Right Knee",
    "Thorax", "Left Ankle", "Right Ankle", "Neck", "Left Wrist", "Right Wrist",
    "Head", "Left Elbow", "Right Elbow"
]
num_joints = len(joint_names)

# Initial joint positions (in local coordinates, relative to pelvis)
initial_positions = np.array([
    [0, 0],  # Pelvis
    [-1, 1],  # Left Hip
    [1, 1],  # Right Hip
    [0, 2],  # Spine
    [-1, 3],  # Left Knee
    [1, 3],  # Right Knee
    [0, 4],  # Thorax
    [-1, 5],  # Left Ankle
    [1, 5],  # Right Ankle
    [0, 6],  # Neck
    [-1, 6],  # Left Wrist
    [1, 6],  # Right Wrist
    [0, 7],  # Head
    [-1, 6],  # Left Elbow
    [1, 6],  # Right Elbow
], dtype=float)

# Forward roll motion parameters
roll_frames = 60  # Total frames for the animation
roll_radius = 10  # Radius of the rolling circle
roll_speed = 0.1  # Speed of rolling

# Function to rotate a point around the origin
def rotate_point(point, angle):
    rot_matrix = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])
    return np.dot(rot_matrix, point)

# Generate the rolling motion
def forward_roll(t):
    angle = t * roll_speed
    center = np.array([roll_radius * math.cos(angle), roll_radius * math.sin(angle)])
    rotated_joints = np.array([rotate_point(pos, angle) for pos in initial_positions])
    return rotated_joints + center

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.axis('off')

# Create scatter plot for the point lights
scat = ax.scatter([], [], color='white', s=100)

# Animation update function
def update(frame):
    positions = forward_roll(frame)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=roll_frames, interval=50, blit=True)

# Display the animation
plt.show()
