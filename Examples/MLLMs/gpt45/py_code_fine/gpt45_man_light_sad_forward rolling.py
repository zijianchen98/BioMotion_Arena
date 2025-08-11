
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Define the initial positions of the point lights
# This is a simplified representation of a happy person
def init():
    points.set_data([], [])
    return points,

# Define the forward rolling motion
def forward_roll(frame):
    t = frame / 10.0  # Scale frame to control speed of animation
    # Calculate the positions of the points based on simple sine/cosine functions
    x = np.array([0, 0, -1, 1, -1, 1, -0.5, 0.5, -1.5, 1.5, 0, 0, -1, 1, 0]) + np.sin(t)  # Example positions
    y = np.array([2, 1.5, 1, 1, 1, 1, 0.5, 0.5, -0.5, -0.5, 0, -t, -1, -t, -2])  # Example positions
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, forward_roll, frames=100, init_func=init, blit=True, interval=20)

# Show the animation
plt.show()
