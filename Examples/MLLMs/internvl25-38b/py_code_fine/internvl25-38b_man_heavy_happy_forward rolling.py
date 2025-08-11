
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Define the initial positions of the 15 point-lights
n_points = 15
angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
x = 5 + 2 * np.cos(angles)
y = 5 + 2 * np.sin(angles)
points = ax.scatter(x, y, c='white', s=100)

# Define the animation function
def update(frame):
    angle = frame * np.pi / 30
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                  [np.sin(angle), np.cos(angle)]])
    centered_points = np.column_stack([x - 5, y - 5])
    rotated_points = np.dot(centered_points, rotation_matrix)
    points.set_offsets(rotated_points + [5, 5])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=50, blit=True)

# Display the animation
plt.show()
