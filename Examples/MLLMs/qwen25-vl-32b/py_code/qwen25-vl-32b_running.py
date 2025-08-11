
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 60

# Define the positions of the point lights for each frame
# Each row represents a frame, and each column represents a point light's x or y coordinate
positions = np.array([
    # Frame 1
    [0.4, 0.8, 0.6, 0.8, 0.5, 0.6, 0.4, 0.4, 0.6, 0.4, 0.6, 0.2, 0.4, 0.2, 0.6],
    [0.2, 0.4, 0.4, 0.6, 0.5, 0.8, 0.6, 0.2, 0.4, 0.8, 0.6, 0.4, 0.2, 0.4, 0.6],
    # Frame 2
    [0.4, 0.8, 0.6, 0.8, 0.5, 0.6, 0.4, 0.4, 0.6, 0.4, 0.6, 0.2, 0.4, 0.2, 0.6],
    [0.2, 0.4, 0.4, 0.6, 0.5, 0.8, 0.6, 0.2, 0.4, 0.8, 0.6, 0.4, 0.2, 0.4, 0.6],
    # ... (repeat for all frames)
])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes

# Initialize the scatter plot
scatter = ax.scatter([], [], s=50, c='white')

def update(frame):
    # Update the positions of the point lights
    scatter.set_offsets(positions[frame].reshape(-1, 2))
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

# Display the animation
plt.show()
