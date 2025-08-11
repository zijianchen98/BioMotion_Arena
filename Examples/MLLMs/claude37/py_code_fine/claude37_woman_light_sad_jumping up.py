
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
duration = 200  # milliseconds
frames = 60  # Number of frames in the animation

# Create basic joint positions (x, y) for a sad woman in a jumping motion
def create_joint_positions(frame):
    # Define static base positions
    base_positions = np.array([
        [0, 0],  # center point for hips
        [-0.1, -0.1], [0.1, -0.1],  # knees
        [-0.15, -0.25], [0.15, -0.25],  # ankles
        [-0.05, 0.05], [0.05, 0.05],  # arms
        [-0.05, 0.15], [0.05, 0.15],  # shoulders
        [0, 0.25],  # head
        # total 15 points
    ])

    # Create upward motion for the jump
    amp = 0.25  # Amplitude of the jump
    y_offset = amp * np.sin(np.pi * frame / (frames / 2))

    # Update positions
    positions = base_positions + np.array([0, y_offset])
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_facecolor('black')

# Create white points (lights)
points, = ax.plot([], [], 'o', color='white')

# Initialize the points
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    positions = create_joint_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=duration/frames)

# Show the animation
plt.show()
