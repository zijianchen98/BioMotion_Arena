
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the number of points and the background color
num_points = 15
background_color = 'black'

# Define the point positions and colors
points = np.random.rand(num_points, 2)
colors = np.ones((num_points, 4))
colors[:, 3] = 1  # alpha channel for transparency

# Define the animation function
def animate(frame):
    global points
    ax.clear()
    ax.set_facecolor(background_color)
    
    # Update the point positions based on the action (turning around)
    angle = np.radians(frame * 10)  # increase angle by 10 degrees per frame
    x = np.cos(angle) * 1 + 0.5  # add some offset to the x-coordinate
    y = np.sin(angle) * 1 + 0.5  # add some offset to the y-coordinate
    points[:, 0] = x + np.cos(angle + np.pi/2) * np.random.rand(num_points) * 0.2
    points[:, 1] = y + np.sin(angle + np.pi/2) * np.random.rand(num_points) * 0.2
    
    # Plot the points
    for i in range(num_points):
        ax.scatter(points[i, 0], points[i, 1], c=colors[i], s=100)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(360), interval=50, repeat=True)

# Show the animation
plt.show()
