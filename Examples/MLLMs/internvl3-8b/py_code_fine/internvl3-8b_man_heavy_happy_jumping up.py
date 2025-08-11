
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_xticks([])
ax.set_yticks([])

# Number of points
num_points = 15

# Set up the points
points = ax.scatter(*[0 for _ in range(num_points)], color='white', s=200)

# Function to update the points position
def update(frame):
    global points
    for i in range(num_points):
        # Calculate the position based on the frame
        x = 10 * np.sin(frame/10 + i/5)
        y = 10 - 8 * np.cos(frame/8 + i/10)
        points.set_offsets([x, y])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 100), interval=50, blit=True)

# Show the plot
plt.show()
