
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 5)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Initial positions of the point lights
num_points = 15
y_positions = np.array([0.5, 1.0, 2.0, 1.0, 0.5, 0.0, -0.5, -1.0, -0.5, 0.0, 1.0, 1.5, 2.0, 1.5, 0.5])
x_positions = np.array([0, -0.5, 0, 0.5, 0, 0, 0, 0, -0.5, 0.5, 0, 0, 0, 0, 0])

# Scatter plot for point lights
points, = ax.plot([], [], 'o', color='white')

# Update function for animation
def update(frame):
    # Calculate new positions for jumping motion
    new_y_positions = y_positions + 0.1 * np.sin(np.pi * (frame / 10.0))
    new_x_positions = x_positions + frame / 30.0  # Jump forward motion
    points.set_data(new_x_positions, new_y_positions)
    return points,

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
