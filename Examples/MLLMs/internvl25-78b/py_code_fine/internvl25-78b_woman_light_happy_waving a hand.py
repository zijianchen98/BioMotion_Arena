
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

num_points = 15
points = np.array([
    [5, 3], [5.2, 3.2], [4.8, 3.2],  # Head
    [4.5, 4], [4.8, 4], [5.2, 4], [5.5, 4],  # Shoulders
    [4, 5], [4.3, 5], [5.7, 5], [6, 5],  # Upper body
    [4.2, 6], [4.5, 6], [5.5, 6], [5.8, 6],  # Lower body
    [4.5, 7], [5.5, 7]  # Legs
])

scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    amplitude = 0.5
    frequency = 0.05
    wave = np.sin(frame * frequency) * amplitude
    points[9:11, 0] += wave  # Moving right arm for waving
    scatter.set_offsets(points)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.axis('off')
plt.show()
