
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create initial positions of the points representing the happy man's body
# Simplified positions for demonstration
points_x = np.array([0, 0.5, -0.5, 0, 0, -0.5, 0.5, 0, 0, -0.5, 0.5, 0, 0, 0.5, -0.5])
points_y = np.array([1, 0.7, 0.7, 0, -0.7, -1, -1, -0.7, -1, -1, -0.7, 0.7, 1, 1, 1])

# Create a scatter plot for the point-lights
point_lights, = ax.plot(points_x, points_y, 'o', color='white')

# Update function for animation
def update(frame):
    # Create a smooth motion effect by modifying the y-coordinates
    y_shift = 0.01 * np.sin(np.radians(frame * 10))  # Simple oscillation
    new_y = points_y + y_shift
    point_lights.set_data(points_x, new_y)
    return point_lights,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=50, blit=True)

# Show the animation
plt.show()
