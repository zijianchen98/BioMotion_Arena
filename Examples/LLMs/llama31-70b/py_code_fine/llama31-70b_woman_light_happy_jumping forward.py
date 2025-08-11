
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the happy woman
# Each row represents a point-light with (x, y, z) coordinates
points = np.array([
    [0, 0, 0],  # Head
    [-0.5, 0.5, 0], [-0.5, -0.5, 0],  # Shoulders
    [0, 1, 0],  # Neck
    [-1, 1.5, 0], [-1, -1.5, 0],  # Elbows
    [-1.5, 2, 0], [-1.5, -2, 0],  # Hands
    [0, -1, 0],  # Hips
    [-0.5, -2, 0], [-0.5, -3, 0],  # Knees
    [-1, -2.5, 0], [-1, -3.5, 0],  # Ankles
    [-1.5, -3, 0], [-1.5, -4, 0]  # Toes
])

# Define the jumping motion
# Each row represents a frame with 15 point-lights
frames = 100
jumping_motion = np.zeros((frames, 15, 3))

for i in range(frames):
    t = i / frames
    jumping_motion[i] = points + np.array([
        [0, 0, 0],  # Head
        [-0.1 * np.sin(2 * np.pi * t), 0.1 * np.cos(2 * np.pi * t), 0],
        [0.1 * np.sin(2 * np.pi * t), 0.1 * np.cos(2 * np.pi * t), 0],  # Shoulders
        [0, 0.2 * np.sin(np.pi * t), 0],  # Neck
        [-0.2 * np.sin(2 * np.pi * t), 0.2 * np.cos(2 * np.pi * t), 0],
        [0.2 * np.sin(2 * np.pi * t), 0.2 * np.cos(2 * np.pi * t), 0],  # Elbows
        [-0.3 * np.sin(2 * np.pi * t), 0.3 * np.cos(2 * np.pi * t), 0],
        [0.3 * np.sin(2 * np.pi * t), 0.3 * np.cos(2 * np.pi * t), 0],  # Hands
        [0, -0.2 * np.sin(np.pi * t), 0],  # Hips
        [-0.1 * np.sin(2 * np.pi * t), -0.2 * np.cos(2 * np.pi * t), 0],
        [0.1 * np.sin(2 * np.pi * t), -0.2 * np.cos(2 * np.pi * t), 0],  # Knees
        [-0.2 * np.sin(2 * np.pi * t), -0.3 * np.cos(2 * np.pi * t), 0],
        [0.2 * np.sin(2 * np.pi * t), -0.3 * np.cos(2 * np.pi * t), 0],  # Ankles
        [-0.3 * np.sin(2 * np.pi * t), -0.4 * np.cos(2 * np.pi * t), 0],
        [0.3 * np.sin(2 * np.pi * t), -0.4 * np.cos(2 * np.pi * t), 0]  # Toes
    ])

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

points_plot = ax.scatter(jumping_motion[0, :, 0], jumping_motion[0, :, 1], s=50, c='white')

def animate(i):
    points_plot.set_offsets(jumping_motion[i, :, :2])
    return points_plot,

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50)

plt.show()
