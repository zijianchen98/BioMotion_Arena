
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([
    [0.5, 0.9], [0.4, 0.8], [0.6, 0.8],
    [0.3, 0.7], [0.5, 0.7], [0.7, 0.7],
    [0.2, 0.6], [0.4, 0.6], [0.6, 0.6], [0.8, 0.6],
    [0.3, 0.5], [0.5, 0.5], [0.7, 0.5],
    [0.4, 0.4], [0.6, 0.4]
])

# Define the target positions of the points after sitting down
target_points = np.array([
    [0.5, 0.4], [0.4, 0.5], [0.6, 0.5],
    [0.3, 0.6], [0.5, 0.6], [0.7, 0.6],
    [0.2, 0.7], [0.4, 0.7], [0.6, 0.7], [0.8, 0.7],
    [0.3, 0.8], [0.5, 0.8], [0.7, 0.8],
    [0.4, 0.9], [0.6, 0.9]
])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Create a list of scatter objects for each point
scatters = []
for i in range(points.shape[0]):
    scatters.append(ax.scatter(points[i, 0], points[i, 1], color='white'))

# Define the update function for the animation
def update(frame):
    # Calculate the new positions of the points based on the current frame
    new_points = points + (target_points - points) * frame / 100
    
    # Update the position of each scatter object
    for i in range(points.shape[0]):
        scatters[i].set_offsets(new_points[i])
    
    return scatters

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

# Show the animation
plt.show()
