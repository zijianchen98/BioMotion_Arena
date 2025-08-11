
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)  # Initial Plotting of points

# Define number of points (joints)
num_points = 15

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to generate the walking motion
def walking_motion(frame):
    # Create a simple walking motion pattern for a sad woman
    # 2D coordinates for point lights
    x = np.array([0, -1, 1, -1.5, 1.5, -2, 2, -1, 1, -1, 1, -0.5, 0.5, -0.2, 0.2])  # Adjust as needed
    y = np.array([frame * 0.1, -1 + (frame % 20) * 0.1, -1 + (frame % 20) * 0.1,
                   -2 + (frame % 20) * 0.1, -2 + (frame % 20) * 0.1,
                   -2 - (frame % 20) * 0.1, -2 - (frame % 20) * 0.1,
                   -1 + (frame % 20) * 0.1, -1 + (frame % 20) * 0.1,
                   -1 - (frame % 20) * 0.1, -1 - (frame % 20) * 0.1,
                   -1 + (frame % 20) * 0.2, -1 - (frame % 20) * 0.2,
                   -0.5 - (frame % 20) * 0.1, 0.5 + (frame % 20) * 0.1])  # Adjust y for sad posture

    # Update point positions
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, walking_motion, frames=200, init_func=init, blit=True, interval=50)

plt.show()
