
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set the coordinates for each frame of the jump
frames = [
    [(4, 3), (5, 4), (6, 3), (5, 2), (4, 1), (5, 0), (6, 0), (7, 1), (6, 2), (5, 3), (6, 4), (5, 5), (6, 6), (5, 7), (6, 5)],
    [(4, 5), (5, 6), (6, 5), (5, 4), (4, 3), (3, 2), (6, 2), (7, 3), (6, 4), (5, 5), (6, 6), (5, 7), (6, 8), (5, 9), (6, 7)],
    [(4, 8), (5, 9), (6, 8), (5, 7), (4, 6), (3, 5), (6, 5), (7, 6), (6, 7), (5, 8), (6, 9), (5, 10), (6, 11), (5, 12), (6, 10)],
    [(4, 12), (5, 13), (6, 12), (5, 11), (4, 10), (3, 9), (6, 9), (7, 10), (6, 11), (5, 12), (6, 13), (5, 14), (6, 15), (5, 16), (6, 14)],
    [(4, 16), (5, 17), (6, 16), (5, 15), (4, 14), (3, 13), (6, 13), (7, 14), (6, 15), (5, 16), (6, 17), (5, 18), (6, 19), (5, 1), (6, 18)]
]

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 8)
ax.set_ylim(0, 19)
ax.set_aspect('equal')
ax.set_facecolor('black')
scatter = ax.scatter([], [])

def update(frame):
    scatter.set_offsets(frame)
    return scatter,

def animate(i):
    if i < len(frames):
        scatter.set_offsets(frames[i])
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=50, blit=True)
plt.axis('off')
plt.show()
