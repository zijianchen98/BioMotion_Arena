
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points in the animation
num_points = 15

# Define the size of the figure
fig, ax = plt.subplots(figsize=(6, 6))

# Set the background color to black
ax.set_facecolor('black')

# Remove the axis labels and ticks
ax.axis('off')

# Define the initial positions and velocities of the points
positions = np.random.rand(num_points, 2)
velocities = np.zeros_like(positions)

# Define the acceleration due to gravity
gravity = np.array([0, -0.1])

# Define the function to update the positions of the points
def update(frame):
    # Update the velocities of the points based on the acceleration due to gravity
    velocities += gravity

    # Update the positions of the points based on their velocities
    positions += velocities

    # Keep the points within the bounds of the figure
    positions %= 1

    # Clear the previous frame
    ax.clear()

    # Plot the points
    ax.scatter(positions[:, 0], positions[:, 1], color='white')

    # Set the limits of the axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
