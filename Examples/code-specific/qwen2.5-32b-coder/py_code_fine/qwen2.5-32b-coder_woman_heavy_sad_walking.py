
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 240  # 4 seconds at 60 FPS
num_points = 15

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Define initial positions
def init():
    points.set_data([], [])
    return points,

# Define the update function for the animation
def update(frame):
    t = frame / 60  # time in seconds

    # Positions of the points representing a walking person with heavy weight
    x_positions = [
        -0.1 + 0.05 * np.sin(t + 0.5),
        0.1 + 0.05 * np.sin(t),
        -0.1 + 0.05 * np.sin(t + 0.5),
        0.1 + 0.05 * np.sin(t),
        -0.1 + 0.05 * np.sin(t + 0.5),
        0.1 + 0.05 * np.sin(t),
        -0.1 + 0.05 * np.sin(t + 0.5),
        0.1 + 0.05 * np.sin(t),
        -0.1 + 0.05 * np.sin(t + 0.5) - 0.05 * np.cos(2*t),
        0.1 + 0.05 * np.sin(t) + 0.05 * np.cos(2*t),
        -0.1 + 0.05 * np.sin(t + 0.5) - 0.05 * np.cos(2*t),
        0.1 + 0.05 * np.sin(t) + 0.05 * np.cos(2*t),
        -0.1 + 0.05 * np.sin(t + 0.5) - 0.05 * np.cos(2*t),
        0.1 + 0.05 * np.sin(t) + 0.05 * np.cos(2*t),
        0.0
    ]

    y_positions = [
        0.9 - 0.1 * np.cos(t),
        0.9 - 0.1 * np.cos(t),
        0.7 - 0.1 * np.cos(t + 0.5),
        0.7 - 0.1 * np.cos(t + 0.5),
        0.5 - 0.1 * np.cos(t),
        0.5 - 0.1 * np.cos(t),
        0.3 - 0.1 * np.cos(t + 0.5),
        0.3 - 0.1 * np.cos(t + 0.5),
        0.1 - 0.1 * np.cos(t) - 0.05 * np.sin(2*t),
        0.1 - 0.1 * np.cos(t) + 0.05 * np.sin(2*t),
        -0.1 - 0.1 * np.cos(t + 0.5) - 0.05 * np.sin(2*t),
        -0.1 - 0.1 * np.cos(t + 0.5) + 0.05 * np.sin(2*t),
        -0.3 - 0.1 * np.cos(t) - 0.05 * np.sin(2*t),
        -0.3 - 0.1 * np.cos(t) + 0.05 * np.sin(2*t),
        -0.5
    ]

    points.set_data(x_positions, y_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=16.67)

plt.show()
