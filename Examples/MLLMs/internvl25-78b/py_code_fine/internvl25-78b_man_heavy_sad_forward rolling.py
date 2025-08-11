
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
duration = 5  # seconds
frames = 100

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
scat = ax.scatter([], [], color='white')

# Initialize point positions
positions = np.zeros((frames, num_points, 2))

# Define initial positions (example configuration)
initial_positions = np.array([
    [0.45, 0.8], [0.5, 0.85], [0.55, 0.8],
    [0.4, 0.75], [0.5, 0.7], [0.6, 0.75],
    [0.4, 0.65], [0.5, 0.6], [0.6, 0.65],
    [0.45, 0.55], [0.5, 0.5], [0.55, 0.55],
    [0.45, 0.45], [0.5, 0.4], [0.55, 0.45]
])

# Fill in positions for forward rolling motion
for i in range(frames):
    angle = i * 2 * np.pi / frames
    positions[i] = initial_positions + [0.1 * np.cos(angle), 0.1 * np.sin(angle)]

def update(frame):
    scat.set_offsets(positions[frame % frames])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=duration*1000/frames, blit=True)

# Show plot
plt.axis('off')
plt.show()
