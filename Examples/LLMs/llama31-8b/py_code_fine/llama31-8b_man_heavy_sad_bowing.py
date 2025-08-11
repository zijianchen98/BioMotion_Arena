
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the number of points
num_points = 15

# Define the initial positions of the points
points = np.random.rand(num_points, 2) * 2

# Define the colors of the points
colors = ['w'] * num_points

# Define the radius of the points
radius = 2

# Define the initial velocities of the points
velocities = np.zeros((num_points, 2))

# Define the animation function
def animate(i):
    global points, velocities
    
    # Update the positions of the points
    points[:, 0] += velocities[:, 0] * 0.01
    points[:, 1] += velocities[:, 1] * 0.01
    
    # Keep the points within the boundaries
    points = np.clip(points, 0, 2)
    
    # Update the velocities of the points
    velocities[:, 0] = np.cos(i / 10) * 0.1
    velocities[:, 1] = np.sin(i / 10) * 0.1
    
    # Draw the background
    ax.clear()
    ax.set_facecolor('k')
    
    # Draw the points
    ax.scatter(points[:, 0], points[:, 1], c=colors, s=radius*radius)
    
    # Draw the sadman
    sadman = plt.Rectangle((0.5, 0.5), 1, 1, color='w')
    ax.add_patch(sadman)
    
    # Draw the heavy weight
    weight = plt.Rectangle((0.6, 0.8), 0.2, 0.2, color='w')
    ax.add_patch(weight)
    
    # Set the axis limits
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), blit=False, interval=16)

# Show the animation
plt.show()
