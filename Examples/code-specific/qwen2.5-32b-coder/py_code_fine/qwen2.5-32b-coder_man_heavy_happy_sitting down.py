
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = fps * duration

# Initialize positions for the lights
positions = np.zeros((num_lights, 2))
velocities = np.zeros_like(positions)

# Define initial positions for a 'happyman' sitting down
def initialize_positions():
    global positions
    # Head
    positions[0] = [0.5, 0.8]
    # Torso
    positions[1] = [0.5, 0.6]
    positions[2] = [0.4, 0.6]
    positions[3] = [0.6, 0.6]
    # Arms
    positions[4] = [0.4, 0.7]
    positions[5] = [0.6, 0.7]
    positions[6] = [0.3, 0.8]
    positions[7] = [0.7, 0.8]
    # Legs
    positions[8] = [0.4, 0.5]
    positions[9] = [0.6, 0.5]
    positions[10] = [0.3, 0.4]
    positions[11] = [0.7, 0.4]
    # Feet
    positions[12] = [0.3, 0.3]
    positions[13] = [0.7, 0.3]
    # Happy face
    positions[14] = [0.5, 0.85]

# Define the motion for sitting down
def update_positions(frame):
    global positions
    t = frame / frames
    # Move torso down
    positions[1][1] -= 0.1 * np.sin(np.pi * t)
    positions[2][1] -= 0.1 * np.sin(np.pi * t)
    positions[3][1] -= 0.1 * np.sin(np.pi * t)
    # Move arms up
    positions[4][1] += 0.05 * np.sin(np.pi * t)
    positions[5][1] += 0.05 * np.sin(np.pi * t)
    # Move legs down
    positions[8][1] -= 0.1 * np.sin(np.pi * t)
    positions[9][1] -= 0.1 * np.sin(np.pi * t)
    # Move feet down
    positions[12][1] -= 0.1 * np.sin(np.pi * t)
    positions[13][1] -= 0.1 * np.sin(np.pi * t)

# Setup plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

# Animation function
def animate(frame):
    update_positions(frame)
    scat.set_offsets(positions)
    return scat,

# Initialize positions
initialize_positions()

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
