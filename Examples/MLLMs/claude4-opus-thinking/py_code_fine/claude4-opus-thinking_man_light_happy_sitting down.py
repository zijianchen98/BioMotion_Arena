
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15  # Number of point lights
width, height = 6, 6  # Dimensions of the plot
fps = 24  # Frames per second
num_frames = 60  # Total frames in the animation

# Point-light positions representing a happy man sitting down
# The coordinates can be adjusted for better representation
point_positions = np.array([
    [0, 2],   # Head
    [-1, 1.5], [0, 1.5], [1, 1.5],  # Shoulders
    [-1, 1], [0, 1], [1, 1],  # Upper Body
    [-1, 0], [1, 0],  # Knees
    [-1, -1], [1, -1],  # Feet
    [0, 0]   # Center of the body
]).T

# Function to update the point positions for animation
def update(frame):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_facecolor('black')

    # Adjust the heights to simulate sitting down
    heights = point_positions[1] - (frame / num_frames)  # Simulate sitting down

    # Draw point lights
    for i in range(num_points):
        ax.plot(point_positions[0][i], heights[i], 'wo', markersize=10)

# Set up figure and axis
fig, ax = plt.subplots(figsize=(width, height))
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/fps)

# Show animation
plt.show()
