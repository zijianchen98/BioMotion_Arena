
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the animation
NUM_LIGHTS = 15
FRAMES = 60
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'
POINT_SIZE = 100

# Define the initial positions of the point-lights for a sad man lying down
# For simplicity, we'll represent the body as a series of points 
# arranged in a lying down position
initial_positions = np.array([
    [0, 2],    # Head
    [0, 1.5],  # Neck
    [0, 1],    # Chest
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],      # Upper body
    [-0.75, -0.5], [0.75, -0.5],  # Hips
    [-0.75, -1], [0.75, -1],      # Thighs
    [-0.5, -1.5], [0.5, -1.5],    # Knees
    [-0.25, -2], [0.25, -2]       # Feet
])

# Function to update the positions to simulate movement (sad motion)
def update_positions(frame):
    # Oscillate some points slightly for a natural effect
    idx = [2, 3, 4, 5, 6]  # Points to oscillate (chest and shoulders)
    offsets = 0.1 * np.sin(np.linspace(0, 2 * np.pi, len(idx)) + frame / 10)
    positions = initial_positions.copy()
    
    for i, offset in zip(idx, offsets):
        positions[i, 1] -= offset  # Move downwards for 'sad' effect
    
    scatter.set_offsets(positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-1, 1)
ax.set_ylim(-3, 3)
ax.axis('off')  # Hide axes

# Create scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], 
                     s=POINT_SIZE, color=POINT_COLOR)

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=FRAMES, 
                              interval=50, blit=True)

# Show the animation
plt.show()
