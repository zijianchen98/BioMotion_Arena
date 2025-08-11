
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the positions of the points
def init_positions():
    positions = np.array([
        [0, 1], [0.2, 0.8], [-0.2, 0.8], [0.4, 0.6], [-0.4, 0.6], 
        [0.6, 0.5], [-0.6, 0.5], [0.8, 0.4], [-0.8, 0.4], 
        [0, 0.3], [0, 0.2], [0.2, 0.1], [-0.2, 0.1], [0.1, 0], [-0.1, 0]
    ])
    return positions

# Update function for the animation
def update(frame, scatter, positions):
    # Example of movement for waving hand
    wave_offset = np.sin(frame / 10) * 0.2
    positions[9:, 0] += wave_offset
    scatter.set_offsets(positions)

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1.5)

# Initialize scatter plot
positions = init_positions()
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, fargs=(scatter, positions), interval=50)

plt.axis('off')
plt.show()
