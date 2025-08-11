
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the points for the initial frame
initial_positions = np.array([
    [0.5, 0.9],  # head
    [0.4, 0.7],  # left shoulder
    [0.6, 0.7],  # right shoulder
    [0.3, 0.5],  # left elbow
    [0.7, 0.5],  # right elbow
    [0.2, 0.3],  # left hand
    [0.8, 0.3],  # right hand
    [0.5, 0.4],  # waist
    [0.4, 0.2],  # left hip
    [0.6, 0.2],  # right hip
    [0.3, 0.1],  # left knee
    [0.7, 0.1],  # right knee
    [0.2, 0.0],  # left foot
    [0.8, 0.0],  # right foot
    [0.5, 0.8]   # neck
])

# Function to simulate bowing motion
def bow_motion(frame, points):
    angle = np.pi / 6 * np.sin(frame / 20)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    displacement = np.array([0, -0.1 * np.sin(frame / 20)])
    points[:, :] = (points @ rotation_matrix.T) + displacement

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Animation function
def animate(frame):
    bow_motion(frame, initial_positions)
    points.set_offsets(initial_positions)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
