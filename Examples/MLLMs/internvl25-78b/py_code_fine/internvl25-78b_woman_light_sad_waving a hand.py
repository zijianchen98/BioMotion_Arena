
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Number of points
num_points = 15

# Initial positions of points
points = np.array([
    [0.5, 0.9],
    [0.3, 0.8], [0.5, 0.8], [0.7, 0.8],
    [0.25, 0.7], [0.45, 0.7], [0.55, 0.7], [0.75, 0.7],
    [0.2, 0.6], [0.4, 0.6], [0.6, 0.6], [0.8, 0.6],
    [0.3, 0.5], [0.5, 0.5], [0.7, 0.5]
])

dots, = ax.plot(points[:, 0], points[:, 1], 'wo', markersize=5)

def init():
    dots.set_data(points[:, 0], points[:, 1])
    return dots,

def animate(frame):
    # Sine wave motion for hand
    amplitude = 0.05
    frequency = 0.02
    wave = amplitude * np.sin(frequency * frame)

    # Update points positions for waving hand
    moving_points = points.copy()
    moving_points[0, 0] += wave
    moving_points[1:4, 0] += wave / 2

    dots.set_data(moving_points[:, 0], moving_points[:, 1])
    return dots,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.show()
