
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 120
fps = 24

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the point lights (simplified model)
positions = np.array([
    [0.0, 0.0],  # Head
    [-0.05, 0.1], [-0.05, 0.2], [-0.05, 0.3],  # Left arm
    [0.05, 0.1], [0.05, 0.2], [0.05, 0.3],  # Right arm
    [0.0, -0.1], [-0.05, -0.1], [0.05, -0.1],  # Torso
    [-0.1, -0.2], [-0.15, -0.3], [-0.15, -0.4],  # Left leg
    [0.1, -0.2], [0.15, -0.3], [0.15, -0.4]   # Right leg
])

# Scatter plot for the point lights
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=100)

def update(frame):
    # Waving motion parameters
    amplitude = 0.1
    frequency = 0.5
    phase_shift = np.pi / 2
    
    # Update right arm positions for waving effect
    new_positions = positions.copy()
    new_positions[5, 1] += amplitude * np.sin(2 * np.pi * frequency * frame / frames + phase_shift)
    new_positions[6, 1] += amplitude * np.sin(2 * np.pi * frequency * frame / frames + phase_shift)
    
    scat.set_offsets(new_positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
