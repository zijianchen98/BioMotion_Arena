
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Parameters for the point-light locations (body parts)
lights = {
    'head': (0, 1),
    'shoulders': [(-0.5, 0.8), (0.5, 0.8)],
    'elbows': [(-0.7, 0.5), (0.7, 0.5)],
    'hands': [(-0.9, 0.2), (0.9, 0.2)],
    'body': (0, 0.6),
    'hips': [(-0.4, 0), (0.4, 0)],
    'knees': [(-0.4, -0.5), (0.4, -0.5)],
    'feet': [(-0.4, -1), (0.4, -1)]
}

# Combine points into an array
points = np.array([
    lights['head'],
    lights['shoulders'][0],
    lights['elbows'][0],
    lights['hands'][0],
    lights['body'],
    lights['hips'][0],
    lights['knees'][0],
    lights['feet'][0],
    lights['shoulders'][1],
    lights['elbows'][1],
    lights['hands'][1],
    lights['hips'][1],
    lights['knees'][1],
    lights['feet'][1],
])

# Create a scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    # Calculate new positions for waving
    new_points = points.copy()
    new_points[3, 1] += 0.1 * np.sin(frame / 10)  # Left hand
    new_points[9, 1] += 0.1 * np.sin(frame / 10)  # Right hand
    scat.set_offsets(new_points)
    return scat,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=50)

# Show the animation
plt.show()
