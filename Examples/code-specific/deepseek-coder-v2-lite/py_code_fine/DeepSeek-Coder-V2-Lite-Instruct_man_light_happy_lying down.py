
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initialize the points
points = np.zeros((15, 2))
for i in range(15):
    angle = 2 * np.pi * i / 15
    points[i, 0] = np.cos(angle)
    points[i, 1] = np.sin(angle)

# Initialize the scatter plot
scatter = ax.scatter([], [], color='white', s=100)

def init():
    scatter.set_offsets(points)
    return scatter,

def update(frame):
    # Rotate the points smoothly
    angle = 2 * np.pi * frame / 100
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    rotated_points = points.dot(rotation_matrix)
    scatter.set_offsets(rotated_points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True, repeat=True)

# Set up the background
ax.set_facecolor('black')
ax.axis('off')

# Show the animation
plt.show()
