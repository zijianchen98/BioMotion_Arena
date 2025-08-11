
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Define initial positions for 15 point-lights (simplified human stick figure)
# Head, shoulders, elbows, wrists, hips, knees, ankles, and torso points
initial_positions = np.array([
    [0, 10],  # Head
    [-2, 8], [2, 8],  # Shoulders
    [-3, 6], [3, 6],  # Elbows
    [-4, 4], [4, 4],  # Wrists
    [0, 0], [-1, -2], [1, -2],  # Hips, Knees
    [-2, -4], [0, -4], [2, -4],  # Ankles
    [-1, 2], [1, 2]  # Torso
])

# Number of frames for one jump cycle
frames = 30
positions = np.zeros((frames, 15, 2))

# Simulate jumping forward motion (simplified biomechanics)
for i in range(frames):
    t = i / frames * 2 * np.pi  # Cycle through one jump
    # Forward movement
    forward_x = i * 0.5
    # Vertical movement (jump arc)
    jump_y = 5 * np.sin(t) - 5
    # Limb movements
    positions[i] = initial_positions + [forward_x, jump_y]
    # Simple limb articulation (e.g., arms and legs bending)
    positions[i, 3:5] = positions[i, 1:3] + [[-1.5 * np.cos(t), -2 * np.sin(t)], [1.5 * np.cos(t), -2 * np.sin(t)]]  # Elbows
    positions[i, 6:9] = positions[i, 4:7] + [[-2 * np.cos(t), -3 * np.sin(t)], [0, -3 * np.sin(t)], [2 * np.cos(t), -3 * np.sin(t)]]  # Knees to ankles

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 20)
ax.set_ylim(-10, 10)
ax.axis('off')

# Scatter plot for point-lights
scat = ax.scatter([], [], c='white', s=100)

def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

ani = FuncAnimation(fig, update, frames=range(frames), interval=50, blit=True)

# Save animation (uncomment to save)
# ani.save('jumping_man.gif', writer='pillow')

plt.show()
