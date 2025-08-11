
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Number of point-lights
num_points = 15
points = np.zeros((num_points, 2))

# Set up the initial positions for the point lights (head, body, legs)
# A simple representation of a bowing action
points[0] = [0, 0.5]  # head
points[1:6] = [[-0.2, 0], [0.2, 0], [-0.4, -0.5], [0.4, -0.5], [0, -1]]  # body
points[6:11] = [[-0.5, -1.5], [-0.5, -1.8], [0.5, -1.5], [0.5, -1.8], [0, -2.2]]  # legs
points[11:] = [[-0.2, -0.5], [0.2, -0.5], [-0.4, -0.5], [0.4, -0.5], [0, -1]]  # reinforcements

# Create scatter plot for point lights
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the update function for the animation
def update(frame):
    # Apply a simple downward motion to represent the bowing action
    points[0, 1] -= 0.02  # head lower
    for i in range(1, num_points):
        points[i, 1] -= 0.02 * (np.random.uniform(0.8, 1.2))  # variations in motion
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.show()
