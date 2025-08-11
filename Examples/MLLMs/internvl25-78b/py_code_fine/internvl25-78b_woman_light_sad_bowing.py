
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Points representing a sad woman bowing
points = np.array([
    [0.3, 0.9], [0.4, 0.8], [0.5, 0.9], [0.6, 0.8], [0.7, 0.9],  # Head
    [0.35, 0.7], [0.45, 0.6], [0.55, 0.6], [0.65, 0.7],  # Upper body
    [0.4, 0.5], [0.6, 0.5],  # Shoulders
    [0.33, 0.4], [0.67, 0.4],  # Elbows
    [0.30, 0.3], [0.70, 0.3],  # Hands
    [0.5, 0.2]  # Waist
])

# Create point-light objects
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def init():
    scat.set_offsets(points)
    return scat,

def update(frame):
    global points
    # Define bowing motion
    if frame < 20:
        points[:, 1] -= 0.01 * (frame - 10)
    else:
        points[:, 1] += 0.01 * (frame - 20)
    
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=40, init_func=init, blit=True, repeat=True)

plt.show()
