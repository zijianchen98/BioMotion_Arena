
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and an axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize positions of the point-lights (15 points)
# Simulating lying down by setting fixed positions
x_positions = np.array([-0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.1, 0.05, 0.0, -0.05, -0.1, -0.15])
y_positions = np.array([-0.8, -0.7, -0.6, -0.5, -0.4, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -0.9, -0.9, -1.0, -1.0])

# Create scatter points for the point-lights
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Simulate slight vertical movement to show the action of lying down
    y_positions_moving = y_positions + 0.05 * np.sin(np.linspace(0, 2 * np.pi, num_points) + frame * 0.1)
    points.set_data(x_positions, y_positions_moving)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
