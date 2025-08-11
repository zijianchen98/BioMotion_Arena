
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the size of the figure
num_points = 15
fig, ax = plt.subplots(figsize=(6, 6))

# Set the background color to black
ax.set_facecolor('black')

# Remove the axis labels and ticks
ax.axis('off')

# Define the initial positions and velocities of the points
positions = np.random.rand(num_points, 2) * 10
velocities = np.random.normal(0, 0.1, (num_points, 2))

# Function to update the positions of the points
def update(frame):
    global positions, velocities
    # Update the positions based on the velocities
    positions += velocities
    # Keep the points within the bounds of the figure
    positions %= 10
    # Clear the previous frame
    ax.clear()
    # Set the background color to black
    ax.set_facecolor('black')
    # Plot the points in white
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)
    # Set the limits of the axes
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=40)

# Show the animation
plt.show()
