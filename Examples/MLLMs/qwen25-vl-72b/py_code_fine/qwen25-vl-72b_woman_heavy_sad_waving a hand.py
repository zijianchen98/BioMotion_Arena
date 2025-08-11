
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

# Define the movement of the points over time
def update_points(num):
    global points
    # Move the points in a wave-like pattern
    for i in range(len(points)):
        points[i][0] += 0.01 * np.sin(2 * np.pi * points[i][1])
        points[i][1] += 0.01 * np.cos(2 * np.pi * points[i][0])
    return points

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the scatter plot of the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for the animation
def animate(i):
    update_points(i)
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
