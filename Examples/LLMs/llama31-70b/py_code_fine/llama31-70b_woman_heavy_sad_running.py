
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light positions for the sad woman with heavy weight
# Each row represents a point-light, with the first two columns representing the x and y positions, 
# and the third column representing the phase offset for the movement
point_lights = np.array([
    [0.0, 0.5, 0.0],  # head
    [-0.2, 0.7, 0.1],  # left shoulder
    [0.2, 0.7, -0.1],  # right shoulder
    [-0.3, 0.9, 0.2],  # left elbow
    [0.3, 0.9, -0.2],  # right elbow
    [-0.4, 1.1, 0.3],  # left wrist
    [0.4, 1.1, -0.3],  # right wrist
    [0.0, 0.3, 0.4],  # torso
    [-0.1, 0.1, 0.5],  # left hip
    [0.1, 0.1, -0.5],  # right hip
    [-0.2, -0.1, 0.6],  # left knee
    [0.2, -0.1, -0.6],  # right knee
    [-0.3, -0.3, 0.7],  # left ankle
    [0.3, -0.3, -0.7],  # right ankle
    [0.0, -0.5, 0.8],  # heavy weight
])

# Define the movement parameters for the running action
# The movement is defined as a sinusoidal function with the given amplitude, frequency, and phase offset
amplitude = 0.1
frequency = 2.0
phase_offset = 0.0

# Create a new figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-light positions
points = ax.scatter(point_lights[:, 0], point_lights[:, 1], s=50, c='white')

# Define the animation function
def animate(frame):
    global points
    points.remove()
    new_points = np.copy(point_lights)
    new_points[:, 0] += amplitude * np.sin(frequency * frame + point_lights[:, 2])
    new_points[:, 1] += amplitude * np.cos(frequency * frame + point_lights[:, 2])
    points = ax.scatter(new_points[:, 0], new_points[:, 1], s=50, c='white')
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), blit=True, interval=50)

plt.show()
