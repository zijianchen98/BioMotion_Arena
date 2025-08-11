
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
point_lights = [
    # Head
    [0, 10],
    # Torso
    [-2, 5], [2, 5],
    # Left arm
    [-4, 3], [-6, 2], [-8, 1],
    # Right arm
    [4, 3], [6, 2], [8, 1],
    # Left leg
    [-2, -2], [-4, -4], [-6, -6],
    # Right leg
    [2, -2], [4, -4], [6, -6]
]

# Define the jumping motion
def jumping_motion(frame):
    motion = []
    for i, point in enumerate(point_lights):
        x, y = point
        if i < 3:  # Head and torso
            y += np.sin(frame / 10.0) * 2
        elif i < 6:  # Left arm
            y += np.sin(frame / 10.0 + np.pi / 2) * 2
        elif i < 9:  # Right arm
            y += np.sin(frame / 10.0 - np.pi / 2) * 2
        elif i < 12:  # Left leg
            y += np.sin(frame / 10.0) * 4
        else:  # Right leg
            y += np.sin(frame / 10.0 - np.pi) * 4
        motion.append([x, y])
    return motion

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 15)
ax.set_facecolor('black')

# Create the point-light plot
def update(frame):
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 15)
    ax.set_facecolor('black')
    motion = jumping_motion(frame)
    for point in motion:
        ax.plot(point[0], point[1], 'o', markersize=5, color='white')

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
