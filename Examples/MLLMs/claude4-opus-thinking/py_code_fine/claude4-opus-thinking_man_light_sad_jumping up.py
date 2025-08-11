
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15
frames = 60
jump_height = 1.0

# Initial position of the point lights (2D array)
# Define positions for a sad figure (as point lights)
# These coordinates are simple for demonstration purposes.
# The coordinates could be adapted to better represent a sad man.
positions = np.array([
    [0, 1.5], [1, 2], [-1, 2],  # Head
    [0, 1], [1, 1.5], [-1, 1.5],  # Shoulders
    [0, 0], [1, 1], [-1, 1],  # Upper body
    [0, -1], [1, 0], [-1, 0],  # Lower body
    [0.5, -2], [-0.5, -2], [1, -1], [-1, -1],  # Legs
])

# Function to update the animation
def update(frame):
    # Clear the axes for each frame
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_facecolor('black')

    # Calculate the new y positions for jumping motion
    jump_offset = jump_height * np.sin(np.pi * frame / (frames // 2))

    # Update y positions
    updated_positions = positions + [0, jump_offset]
    
    # Plot the points
    ax.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white', s=100)

# Setting up the figure and axis
fig, ax = plt.subplots()

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=False, repeat=True)

# Display the animation
plt.show()
