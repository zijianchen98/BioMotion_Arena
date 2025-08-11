
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial position of the 15 white point-lights
initial_positions = [
    (0.0, 0.5), (0.1, 0.6), (0.2, 0.5), (0.1, 0.4),
    (0.0, 0.4), (-0.1, 0.4), (-0.2, 0.5), (-0.1, 0.6),
    (0.0, 0.6), (0.05, 0.7), (-0.05, 0.7), 
    (0.0, 0.3), (0.05, 0.2), (-0.05, 0.2), (0.0, 0.1)
]

# Animation parameters
num_frames = 100
speed = 0.01

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create a scatter plot for the point-lights
scat = ax.scatter([], [], c='white')

def update(frame):
    positions = initial_positions
    # Simulate rolling motion
    for i, (x, y) in enumerate(positions):
        new_x = x + np.sin(frame * speed) * 0.1
        new_y = y + np.cos(frame * speed) * 0.1
        positions[i] = (new_x, new_y)

    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()
