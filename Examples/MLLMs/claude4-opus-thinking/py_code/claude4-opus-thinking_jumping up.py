
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters
num_points = 15
frames = 60
jump_height = 1.5

# Define point positions relative to the jumping motion
# Initial positions of the point-lights (head, arms, torso, legs)
initial_positions = np.array([
    [0, 1],   # Head
    [-0.2, 0.75], [0.2, 0.75],  # Shoulders
    [-0.3, 0.5], [0.3, 0.5],  # Elbows
    [0, 0.5],  # Torso Center
    [-0.25, 0.25], [0.25, 0.25],  # Hips
    [-0.3, 0], [0.3, 0],  # Knees
    [-0.3, -0.25], [0.3, -0.25],  # Feet
    [0, -0.5]   # Ground Level
])

# Function to update the positions for animation
def update(frame):
    plt.clf()
    # Calculate the vertical position for the jump
    vertical_offset = jump_height * np.sin(np.pi * frame / (frames // 2))
    
    # Adjust positions
    animated_positions = initial_positions.copy()
    animated_positions[:, 1] += vertical_offset
    
    # Set the limits and style
    plt.xlim(-1, 1)
    plt.ylim(-1, 2)
    plt.axis('off')  # Hide axes
    plt.scatter(animated_positions[:, 0], animated_positions[:, 1], color='white', s=100)  # Plot points

# Create figure to display
fig = plt.figure()
plt.style.use('dark_background')

# Animate
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

# Show animation
plt.show()
