
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
POINT_SIZE = 20
STARTING_POSITIONS = [np.random.rand(2) for _ in range(NUM_POINTS)]
TIMESTEPS = 60

# Initialize figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')
circles = [ax.scatter(i, j, s=POINT_SIZE, color='white') for i, j in STARTING_POSITIONS]

def update(frame):
    # Update positions
    for i, (x, y) in enumerate(STARTING_POSITIONS):
        if frame < TIMESTEPS // 2:
            # Jumping up
            vx = 0
            vy = 0.03
            STARTING_POSITIONS[i] = (x + vx * 0.1, y + vy * 0.1)
            circles[i].set_offsets(STARTING_POSITIONS[i])
        else:
            # Falling down smoothly
            vy *= 0.9
            STARTING_POSITIONS[i] = (x, y - vy * 0.1)
            circles[i].set_offsets(STARTING_POSITIONS[i])

    return circles

# Animation object
ani = animation.FuncAnimation(fig, update, frames=TIMESTEPS, repeat=False)

plt.show()
