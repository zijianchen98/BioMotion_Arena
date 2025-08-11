
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
def init_positions():
    positions = np.array([
        [0, 1], [-0.5, 0.8], [0.5, 0.8], [-1, 0.5], [1, 0.5],
        [-0.5, 0.5], [0.5, 0.5], [-1, 0], [0, 0], [1, 0],
        [-0.5, -0.5], [0.5, -0.5], [-1, -0.8], [0, -0.8], [1, -0.8], 
        [0, -1]
    ])
    return positions

# Update function for the animation
def update_positions(i, points):
    angle = i / 10.0
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    for point in points:
        point.set_data(np.dot(point.get_data(), rotation_matrix))
    return points

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Create point-light objects
points = [ax.scatter(*pos, color='white') for pos in init_positions()]

# Create animation
ani = animation.FuncAnimation(fig, update_positions, frames=100, fargs=(points,), interval=50, blit=True)

plt.axis('off')
plt.show()
