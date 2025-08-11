
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize point positions
n_points = 15
black_background = (0, 0, 0)
point_color = 'white'

# Define initial positions of points
# Simplified model for a lying down person
initial_positions = np.array([
    [0, 0.9], [0.2, 0.9], [0.4, 0.9],
    [0.1, 0.8], [0.3, 0.8], [0.5, 0.8],
    [0, 0.7], [0.2, 0.7], [0.4, 0.7], [0.6, 0.7],
    [0.1, 0.6], [0.3, 0.6], [0.5, 0.6], [0.7, 0.6],
    [0.2, 0.5], [0.4, 0.5]
])

# Normalize positions
initial_positions -= np.mean(initial_positions, axis=0)

# Animation function
def animate(frame):
    angle = frame / 10.0
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    rotated_positions = np.dot(initial_positions, rotation_matrix)
    
    scatter.set_offsets(rotated_positions)
    return scatter,

# Setup plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor(black_background)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color=point_color)

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50, blit=True)

plt.axis('off')
plt.show()
