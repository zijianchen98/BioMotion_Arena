
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim((-10, 10)
ax.set_ylim((-10, 10))
ax.set_aspect('equal')
ax.axis('off')

# Set up the points (15 white points on a circle
points = np.zeros((15, 2))
radius = 5
for i in range(15):
    angle = 2 * np.pi * i / 14
    points[i] = [radius * np.cos(angle), radius * np.sin(angle)]

# Function to update the positions of the points
def update_points(i):
    global points
    # Calculate the new positions based on forward rolling motion
    points[:, 0] += 0.1 * np.sin(i / 5)
    points[:, 1] += 0.1 * np.cos(i / 5)
    # Ensure the points stay within the circle
    points[points > radius] = 2 * radius - points[points > radius]
    points[points < -radius] = -2 * radius - points[points < -radius]

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=np.arange((100), interval=50)

plt.show()
