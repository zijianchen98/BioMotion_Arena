
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points
def init_points():
    # Define initial positions for a turning around motion (sad woman)
    points = np.array([
        [0, -1], [0, 1], [-1, 0], [1, 0], [0, 0],  # Core body
        [-0.5, -0.5], [0.5, -0.5], [-0.5, 0.5], [0.5, 0.5],  # Arms
        [-1, -1], [1, -1], [-1, 1], [1, 1],  # Legs
        [-0.8, 0], [0.8, 0]  # Head points
    ])
    return points

# Update function for animation
def update(frame):
    global points
    angle = frame / 10.0
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_points = np.dot(points, rotation_matrix)
    scatter.set_offsets(rotated_points)

    # Adjust points to create a more dynamic and sad appearance
    if frame % 30 == 0:
        points[4] += np.random.normal(0, 0.1, size=(2,))  # Random head tilt

    return scatter,

# Initialize points
points = init_points()

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

ani = animation.FuncAnimation(fig, update, frames=range(0, 360), interval=50, blit=True)

plt.axis('off')
plt.show()
