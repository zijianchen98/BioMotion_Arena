
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create 15 point-lights
n_points = 15
points = np.random.rand(n_points, 2) * 10

# Function to update the positions of the points for each frame
def update(frame):
    global points
    # Simulate simple random walk for each point
    points += np.random.normal(size=(n_points, 2)) * 0.1
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_facecolor('black')
    ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Animate the points
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
