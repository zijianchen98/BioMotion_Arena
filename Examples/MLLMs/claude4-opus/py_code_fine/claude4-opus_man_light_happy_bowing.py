
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_points = 15

# Initialize positions of point-lights (for "bowing" motion)
# Assuming a simple upright position to mid-bow transformation
def get_positions(frame):
    # Create a base position for "bowing"
    base_y = np.array([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])
    x_pos = np.zeros(num_points)  # All x coordinates are zero for a vertical bow
    y_pos = base_y * (1 - frame / 30)  # Animate down for bowing effect
    return x_pos, y_pos

# Set up for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-6, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the points
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    x, y = get_positions(frame)
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 31), init_func=init, blit=True, interval=100)

# Show the animation
plt.show()
