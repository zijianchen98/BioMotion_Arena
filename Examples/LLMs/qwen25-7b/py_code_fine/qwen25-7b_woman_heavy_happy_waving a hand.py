
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the points
num_points = 15
initial_positions = np.random.rand(num_points, 2) * 8 - 4  # Random initial positions within [-4, 4]

# Define the target positions for each points based on the hand-waving motion
target_positions = np.array([
    [0[0] + 1 if t % 4 == 0 else 0[0] - 1 if t % 4 == 2 else  t[0] for t in range(15) ]
    for t in range(-2, 10)  # 13 frames to cover the wave motion
])

def update_points(frame):
    for i, pos in enumerate(initial_positions):
        x[i][0] = target_positions[frame, i]
    return initial_positions,

fig, ax = plt.subplots()
ax, = ax.plot([], [], 'o', color='white')

def init():
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    return

ani = animation.FuncAnimation(fig, update_points, frames=len(target_positions), init_func=init, blit=True)
plt.show()
