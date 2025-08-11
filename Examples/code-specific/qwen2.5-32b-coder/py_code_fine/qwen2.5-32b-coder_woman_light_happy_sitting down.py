
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 200
fps = 24

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the lights (approximate starting position for sitting down)
positions = np.array([
    [-0.2, 0.8], [-0.1, 0.7], [0.0, 0.7], [0.1, 0.7], [0.2, 0.8],  # Head
    [-0.1, 0.6], [0.1, 0.6],                                      # Shoulders
    [0.0, 0.4],                                                  # Chest
    [0.0, 0.2],                                                  # Waist
    [-0.1, 0.0], [0.1, 0.0],                                      # Hips
    [-0.1, -0.2], [0.1, -0.2],                                    # Knees
    [-0.1, -0.4], [0.1, -0.4]                                     # Ankles
])

# Scatter plot for the point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

def update(frame):
    t = frame / frames * 2 * np.pi  # Time variable for smooth motion

    # Update positions for sitting down motion
    new_positions = np.copy(positions)

    # Head bobbing slightly
    new_positions[:5, 1] += 0.02 * np.sin(t)

    # Shoulder movement
    new_positions[5:7, 0] += 0.05 * np.sin(t + np.pi / 2)

    # Chest movement
    new_positions[7, 1] += 0.02 * np.sin(t)

    # Waist movement
    new_positions[8, 1] += 0.02 * np.sin(t)

    # Hip movement
    new_positions[9:11, 1] += 0.02 * np.sin(t)

    # Knee movement
    new_positions[11:13, 1] += 0.1 * np.sin(t + np.pi)

    # Ankle movement
    new_positions[13:, 1] += 0.1 * np.sin(t + np.pi)

    scatter.set_offsets(new_positions)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
