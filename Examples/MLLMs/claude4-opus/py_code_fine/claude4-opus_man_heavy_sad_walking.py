
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration for the animation
NUM_POINTS = 15
FRAMES = 100
FPS = 30
WEIGHT_Y = -0.5  # Y-position of the weight

# Define the initial positions of the points representing the sad man
# Positions are set to represent a simple walking pattern
initial_positions = np.array([
    [0, 1],     # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.4, 0.2], [0.4, 0.2],  # Elbows
    [-0.3, 0], [0.3, 0],      # Hands
    [-0.2, -1], [0.2, -1],    # Knees
    [-0.1, -2], [0.1, -2],    # Feet (static)
    [0, WEIGHT_Y]              # Weight
])

def update_positions(frame):
    """Update the positions of the points to create a walking effect."""
    # Simple walking motion
    displacement = np.sin(np.linspace(0, 2 * np.pi * frame / FRAMES, NUM_POINTS))
    y_positions = initial_positions[:, 1] + displacement * 0.1  # Oscillation effect
    new_positions = np.column_stack((initial_positions[:, 0], y_positions))
    
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 2)
    ax.set_facecolor('black')

    # Plot all points
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

# Create a figure for the animation
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.set_facecolor('black')

# Creating the animation
ani = animation.FuncAnimation(fig, update_positions, frames=FRAMES, interval=1000/FPS)

# Show the animation
plt.show()
