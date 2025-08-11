
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the white point-lights on the body
def get_body_positions(t):
    t = t / 100.0  # Normalize time
    amplitude = 0.5
    height = 0.3 * np.sin(2 * np.pi * t)  # Vertical motion

    # Positions relative to the center of mass
    positions = np.array([
        [0, 0.5 + height],  # Head
        [-0.1, 0.4 + height], [-0.1, 0.2 + height], [-0.1, 0],  # Left leg
        [0.1, 0.4 + height], [0.1, 0.2 + height], [0.1, 0],  # Right leg
        [-0.2, 0.3], [0, 0.3], [0.2, 0.3],  # Waist level
        [-0.3, 0.3], [0.3, 0.3], [-0.3, 0.2], [0.3, 0.2],  # Shoulders and arms
    ])
    return positions

fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1)
ax.axis('off')

points = ax.plot([], [], 'wo', markersize=10)

def init():
    points[0].set_data([], [])
    return points

def update(frame):
    positions = get_body_positions(frame)
    points[0].set_data(positions[:, 0], positions[:, 1])
    return points

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=40)

plt.show()
