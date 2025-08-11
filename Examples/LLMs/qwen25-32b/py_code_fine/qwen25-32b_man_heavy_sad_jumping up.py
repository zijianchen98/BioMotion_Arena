
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis.
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Initial positions of the point-lights for a sadman jumping up.
points = [
    (5, 1),  # head
    (4, 2),  # left shoulder
    (6, 2),  # right shoulder
    (3, 3),  # left elbow
    (7, 3),  # right elbow
    (4, 4),  # left hand
    (6, 4),  # right hand
    (5, 5),  # torso
    (3, 6),  # left hip
    (7, 6),  # right hip
    (2, 7),  # left knee
    (8, 7),  # right knee
    (1, 8),  # left foot
    (9, 8),  # right foot
    (5, 9)   # tailbone
]

# Scatter plot for the point-lights.
scat = ax.scatter(*zip(*points), color='white', s=50)

# Constants for the animation.
AMPLITUDE = 1.0
FREQUENCY = 0.1
PHASE_OFFSETS = [i * 0.1 for i in range(len(points))]

def update(frame):
    new_points = []
    for i, (x, y) in enumerate(points):
        # Update the y-coordinate based on a sine wave to simulate jumping.
        displacement = AMPLITUDE * np.sin(FREQUENCY * frame + PHASE_OFFSETS[i])
        new_y = y + displacement
        new_points.append((x, new_y))
    scat.set_offsets(new_points)
    return scat,

# Create the animation.
anim = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
