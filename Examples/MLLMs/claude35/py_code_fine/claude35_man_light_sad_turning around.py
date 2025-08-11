
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Define the initial positions of the point lights
num_points = 15
theta = np.linspace(0, 2 * np.pi, num_points)  # Circular motion
radius = 0.5
initial_positions = np.array([radius * np.cos(theta), radius * np.sin(theta)]).T

# Function to update the points for the animation
def update(frame):
    # Simulate a turning around motion
    angle = np.radians(frame)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    
    rotated_positions = initial_positions.dot(rotation_matrix)
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 5), blit=True, interval=50)

# Show the animation
plt.show()
