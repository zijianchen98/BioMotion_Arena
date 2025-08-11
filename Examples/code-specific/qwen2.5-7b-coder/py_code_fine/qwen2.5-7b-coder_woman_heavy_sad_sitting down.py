
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 60

# Define the initial positions of the 15 point lights
initial_positions = np.random.rand(15, 2) * 8 - 4

# Define the target positions for each frame
target_positions = np.array([
    [0, -4],
    [-1, -3],
    [1, -3],
    [-2, -2],
    [2, -2],
    [-3, -1],
    [3, -1],
    [-4, 0],
    [4, 0],
    [-5, 1],
    [5, 1],
    [-6, 2],
    [6, 2],
    [-7, 3],
    [7, 3]
])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

def update(frame):
    # Calculate the fraction of the way through the current frame
    t = frame / num_frames
    
    # Interpolate between the initial and target positions
    positions = (1 - t) * initial_positions + t * target_positions
    
    # Update the scatter plot
    scatter.set_offsets(positions)
    
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

# Show the animation
plt.show()
