
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of points and the action
NUM_POINTS = 15
ACTION = 'bowing'
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'

# Define a biomechanically plausible motion for a person bowing
def bowing_motion(t, amplitude=0.2, frequency=0.5, speed=0.1):
    # Simulate the motion of a person bowing
    # Each point moves in a way that mimics the motion of a human body
    # Here, we use a simplified model with different parts of the body
    # For simplicity, we simulate the motion of the head, shoulders, torso, arms, and legs
    # We use sine waves with different phases and amplitudes to simulate the motion

    # Time normalization
    t_norm = t / 10.0  # Normalize time to 0-1 for the sine wave

    # Define the positions of the points (relative to the center of the body)
    # These positions are based on a simplified human body model
    positions = np.array([
        [0, 0],     # Head
        [0, 0.2],   # Upper back
        [0, 0.4],   # Mid back
        [0, 0.6],   # Lower back
        [0, 0.8],   # Hip
        [-0.3, 0.8], # Left hip
        [-0.2, 0.9], # Left knee
        [-0.1, 1.0], # Left ankle
        [0.3, 0.8],  # Right hip
        [0.2, 0.9],  # Right knee
        [0.1, 1.0],  # Right ankle
        [-0.2, 0.2], # Left shoulder
        [-0.1, 0.1], # Left elbow
        [0.1, 0.1],  # Right elbow
        [0.2, 0.2],  # Right shoulder
    ])

    # Apply the motion to each point
    # Use sine waves with different phases to simulate realistic motion
    motion = np.zeros_like(positions)
    motion[:, 0] = amplitude * np.sin(2 * np.pi * frequency * t_norm)  # Y-axis movement for head
    motion[:, 1] = amplitude * np.sin(2 * np.pi * frequency * t_norm + np.pi / 2)  # X-axis movement for torso

    # Apply motion to each point
    positions += motion * speed

    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create the points
points = [ax.scatter([], [], c=POINT_COLOR, s=50, edgecolors='none') for _ in range(NUM_POINTS)]

# Update function for animation
def update(frame):
    positions = bowing_motion(frame)
    for i, point in enumerate(points):
        point.set_offsets(positions[i])
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
