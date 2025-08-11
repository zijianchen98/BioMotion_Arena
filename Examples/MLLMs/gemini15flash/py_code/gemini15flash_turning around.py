
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 5], [2, 7],
    [3, 2], [3, 4], [3, 6], [3, 8], [4, 3], [4, 7],
    [5, 2], [5, 8], [6, 5]
])

# Define the animation frames
num_frames = 100
frames = []
for i in range(num_frames):
    angle = 2 * np.pi * i / num_frames
    rotated_positions = np.copy(initial_positions)

    # Rotate the point-lights around the center
    center = np.mean(initial_positions, axis=0)
    rotated_positions[:, 0] -= center[0]
    rotated_positions[:, 1] -= center[1]
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_positions = np.dot(rotated_positions, rotation_matrix)
    rotated_positions[:, 0] += center[0]
    rotated_positions[:, 1] += center[1]
    frames.append(rotated_positions)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

scat = ax.scatter([], [], s=50, c='white')

def animate(i):
    scat.set_offsets(frames[i])
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=50, blit=True)

# Save the animation as a GIF
ani.save('biological_motion.gif', writer='imagemagick', fps=20)  # Requires ImageMagick

plt.show()

