
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the background color
num_points = 15
background_color = 'black'

# Define the point-light positions and velocities
points = np.zeros((num_points, 2))
velocities = np.zeros((num_points, 2))

# Define the initial positions and velocities for a sadwoman jumping up
# The points will be placed on a circle to represent the human body
theta = np.linspace(0, 2*np.pi, num_points, endpoint=False)
points[:, 0] = 200 + 100 * np.cos(theta)
points[:, 1] = 200 + 100 * np.sin(theta)

# Define the velocities to create a jumping motion
velocities[:, 0] = 0.5 * np.cos(theta)
velocities[:, 1] = 2.5 * np.sin(theta)

# Define the animation function
def animate(i):
    global points
    # Update the point-light positions based on the velocities
    points[:, 0] += velocities[:, 0] * 0.1
    points[:, 1] += velocities[:, 1] * 0.1
    
    # Reset the positions to the starting point after a full cycle
    if i % 100 == 0:
        points[:, 0] = 200 + 100 * np.cos(theta)
        points[:, 1] = 200 + 100 * np.sin(theta)
    
    # Clear the current axes and plot the points
    ax.clear()
    ax.set_facecolor(background_color)
    ax.set_xlim(0, 400)
    ax.set_ylim(0, 400)
    ax.set_aspect('equal')
    ax.scatter(points[:, 0], points[:, 1], color='white')

# Create a new figure
fig, ax = plt.subplots()

# Set the animation parameters
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, repeat=True)

# Show the animation
plt.show()
