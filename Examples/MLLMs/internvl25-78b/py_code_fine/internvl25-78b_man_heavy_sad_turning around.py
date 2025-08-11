
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.axis('off')

# Number of points
num_points = 15

# Initialize point positions
points = np.zeros((num_points, 2))

# Define initial positions
points[0] = [0, 5]
points[1:4] = [0, 4], [-1, 4], [1, 4]
points[4:7] = [0, 3], [-1, 3], [1, 3]
points[7:10] = [0, 2], [-1, 2], [1, 2]
points[10:13] = [0, 1], [-1, 1], [1, 1]
points[13:15] = [-0.5, 0], [0.5, 0]

# Create scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function
def update(frame):
    angle = frame % 360
    rotation_matrix = np.array([
        [np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
        [np.sin(np.radians(angle)), np.cos(np.radians(angle))]
    ])
    rotated_points = np.dot(points, rotation_matrix)
    scat.set_offsets(rotated_points)

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=50)

plt.show()
