
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Define initial positions of points
positions = np.array([
    [0.45, 0.9], [0.5, 0.9], [0.55, 0.9],
    [0.4, 0.8], [0.45, 0.8], [0.5, 0.8], [0.55, 0.8], [0.6, 0.8],
    [0.4, 0.7], [0.45, 0.7], [0.5, 0.7], [0.55, 0.7], [0.6, 0.7],
    [0.45, 0.6], [0.5, 0.6], [0.55, 0.6]
])

# Create scatter plot
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

def update(frame):
    amplitude = 0.05
    frequency = 0.1

    # Calculate new positions
    new_positions = positions.copy()
    new_positions[:, 1] = positions[:, 1] - amplitude * np.sin(frequency * frame)

    # Update scatter plot data
    scat.set_offsets(new_positions)

    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

# Display animation
plt.axis('off')
plt.show()
