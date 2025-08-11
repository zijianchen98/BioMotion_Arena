
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24

# Initialize positions
np.random.seed(0)
positions = np.zeros((frames, num_lights, 2))

# Define jumping forward motion
def jumping_forward(t):
    x = t * 0.1  # Move forward
    y = 0.5 * np.sin(t * 0.5) - 0.5  # Jumping up and down
    return x, y

# Generate positions for each frame
for i in range(frames):
    t = i / fps
    base_x, base_y = jumping_forward(t)

    # Define 15 point-light positions relative to the base position
    positions[i] = [
        [base_x + dx, base_y + dy]
        for dx, dy in [
            (-0.2, 0.8), (-0.1, 0.8), (0, 0.9), (0.1, 0.8), (0.2, 0.8),
            (-0.3, 0.6), (-0.2, 0.6), (-0.1, 0.7), (0, 0.7), (0.1, 0.7), (0.2, 0.6), (0.3, 0.6),
            (-0.2, 0.4), (0.2, 0.4),
            (0, 0.2)
        ]
    ]

# Create plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 1)
ax.axis('off')
ax.set_facecolor('black')

# Initialize scatter plot
scatter = ax.scatter([], [], s=100, color='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)

plt.show()
