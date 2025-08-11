
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define the initial positions of the point-lights
points = np.array([
    [5, 1], [4, 2], [6, 2], [3, 3], [4.5, 3], [5.5, 3], [7, 3],
    [3.5, 4], [4.5, 4], [5.5, 4], [6.5, 4],
    [4, 5], [6, 5],
    [5, 6]
])

# Define the rotation angle for the turning motion
angle = np.linspace(0, 2 * np.pi, 100)

# Animation function
def update(frame):
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Apply rotation
    theta = angle[frame]
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    rotated_points = np.dot(points, rotation_matrix)
    
    # Plot the point-lights
    for x, y in rotated_points:
        ax.plot(x + 5, y + 5, 'wo', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(len(angle)), interval=50)

# Save the animation as a GIF
ani.save('happyman_turning_around.gif', writer='pillow')

# Show the animation
plt.show()
