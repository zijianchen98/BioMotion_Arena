
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
num_frames = 100
duration = 5  # duration in seconds
fps = num_frames / duration

# Points for a sad man's walking motion
# These coordinates simulate the limbs of a 'sad man' walking
# Initial positions of the points (head, body, arms, legs)
initial_positions = np.array([
    [0, 1.5],   # Head
    [0, 0.5],   # Body
    [-0.5, 1],  # Left arm
    [0.5, 1],   # Right arm
    [-0.3, 0],  # Left leg upper
    [0.3, 0],   # Right leg upper
    [-0.3, -1], # Left leg lower
    [0.3, -1],  # Right leg lower
    [0.5, 0],   # Right foot
    [-0.5, 0],  # Left foot
    [0, 0.8],   # Upper body
    [0, 0.3],   # Middle body
    [0, -0.5],  # Lower body
    [0.2, 0.8], # Right shoulder
    [-0.2, 0.8],# Left shoulder
    [0, 0]      # Center of mass
]).T

# Function to calculate walking motion
def get_positions(step):
    """Calculate the positions for each frame."""
    theta = np.pi / 20 * step  # phase for sine wave motion
    # Simulate a simple walking motion using sine and cosine
    offsets = np.array([
        [0, 1.5],  # Head
        [0, 0.5],  # Body
        [-0.5 + 0.1 * np.sin(theta), 1],  # Left arm
        [0.5 - 0.1 * np.sin(theta), 1],   # Right arm
        [-0.3 + 0.1 * np.cos(theta), 0],  # Left leg upper
        [0.3 - 0.1 * np.cos(theta), 0],   # Right leg upper
        [-0.3 + 0.1 * np.sin(theta), -1], # Left leg lower
        [0.3 - 0.1 * np.sin(theta), -1],  # Right leg lower
        [0.5, 0], # Right foot
        [-0.5, 0],# Left foot
        [0, 0.8], # Upper body
        [0, 0.3], # Middle body
        [0, -0.5],# Lower body
        [0.2, 0.8],# Right shoulder
        [-0.2, 0.8],# Left shoulder
        [0, 0],   # Center of mass
    ]).T
    return initial_positions + offsets

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor("black")
points, = ax.plot([], [], 'o', color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Update function for the animation
def update(frame):
    positions = get_positions(frame)
    points.set_data(positions[0], positions[1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init,
                              blit=True, interval=1000/fps)

# Show the animation
plt.show()
