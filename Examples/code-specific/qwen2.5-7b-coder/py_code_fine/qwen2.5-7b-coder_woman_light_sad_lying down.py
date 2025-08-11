
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames
num_frames = 60

# Define the positions of the point lights
positions = np.zeros((num_frames, 15, 2))

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot for the point lights
scat = ax.scatter(positions[0, :, 0], positions[0, :, 1], color='white')

def update(frame):
    # Update the positions of the point lights based on the current frame
    scat.set_offsets(positions[frame])
    return scat,

# Load the precomputed positions from a file or generate them using a motion capture system
# For simplicity, we'll use random positions here
np.random.seed(42)
for i in range(num_frames):
    positions[i] = np.random.rand(15, 2) * 2 - 1

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
