
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the skeleton of the sadman using point-light markers
# These positions are normalized and represent relative coordinates for the human body
point_connections = [
    (0, 1), (1, 2), (2, 3), (3, 4),       # Spine and head
    (1, 5), (5, 6),                       # Left arm
    (1, 7), (7, 8),                       # Right arm
    (3, 9), (9, 10),                      # Left leg
    (3, 11), (11, 12),                    # Right leg
    (6, 13), (8, 13),                     # Arms meeting in midair
    (10, 14), (12, 14)                    # Legs meeting in midair
]

# Relative point positions (15 points: head, torso, arms, legs)
# These positions will be used as reference for movement
base_positions = np.array([
    [0, 1],      # Head
    [0, 0.75],   # Upper torso
    [0, 0.5],    # Mid torso
    [0, 0.25],   # Lower torso
    [0, 0],      # Pelvis
    [-0.25, 0.75], # Left shoulder
    [-0.5, 0.5], # Left elbow
    [0.25, 0.75], # Right shoulder
    [0.5, 0.5],  # Right elbow
    [-0.15, 0],  # Left hip
    [-0.3, -0.25], # Left knee
    [0.15, 0],    # Right hip
    [0.3, -0.25], # Right knee
    [0, 1.1],     # Overhead meeting point (at the highest point while jumping)
    [0, -0.35]    # Feet meeting point (when legs contract at midair)
])

# Function to create jumping motion
def generate_jump_motion(base_pts, num_frames, jump_height):
    frames = []
    for i in range(num_frames):
        t = i / num_frames
        vertical_displacement = jump_height * np.sin(np.pi * t) # Smooth jump arch
        motion = base_pts.copy()

        # Apply vertical displacement
        motion[:, 1] += vertical_displacement
        # Add leg and arm contraction/extensions during jumping motion
        compression = 0.2 * np.sin(2 * np.pi * t)
        motion[10, 1] += compression
        motion[12, 1] += compression
        motion[6, 0] += compression
        motion[8, 0] -= compression

        frames.append(motion)
    return frames

# Generate the motion data
num_frames = 60
jump_height = 0.5
motion_frames = generate_jump_motion(base_positions, num_frames, jump_height)

# Set up the figure for animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_facecolor("black")
ax.axis('off')

points, = ax.plot([], [], 'wo', markersize=8) # White points (markers)

# Function to initialize the frame
def init():
    points.set_data([], [])
    return points,

# Function to update the frame
def update(frame):
    positions = motion_frames[frame]
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=30)

plt.show()
