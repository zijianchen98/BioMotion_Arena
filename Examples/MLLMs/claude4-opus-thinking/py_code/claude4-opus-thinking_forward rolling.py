
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_lights = 15

# Define position for the point lights
# Assuming a basic forward roll pattern with key frames
# This is illustrative; you might refine the angles and movement based on biomechanics
key_frames = [
    np.array([[0, 1], [0, 0.5], [0, 0], [0, -0.5], [0, -1], 
               [-1, -1], [-1, -0.5], [-1, 0], [-1, 0.5], [-1, 1],
               [-2, -1], [-2, -0.5], [-2, 0], [-2, 0.5], [-2, 1]]),
    np.array([[1, 1], [0.5, 0.5], [0, 0], [-0.5, -0.5], [-1, -1], 
               [0, -2], [0.5, -2], [1, -2], [1.5, -1.5], [1, -1],
               [0, -2], [0.5, -2], [1, -2], [1.5, -1.5], [1, -1]]),
    np.array([[0, 1], [0.5, 0.5], [1, 0], [1, -0.5], [1, -1], 
               [0.5, -2], [0, -2], [-0.5, -2], [-1, -1.5], [-1, -1],
               [-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2]]),
]

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Loop over the key frames to create smooth animation
    if frame < len(key_frames):
        pos = key_frames[frame]
    else:
        pos = key_frames[-1]  # Hold the last position

    points.set_data(pos[:, 0], pos[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(key_frames), init_func=init,
                              interval=300, blit=True)

# Show the animation
plt.show()
