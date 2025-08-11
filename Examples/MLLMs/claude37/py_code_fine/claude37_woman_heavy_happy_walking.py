
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15  # Number of point lights
FRAME_RATE = 30  # Animation frame rate
WALK_CYCLES = 2  # Number of walk cycles
DURATION = WALK_CYCLES * 60  # Duration of the animation in frames

# Point-light positions (simplified for animation)
points = np.array([
    [0, 2],   # Head
    [-1, 1],  # Left shoulder
    [1, 1],   # Right shoulder
    [-1.5, 0],  # Left hand
    [1.5, 0],   # Right hand
    [0, 0],   # Torso
    [-1, -1],  # Left knee
    [1, -1],   # Right knee
    [-1, -2],  # Left foot
    [1, -2],   # Right foot
    [0, 1.5],  # Mid torso (for balance)
    [-1, 0.5], # Left thigh
    [1, 0.5],  # Right thigh
    [-0.5, 0], # Mid-left
    [0.5, 0],  # Mid-right
    [0, -1]    # Lower torso (for realism)
])

# Walker's walking motion parameters
def walking_motion(frame):
    # Create a walking pattern using sine
    offset = np.sin((frame / DURATION) * (2 * np.pi) * 2)  # Two cycles
    new_points = points.copy()
    new_points[:, 1] = points[:, 1] + offset  # Shift up/down
    new_points[:, 0] += (frame / FRAME_RATE * 0.1)  # Move forward
    return new_points

# Set up the figure for the animation
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
points_plot = ax.scatter([], [], s=100, color='white')

# Update function for the animation
def update(frame):
    new_points = walking_motion(frame)
    points_plot.set_offsets(new_points)
    return points_plot,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=DURATION, blit=True, interval=1000/FRAME_RATE)

# Show the animation
plt.show()
