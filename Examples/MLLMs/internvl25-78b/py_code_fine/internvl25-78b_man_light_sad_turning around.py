
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and the axis with black background
fig, ax = plt.subplots(figsize=(4, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Define the point lights
n_points = 15
dots, = ax.plot([], [], 'wo', markersize=5)

# Initial positions of the points
def init():
    dots.set_data([], [])
    return dots,

# Animation function
def animate(t):
    # Define the positions of the points
    positions = np.array([
        [0.5, 0.05],  # head
        [0.3, 0.15], [0.7, 0.15],  # shoulders
        [0.3, 0.25], [0.4, 0.25], [0.6, 0.25], [0.7, 0.25],  # upper body
        [0.25, 0.35], [0.35, 0.35], [0.65, 0.35], [0.75, 0.35],  # lower body
        [0.2, 0.45], [0.3, 0.45], [0.7, 0.45], [0.8, 0.45],  # arms
        [0.45, 0.55], [0.55, 0.55]  # legs
    ])

    # Rotation matrix
    angle = t % (2 * np.pi)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Apply rotation
    rotated_positions = np.dot(positions - [0.5, 0.5], rotation_matrix) + [0.5, 0.5]

    # Update the data
    dots.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return dots,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 128),
                              init_func=init, blit=True, repeat=True)

# Display the animation
plt.axis('off')
plt.show()
