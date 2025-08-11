
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of point-lights and their initial positions
num_points = 15
theta = np.linspace(0, 2 * np.pi, num_points)  # Angle for each point-light
radius = 1  # Radius of the circular motion

# Initial positions of the point-lights arranged in a circular pattern
initial_positions = np.array([[radius * np.cos(t), radius * np.sin(t)] for t in theta])

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')  # Solid black background

# Create a scatter plot for the point-lights
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation
def update(frame):
    # Calculate the angle of rotation based on the frame
    angle = np.radians(frame * 4)  # Control the speed of rotation
    # Rotate the initial positions to create a turning effect
    rotated_positions = initial_positions @ np.array([[np.cos(angle), -np.sin(angle)],
                                                       [np.sin(angle), np.cos(angle)]])
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 90), init_func=init, blit=True, interval=50)

plt.axis('off')  # Disable the axis
plt.show()
