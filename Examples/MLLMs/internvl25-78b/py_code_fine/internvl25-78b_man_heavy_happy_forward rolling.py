
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define point positions for a happy man with a round body
points = {
    'head': [0, 1],
    'shoulders': [-0.5, 0.8, 0.5, 0.8],
    'elbows': [-0.7, 0.5, 0.7, 0.5],
    'hands': [-0.8, 0.2, 0.8, 0.2],
    'waist': [-0.3, 0, 0.3, 0],
    'hips': [-0.4, -0.2, 0.4, -0.2],
    'knees': [-0.5, -0.5, 0.5, -0.5],
    'feet': [-0.6, -0.7, 0.6, -0.7]
}

def roll(position, angle):
    c, s = np.cos(angle), np.sin(angle)
    matrix = np.array(((c, -s), (s, c)))
    return np.dot(position, matrix)

def update(frame):
    angle = frame * 0.1
    new_points = {}

    for key, pos in points.items():
        new_points[key] = roll(np.array(pos).reshape(-1, 2), angle).flatten()

    scat.set_offsets(np.array([
        new_points['head'],
        new_points['shoulders'],
        new_points['elbows'],
        new_points['hands'],
        new_points['waist'],
        new_points['hips'],
        new_points['knees'],
        new_points['feet']
    ]).flatten())

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Initial scatter points
scat = ax.scatter([], [], s=50, color='white')

# Update function for the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()
