
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.8, 0.4], [-0.6, 0.4], [-0.4, 0.4], [-0.2, 0.4], [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4],
    [0, 0.1], [0, -0.1]
])

# Define the walking motion parameters
num_frames = 100
frame_rate = 30
amplitude = 0.1
frequency = 0.1

# Create a function to update the positions of the points for each frame
def update(frame):
    t = frame / frame_rate
    x_offset = amplitude * np.sin(2 * np.pi * frequency * t)
    y_offset = amplitude * np.cos(2 * np.pi * frequency * t)

    updated_positions = initial_positions.copy()
    updated_positions[:, 0] += x_offset
    updated_positions[:, 1] += y_offset

    # Apply a slight vertical oscillation to the points to simulate walking
    updated_positions[4:13, 1] += 0.05 * np.sin(2 * np.pi * frequency * t + np.pi / 2)

    scat.set_offsets(updated_positions)
    return scat,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate, blit=True)

plt.show()
