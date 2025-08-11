
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and their initial positions
num_lights = 15
initial_positions = np.array([
    [0, 4], [1, 5], [-1, 5], [2, 6], [-2, 6], [0, 6],
    [0, 3], [1, 4], [-1, 4], [2, 5], [-2, 5], [0, 5],
    [0, 2], [1, 3], [-1, 3], [0, 1]
])
# Set the style of the animation
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 7)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # white point-lights

# Update function for animation
def update(frame):
    global initial_positions
    # Simulate jumping and moving forward
    offset = frame * 0.1  # Forward movement
    height_change = 2 * np.sin(frame * 0.1)  # Jump height
    new_positions = initial_positions.copy()
    new_positions[:, 0] += offset  # Move forward
    new_positions[:, 1] += height_change  # Up and down motion
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=50)
plt.show()
