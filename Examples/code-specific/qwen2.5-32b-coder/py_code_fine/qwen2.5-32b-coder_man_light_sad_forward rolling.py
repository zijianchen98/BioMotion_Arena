
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24

# Initial positions of the lights (simplified model of a person)
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0.8], [-0.5, 0.6], [-0.5, 0.4],  # Left arm
    [0.5, 0.8], [0.5, 0.6], [0.5, 0.4],    # Right arm
    [-0.3, 0], [-0.3, -0.2], [-0.3, -0.4], # Left leg
    [0.3, 0], [0.3, -0.2], [0.3, -0.4]    # Right leg
])

# Function to update the position of the lights
def update(frame):
    t = frame / frames * 2 * np.pi
    # Simple forward rolling motion with a slight bounce effect
    positions = initial_positions.copy()
    positions[:, 1] -= 0.1 * np.sin(t + positions[:, 0] * 2)  # Vertical motion with phase shift
    positions[:, 0] += 0.05 * np.cos(t)  # Horizontal motion
    scatter.set_offsets(positions)
    return scatter,

# Setup figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1.5)
ax.axis('off')
ax.set_facecolor('black')

# Create scatter plot for the lights
scatter = ax.scatter([], [], s=100, c='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
