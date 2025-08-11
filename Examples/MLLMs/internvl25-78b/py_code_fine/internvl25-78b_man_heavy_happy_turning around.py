
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points
initial_positions = np.array([
    [0, 1], [0.5, 0.8], [-0.5, 0.8], [0, 0], [0.5, 0], [-0.5, 0],
    [0, -0.2], [0.5, -0.2], [-0.5, -0.2], [0, -0.6], [0.3, -0.6], [-0.3, -0.6],
    [0, -0.8], [0.4, -0.8], [-0.4, -0.8]
])

# Define the angles for rotation
angles = np.linspace(0, 2 * np.pi, 100)

def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')
    
    # Rotate points around the center
    rotation_matrix = np.array([
        [np.cos(angles[frame]), -np.sin(angles[frame])],
        [np.sin(angles[frame]), np.cos(angles[frame])]
    ])
    rotated_positions = np.dot(initial_positions, rotation_matrix.T)
    
    # Plot the points
    ax.scatter(rotated_positions[:, 0], rotated_positions[:, 1], color='white')

fig, ax = plt.subplots(figsize=(6, 6))
ani = animation.FuncAnimation(fig, update, frames=len(angles), interval=50)
plt.show()
