
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the point-lights
def init_positions():
    # Define the positions of the point-lights
    positions = np.array([
        [0,  0,  0,  10,   8,  7,  6,  5,  4,  3,  2,  1,  0,  1,  1 ],
        [  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1 ]
    ])
    return positions

# Update the positions for each sitting down
def update_positions(frame, positions):
    # Simplified model for sitting down
    if frame < 30:
        positions[0, 7] += 1
        positions[0, 8] += 1
    elif frame < 60:
        positions[0, 7] -= 1
        positions[8, 8] += 1
    elif frame < 91:
        positions[7, 7] += 1
        positions[7, 8] += 1
    elif frame < 121:
        positions[7, 7] -= 1
        positions[8, 8] -= 1
    else:
        positions[7, 7] -= 1
        positions[7, 8] -= 1
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.ax.set_xlim(0, 15)
ax.ax.set_ylim(0, 15)
ax.ax.set_aspect('equal'
ax.ax.axis('off')

# Initialize the positions
positions = init_positions()

# Create the scatter plot
scat = ax.scatter(positions[0], positions[0], c='w', s=100)

# Animation function
def animate(frame):
    positions = update_positions(frame, positions)
    scat.set_offsets(positions.T)
    return scat,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, 151), interval=20, blit=True)

# Show the animation
plt.show()
