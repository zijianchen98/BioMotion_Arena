
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial positions of the point-lights for the sadman with heavy weight bowing
initial_positions = np.array([
    [0.0, 1.0],  # Head
    [-0.1, 0.8], [-0.1, 0.6], [-0.1, 0.4],  # Left arm
    [0.1, 0.8], [0.1, 0.6], [0.1, 0.4],  # Right arm
    [0.0, 0.2],  # Torso
    [-0.2, 0.0], [0.2, 0.0],  # Hips
    [-0.3, -0.2], [-0.1, -0.2], [0.1, -0.2], [0.3, -0.2]  # Legs
])

# Define the animation
def update(frame):
    positions = initial_positions.copy()
    positions[0, 1] = np.sin(np.deg2rad(frame)) + 0.6  # Head movement
    positions[5:8, 1] = np.sin(np.deg2rad(frame)) + 0.2  # Arm movement
    positions[0, 1] -= 0.1 * np.abs(np.sin(np.deg2rad(frame * 2)))  # Torso bowing
    positions[8:10, 1] -= 0.1 * np.abs(np.sin(np.deg2rad(frame)))  # Hips movement
    positions[10:, 1] -= 0.1 * np.abs(np.sin(np.deg2rad(frame)))  # Legs movement

    scat.set_offsets(positions)
    return scat,

fig = plt.figure(figsize=(4, 6))
ax = plt.axes(xlim=(-1, 1), ylim=(-2, 2))
ax.axis('off')

scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

anim = animation.FuncAnimation(fig, update, frames=360, interval=50, blit=True)

plt.show()
