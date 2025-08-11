
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize parameters
num_points = 15
duration = 5  # duration of the animation in seconds
fps = 30      # frames per second
frames = duration * fps

# Creating a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.set_xticks([])  # Remove x ticks
ax.set_yticks([])  # Remove y ticks

# Initialize positions of the point lights
# Simulating a sad woman with heavy weight jumping forward
initial_positions = np.array([
    [0, 0],  # Center
    [0.5, 1], [1, 0.5], [-0.5, 1], [-1, 0.5],  # Upper body
    [0.5, -1], [-1, -1], [-0.5, -1], [1, -1],  # Lower body
    [0.2, -2], [-0.2, -2], [0.2, -2.5], [-0.2, -2.5],  # Legs
    [0.5, -0.5], [-0.5, -0.5], [1, -1.5], [-1, -1.5]  # Interaction with weight
])

# Define the update function for animation
def update(frame):
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_facecolor('black')
    
    # Calculate new positions based on frame
    time = frame / fps
    jump_height = np.sin(np.pi * time) * 2  # Jumping trajectory
    forward_distance = time * 5              # Moving forward

    # Update initial positions to represent the jump
    for i in range(num_points):
        x = initial_positions[i, 0] + forward_distance
        y = initial_positions[i, 1] + jump_height
        ax.plot(x, y, 'o', color='white')

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps)

# Display the animation
plt.show()
