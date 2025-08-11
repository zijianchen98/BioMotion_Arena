
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
n_points = 15

# Define the position and velocity of each point light
points = np.zeros((n_points, 2))
velocities = np.zeros((n_points, 2))

# Define the initial positions and velocities for a jumping motion
for i in range(n_points):
    points[i, 0] = np.sin(i * np.pi / n_points) * 0.5 + 0.5  # x position
    points[i, 1] = np.cos(i * np.pi / n_points) * 0.5 + 0.5  # y position

    # Assign velocities to each point light to create a jumping motion
    if i < 5:
        velocities[i, 0] = 0.1  # initial x velocity
        velocities[i, 1] = -0.2  # initial y velocity
    elif i < 10:
        velocities[i, 0] = -0.1  # x velocity
        velocities[i, 1] = 0.2  # y velocity
    else:
        velocities[i, 0] = 0.1  # x velocity
        velocities[i, 1] = -0.2  # y velocity

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with a black background
ax.set_facecolor('black')

# Create a scatter plot with the initial points
scatter = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

# Define the animation function
def animate(frame):
    global points

    # Update the positions of the point lights based on their velocities
    points += velocities / 10

    # Keep the points within the boundaries
    points = np.clip(points, 0, 1)

    # Clear the previous frame
    ax.clear()

    # Set the black background
    ax.set_facecolor('black')

    # Update the scatter plot with the new positions
    scatter = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20)

# Show the animation
plt.show()
