
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the sadman
point_lights = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.4, 0.7],  # Left elbow
    [0.6, 0.7],  # Right elbow
    [0.4, 0.6],  # Left hand
    [0.6, 0.6],  # Right hand
    [0.5, 0.5],  # Hip
    [0.4, 0.4],  # Left knee
    [0.6, 0.4],  # Right knee
    [0.4, 0.3],  # Left ankle
    [0.6, 0.3],  # Right ankle
    [0.5, 0.2],  # Left foot
    [0.5, 0.1],  # Right foot
    [0.5, 0.0],  # Center of mass
])

# Define the animation parameters
fps = 30
duration = 5  # seconds
num_frames = int(fps * duration)

# Define the motion parameters
roll_angle = np.linspace(0, 2 * np.pi, num_frames)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points, = ax.plot(point_lights[:, 0], point_lights[:, 1], 'wo', markersize=5)

def animate(frame):
    # Update the point-lights based on the roll angle
    angle = roll_angle[frame]
    rotated_points = np.copy(point_lights)
    rotated_points[:, 0] = point_lights[:, 0] * np.cos(angle) - point_lights[:, 1] * np.sin(angle)
    rotated_points[:, 1] = point_lights[:, 0] * np.sin(angle) + point_lights[:, 1] * np.cos(angle)

    # Update the point-lights on the plot
    points.set_data(rotated_points[:, 0], rotated_points[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/fps)

plt.show()
