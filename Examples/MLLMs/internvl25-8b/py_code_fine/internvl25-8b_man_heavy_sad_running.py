
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_points(i):
    for j in range(8):
        points[j].set_data(pos1[j][0] + np.sin(np.pi * i / 60 + 0.03 * i + 0.02 * i ** 2) * 0.1,
                           pos1[j][1] + np.sin(np.pi * i / 60 + 0.03 * i + 0.02 * i ** 2) * 0.1)
    points[8].set_data(pos2[0] + np.sin(np.pi * i / 60 + 0.03 * i + 0.02 * i ** 2) * 0.1,
                        pos2[1])

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Define initial positions for the 15 lights
pos1 = [(0, 0), (0, 0.25), (0, 0.45), (0, 0.6), (0, 0.6), (0, 0.45), (0, 0.3), (0, 0.15), (0, 0.15),
        (0, 0.1), (0.25, 0.1), (0.25, 0.15), (0.25, 0.3), (0.25, 0.45), (0.4, 0.5)]
pos2 = [(0.6, 0), (0.6, 0.5), (0.6, 0.5), (0.6, 0.5), (0.75, 0.8), (0.75, 0.85), (0.75, 0.85), (0.75, 0.85),
        (0.8, 0.9), (0.8, 0.85), (0.8, 0.85), (0.8, 0.85), (0.8, 0.8), (0.8, 0.75), (0.8, 0.7)]

# Create the 15 white point-lights
points = [plt.plot([], [], 'o', color='white', markersize=2)[0] for _ in range(15)]
points[8].set_data(pos2[0], pos2[1])

# Run the animation
ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0, 600), interval=25, blit=True)
plt.show()
