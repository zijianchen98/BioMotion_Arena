
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
initial_positions = np.array([
    [0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
    [0, 1], [1, 2], [2, 3], [3, 4], [4, 5],
    [0, 2], [1, 3], [2, 4], [3, 5], [4, 6]
])

# Define the target positions of the points after jumping up
target_positions = np.array([
    [0, 2], [1, 3], [2, 4], [3, 5], [4, 6],
    [0, 3], [1, 4], [2, 5], [3, 6], [4, 7],
    [0, 4], [1, 5], [2, 6], [3, 7], [4, 8]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 9)

# Create a list of scatter objects for each point
scatters = []
for i in range(15):
    scatters.append(ax.scatter([], [], s=50, c='white'))

# Define the update function for the animation
def update(frame):
    # Calculate the current position of each point based on the frame number
    current_positions = (1 - frame / 100) * initial_positions + (frame / 100) * target_positions
    
    # Update the position of each scatter object
    for i in range(15):
        scatters[i].set_offsets(current_positions[i])
    
    return scatters

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

# Show the animation
plt.show()
