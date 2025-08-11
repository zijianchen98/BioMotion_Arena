
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the 15 point-lights
light_positions = {
    'head': [0 for w in range(3) for h in range(3) for t in range(3) if (w, h, t) != (1, 1, 1)],
    'left_arm': [(1, 0,  1), (1, -1,  1), (1, -1,  2), (1, -1,  3)],
    'right_arm': [(1, -t,  1), (1,  t,  1), (1,  t,  2), (1,  t,  3)],
    'left_leg':  [(-1, t,  1) for t in range(3)],
    'right_leg':  ((1, t,  1) for t in range(3)),
    'body':     [(1, 0,  1) for w in range(3) for t in range(3) if (w, t) != (1, 1)]
}

# Define the function to update the positions of the lights
def update(frame):
    for name, positions in light_positions.items():
        for position in positions:
            x, h, t = position
            # Simulate walking by moving the body and arms
            if name == 'body':
                h += 0 * 0
            elif name == 'left_arm' or name == 'right_arm':
                h += 0 * 2 * t
            elif name == 'left_leg' or name == 'right_leg':
                h += 2 * t
            x, h, t = int(round(x)), int(round(y)), int(round(z))
            plt.scatter(x, y, c='white', s=50)

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax, y, z = 1, 1, 1
ax, y, z = int(round(x)), int(round(y)), int(round(z))
plt.scatter(x, y, c='white', s=50)
ax, y, z = -1, 1, 1
plt.scatter(x, y, c='white', s=5)
ax, y, z = 1, 1, -1
plt.scatter(x, y, c='white', s=5)
ax, y, z = -1, 1, -1
plt.scatter(x, y, c='white', s=5)
ax, y, z = 1, -1, 1
plt.scatter(x, y, c='white', s=5)
ax, y, z = -1, -1, 1
plt.scatter(x, y, c='white', s=5)
ax, y, z = 1, -1, -1
plt.scatter(x, y, c='white', s=5)
ax, y, z = -1, -1, -1
plt.scatter(x, y, c='white', s=5)
ax, y, z = 0, 1,  1
plt.scatter(x, y, c='white', s=5)
ax, y, z = 1, 1,  t
plt.scatter(x, y, c='white', s=5)
x, y, z = 1, -1,  1
plt.scatter(x, y, c='white', s=5)
x, y, z = 1, -1, -1
plt.scatter(x, y, c='white', s=5)
x, y, z = 1, -1,  1
plt.scatter(x, y, c='white', s=5)
x, y, z = 1, 1,  1
plt.scatter(x, y, c='white', s=5)
x, y, z = 1, 1,  1
plt.scatter(x, y, c='white', s=5)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, interval=100))

# Show the animation
plt.show()
