
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_points = 15
point_size = 0.1
speed = 0.5  # Speed of the movement in pixels per frame
duration = 10  # Duration of the animation in seconds

# Create a figure and an axes object
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create a list to store the points
points = []

# Generate the points for the animation
for i in range(num_points):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    points.append([x, y])

# Create a function to update the points
def animate(i):
    global points
    # Update the positions of the points
    for j in range(num_points):
        points[j][0] += speed * np.cos(i * 2 * np.pi / duration)
        points[j][1] += speed * np.sin(i * 2 * np.pi / duration)
    # Update the plot
    ax.clear()
    ax.scatter(*zip(*points), s=point_size, c='white')
    return ax

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration * 10, interval=10, blit=True)

# Show the animation
plt.show()
