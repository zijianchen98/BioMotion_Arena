
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point lights
NUM_LIGHTS = 15

# Define the action: a happy woman with heavy weight lying down
# We'll simulate the motion of 15 joints (e.g., body parts) as point lights

# Define the joints and their positions (simplified for a human body)
# This is a basic skeleton with 15 joints, representing a person lying down
# Positions are in 2D (x, y), with origin at the center of the body

# Initial positions (simplified for a person lying down)
initial_positions = np.array([
    [0, 0],      # Hip
    [1, 0],      # Right thigh
    [1.5, 0.5],  # Right knee
    [1.2, 1.0],  # Right ankle
    [0, 0],      # Left thigh
    [-1, 0],     # Left thigh
    [-1.5, 0.5], # Left knee
    [-1.2, 1.0], # Left ankle
    [0, 0],      # Spine
    [0.5, 0.5],  # Upper back
    [0, 1.0],    # Head
    [0.3, 0.8],  # Right shoulder
    [0.5, 0.6],  # Right elbow
    [-0.3, 0.8], # Left shoulder
    [-0.5, 0.6], # Left elbow
])

# Define a function to simulate motion over time
def animate(t):
    # Simulate a smooth lying down motion
    # We'll interpolate between initial positions and a final lying down position
    # For simplicity, we'll use a sine wave to simulate the motion
    # We'll also simulate a bit of randomness to make it more natural

    # Final positions when lying down
    final_positions = np.array([
        [0, 0],      # Hip
        [1, 0.5],    # Right thigh
        [1.5, 1.0],  # Right knee
        [1.2, 1.5],  # Right ankle
        [0, 0],      # Left thigh
        [-1, 0.5],   # Left thigh
        [-1.5, 1.0], # Left knee
        [-1.2, 1.5], # Left ankle
        [0, 0],      # Spine
        [0.5, 0.5],  # Upper back
        [0, 1.0],    # Head
        [0.3, 0.8],  # Right shoulder
        [0.5, 0.6],  # Right elbow
        [-0.3, 0.8], # Left shoulder
        [-0.5, 0.6], # Left elbow
    ])

    # Interpolate between initial and final positions
    positions = initial_positions * (1 - t) + final_positions * t

    # Add some small random perturbations to make motion more natural
    noise = np.random.normal(0, 0.1, positions.shape)
    positions += noise

    # Update the positions of the point lights
    for i, circle in enumerate(circles):
        circle.set_center(positions[i])

    return circles

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Solid black background
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
circles = [Circle((0, 0), 0.05, color='white') for _ in range(NUM_LIGHTS)]
for circle in circles:
    ax.add_patch(circle)

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=50, blit=True, repeat=True
)

plt.show()
