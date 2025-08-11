
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
initial_positions = np.array([
    [0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
    [0, 1], [1, 2], [2, 3], [3, 4], [4, 5],
    [0, 2], [1, 3], [2, 4], [3, 5], [4, 6]
])

# Define the target positions of the points after jumping forward
target_positions = np.array([
    [1, 0], [2, 1], [3, 2], [4, 3], [5, 4],
    [1, 1], [2, 2], [3, 3], [4, 4], [5, 5],
    [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]
])

# Calculate the difference between the initial and target positions
diff = target_positions - initial_positions

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 7)

# Create a list of scatter objects for each point
scatters = []
for i in range(15):
    scatters.append(ax.scatter([], [], s=50, c='white'))

# Define the update function for the animation
def update(frame):
    # Calculate the new positions of the points based on the current frame
    new_positions = initial_positions + diff * frame / 100
    
    # Update the position of each scatter object
    for i in range(15):
        scatters[i].set_offsets(new_positions[i])
    
    return scatters

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

# Show the animation
plt.show()
