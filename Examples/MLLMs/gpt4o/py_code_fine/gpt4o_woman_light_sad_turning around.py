
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define parameters for the point-light animation
num_frames = 100  # number of animation frames
num_points = 15   # number of points in the biological motion
background_color = 'black'
point_color = 'white'
figure_size = (6, 12)

# Function to generate biomechanically plausible motion (turning around)
def generate_biological_motion(num_points, num_frames):
    """
    Simulate the motion of point-lights representing a person turning around.
    """
    # Define reference structure for a human-like skeleton (e.g., torso, limbs, head)
    skeleton = np.array([
        [0, 1],  # Head
        [0, 0.8], [0, 0.6], [0, 0.4], [0, 0.2], [0, 0],  # Spine / torso
        [-0.1, 0.6], [0.1, 0.6],  # Shoulders
        [-0.2, 0.4], [0.2, 0.4],  # Elbows
        [-0.3, 0.2], [0.3, 0.2],  # Hands
        [-0.1, -0.2], [0.1, -0.2],  # Thighs
        [-0.2, -0.6], [0.2, -0.6],  # Knees
        [-0.1, -1], [0.1, -1]  # Feet
    ])

    skeleton = skeleton[:num_points]

    motion_frames = []
    for i in range(num_frames):
        angle = (i / num_frames) * 360  # Turning around
        rotation_matrix = np.array([
            [np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
            [np.sin(np.radians(angle)), np.cos(np.radians(angle))]
        ])
        transformed_skeleton = skeleton @ rotation_matrix.T
        motion_frames.append(transformed_skeleton)
    
    return np.array(motion_frames)

# Generate motion data
motion_data = generate_biological_motion(num_points, num_frames)

# Initialize plot
fig, ax = plt.subplots(figsize=figure_size)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor(background_color)
ax.axis('off')
points, = ax.plot([], [], 'o', color=point_color, markersize=8)

# Update function for animation
def update(frame):
    positions = motion_data[frame]
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

# Display animation
plt.show()
