
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and their initial positions
num_points = 15
points = np.random.rand(num_points, 2)

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_facecolor('black')

# Create a scatter plot for the points
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the update function for the animation
def update(frame):
    # Update the positions of the points to simulate walking motion
    # Here we use a simple sinusoidal motion for demonstration purposes
    points[:, 0] += 0.01 * np.sin(2 * np.pi * frame / 50)
    points[:, 1] += 0.01 * np.cos(2 * np.pi * frame / 50)
    
    # Update the scatter plot data
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.show()
