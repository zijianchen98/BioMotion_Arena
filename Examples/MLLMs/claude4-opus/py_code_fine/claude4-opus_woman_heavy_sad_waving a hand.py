
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define constants
NUM_POINTS = 15  # Number of points
WAVE_DURATION = 100  # Duration of the wave in frames
FPS = 30  # Frames per second

# Define the points' initial positions (x, y)
# Rough estimate of key body joints in a 2D plane
joint_positions = np.array([
    [0, 0],   # Head
    [-0.2, -0.3], # Left shoulder
    [0.2, -0.3],  # Right shoulder
    [-0.3, -0.5], # Left elbow
    [0.3, -0.5],  # Right elbow
    [-0.4, -0.7], # Left wrist
    [0.4, -0.7],  # Right wrist
    [0, -1.0],    # Torso
    [-0.2, -1.2], # Left hip
    [0.2, -1.2],  # Right hip
    [-0.2, -1.5], # Left knee
    [0.2, -1.5],  # Right knee
    [-0.2, -1.8], # Left ankle
    [0.2, -1.8],  # Right ankle
    [-0.1, -0.4], # Left hand (for waving)
    [0.1, -0.4]   # Right hand (for waving)
])

# Define the waving motion for the right wrist
def wave_motion(frame):
    return 0.1 * np.sin(frame / 5)  # Waving motion

# Create a figure and axis
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 1)
ax.axis('off')  # Turn off the axes

# Create scatter points for animation
points, = ax.plot([], [], 'wo', markersize=10)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    # Update the right wrist position based on waving
    joint_positions[6, 0] = 0.4 + wave_motion(frame)  # Right wrist X position
    joint_positions[6, 1] = -0.7 + wave_motion(frame)  # Right wrist Y position
    points.set_data(joint_positions[:, 0], joint_positions[:, 1])
    return points,

# Create an animation
ani = FuncAnimation(fig, update, frames=np.arange(0, WAVE_DURATION), init_func=init, blit=True, interval=1000/FPS)

# Display the animation
plt.show()
