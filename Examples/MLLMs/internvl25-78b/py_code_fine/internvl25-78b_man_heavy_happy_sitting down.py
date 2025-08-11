
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define joint positions for a standing pose
def initial_pose():
    return np.array([
        [0, 10],  # Head
        [0, 8],   # Neck
        [-1, 6],  # Left shoulder
        [1, 6],   # Right shoulder
        [-2, 4],  # Left elbow
        [2, 4],   # Right elbow
        [-3, 2],  # Left hand
        [3, 2],   # Right hand
        [0, 6],   # Spine
        [0, 4],   # Waist
        [-1, 2],  # Left hip
        [1, 2],   # Right hip
        [-2, 0],  # Left knee
        [2, 0],   # Right knee
        [-3, -2], # Left foot
        [3, -2],  # Right foot
    ])

# Function to simulate sitting down motion
def sitting_motion(frame, points):
    # Calculate the sitting motion over 60 frames
    frames = 60
    y_scale = np.linspace(1, 0.5, frames)
    y_shift = np.linspace(0, -5, frames)
    
    if frame < frames:
        scale = y_scale[frame]
        shift = y_shift[frame]
        points[:, 1] = initial_positions[:, 1] * scale + shift

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 12)
ax.set_facecolor('black')

points, = ax.plot([], [], 'o', color='white')

initial_positions = initial_pose()

# Animation update function
def update(frame):
    sitting_motion(frame, points.set_data(initial_positions[:, 0], initial_positions[:, 1]))
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=50, blit=True)

plt.axis('off')
plt.show()
