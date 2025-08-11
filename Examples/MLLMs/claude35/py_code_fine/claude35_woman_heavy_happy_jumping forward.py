
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point lights
num_points = 15
points = np.zeros((num_points, 2))

# Initialize the positions of the point lights
for i in range(num_points):
    points[i, 0] = np.sin(np.pi * i / (num_points - 1))  # x-coordinates
    points[i, 1] = -4 + (i % 5)  # y-coordinates

# Update function for animation
def update(frame):
    # Simulate jumping motion by altering the y-coordinates based on a sine wave
    points[:, 1] = points[:, 1] + 0.1 * np.sin(2 * np.pi * (frame / 20))  # Vertical motion
    points[:, 0] += 0.5  # Forward motion
    
    # Clear the previous points
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-5, 5)
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Plot the point-lights
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.show()
