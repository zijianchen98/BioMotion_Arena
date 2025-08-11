
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the sad woman's joints
joints = np.array([
    [0.5, 0.5],  # Head
    [0.4, 0.6],  # Left shoulder
    [0.6, 0.6],  # Right shoulder
    [0.4, 0.4],  # Left elbow
    [0.6, 0.4],  # Right elbow
    [0.4, 0.2],  # Left wrist
    [0.6, 0.2],  # Right wrist
    [0.5, 0.8],  # Hip
    [0.4, 0.7],  # Left knee
    [0.6, 0.7],  # Right knee
    [0.4, 0.5],  # Left ankle
    [0.6, 0.5],  # Right ankle
    [0.3, 0.4],  # Left toe
    [0.7, 0.4],  # Right toe
    [0.5, 0.9]   # Body
])

# Define the animation frames
frames = 100
animation_joints = np.zeros((frames, 15, 2))

# Simulate the lying down action
for i in range(frames):
    angle = i / frames * np.pi
    animation_joints[i] = joints + np.array([
        [0, 0],  # Head
        [-0.1 * np.sin(angle), -0.1 * np.cos(angle)],  # Left shoulder
        [0.1 * np.sin(angle), -0.1 * np.cos(angle)],  # Right shoulder
        [-0.2 * np.sin(angle), -0.2 * np.cos(angle)],  # Left elbow
        [0.2 * np.sin(angle), -0.2 * np.cos(angle)],  # Right elbow
        [-0.3 * np.sin(angle), -0.3 * np.cos(angle)],  # Left wrist
        [0.3 * np.sin(angle), -0.3 * np.cos(angle)],  # Right wrist
        [0, 0],  # Hip
        [-0.1 * np.sin(angle), 0.1 * np.cos(angle)],  # Left knee
        [0.1 * np.sin(angle), 0.1 * np.cos(angle)],  # Right knee
        [-0.2 * np.sin(angle), 0.2 * np.cos(angle)],  # Left ankle
        [0.2 * np.sin(angle), 0.2 * np.cos(angle)],  # Right ankle
        [-0.3 * np.sin(angle), 0.3 * np.cos(angle)],  # Left toe
        [0.3 * np.sin(angle), 0.3 * np.cos(angle)],  # Right toe
        [0, -0.1 * np.sin(angle)]  # Body
    ])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Function to update the plot for each frame
def update(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.scatter(animation_joints[frame, :, 0], animation_joints[frame, :, 1], c='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

plt.show()
