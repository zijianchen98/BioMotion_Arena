
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the dots for the point-lights.
initial_dots_positions = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (0, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
    (-2, -1), (0, -2),
    (2, -1), (0, 2),
    (-1, 2), (1, 2)
]

# Create an empty figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

# Initialize the dots
dots = []
for x, y in initial_dots_positions:
    dot = plt.Circle((x, y), color='white', facecolor='white', lw=0)
    ax.add_artist(dot)
    dots.append(dot)

# Animation update function
def update(frame):
    for idx, (x, y) in enumerate(initial_dots_positions):
        dx, dy = np.cos(np.pi / 6 * frame), np.sin(np.pi / 6 * frame)
        dots[idx].center = x + dx, y + dy
    return dots

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 12), interval=100, blit=True)

# Show the animation
plt.axis('off')
plt.show()
