
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames_per_second = 10
total_frames = 120
amplitude = 10
frequency = np.pi / 15
phase_diff = np.linspace(0, 2 * np.pi, num_points)

# Initial positions
positions = np.zeros((num_points, 2))

def update(frame):
    global positions
    for i in range(num_points):
        angle = frame * frequency + phase_diff[i]
        positions[i, 0] = i * 5 + 5 + amplitude * np.cos(angle)
        positions[i, 1] = 30 + amplitude * np.sin(angle)
    scat.set_offsets(positions)

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 80)
ax.set_ylim(0, 60)
ax.set_facecolor('black')
ax.axis('off')

scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/frames_per_second)

# Show the animation
plt.show()
