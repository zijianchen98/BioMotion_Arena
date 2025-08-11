
import numpy as np
import matplotlib.pyplot as plt

# Coordinates for the happyman in a sitting position
happyman_points = {
    'head': (np.random.uniform(0.1, 0.9, 2), np.random.uniform(0.1, 0.7, 2)),
    'body': (np.random.uniform(0.3, 0.8, 2), np.random.uniform(0.2, 0.6, 2)),
    'left_arm': (np.random.uniform(0.4, 0.6, 2), np.random.uniform(0.5, 0.8, 2)),
    'right_arm': (np.random.uniform(0.6, 0.8, 2), np.random.uniform(0.5, 0.8, 2)),
    'left_leg': (np.random.uniform(0.7, 0.9, 2), np.random.uniform(0.2, 0.5, 2)),
    'right_leg': (np.random.uniform(0.3, 0.5, 2), np.random.uniform(0.2, 0.5, 2))
}

# Generate 300 frames for smooth motion
num_frames = 300
positions = {}

for key in happyman_points:
    positions[key] = [happyman_points[key] for _ in range(num_frames)]
    for frame in range(num_frames):
        delta = np.random.uniform(-0.01, 0.01, 2)
        positions[key][frame] = (positions[key][frame][0] + delta[0] % 1, positions[key][frame][1] + delta[1] % 0.4)

# Draw the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
for frame in range(num_frames):
    ax.clear()
    for key in positions:
        x, y = positions[key][frame]
        ax.add_patch(plt.Circle((x, y), 0.05, color='white'))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.pause(0.02)

plt.show()
