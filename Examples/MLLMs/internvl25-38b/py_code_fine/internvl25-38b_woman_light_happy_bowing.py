
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the animation
num_points = 15
frame_rate = 30
num_frames = 200
time = np.linspace(0, 1, num_frames)
amplitude = 10
frequency = 2 * np.pi

# Initial positions of the points
positions = np.array([
    [30, 50], [30, 40], [30, 30], [30, 20], [30, 10],
    [20, 45], [20, 35], [20, 25], [20, 15], [20, 5],
    [40, 45], [40, 35], [40, 25], [40, 15], [40, 5]
])

# Function to update the position of the points
def update(frame):
    for i, pos in enumerate(positions):
        if i < 5:
            positions[i, 1] = 50 - amplitude * np.sin(frequency * time[frame])
        elif i < 10:
            positions[i, 1] = 45 - amplitude * np.sin(frequency * time[frame] + np.pi / 2)
        else:
            positions[i, 1] = 45 - amplitude * np.sin(frequency * time[frame] - np.pi / 2)
    scat.set_offsets(positions)
    return scat,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 60)
ax.set_ylim(0, 60)
ax.axis('off')

# Scatter plot for point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

# Animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 / frame_rate, blit=True)

plt.show()
