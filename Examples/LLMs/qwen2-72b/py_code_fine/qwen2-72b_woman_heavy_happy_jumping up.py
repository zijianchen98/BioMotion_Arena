
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions and velocities of the points
np.random.seed(0)
num_points = 15
positions = np.random.rand(num_points, 2) * 100
velocities = np.zeros((num_points, 2))

# Define the gravitational acceleration
gravity = np.array([0, -9.81])

def update(frame):
    global positions, velocities
    # Update velocities based on gravity and previous velocity
    velocities += gravity * 0.1  # Time step adjustment
    # Update positions based on velocities
    positions += velocities * 0.1
    # Bounce off the ground
    for i in range(num_points):
        if positions[i, 1] < 0:
            positions[i, 1] = 0
            velocities[i, 1] *= -0.7  # Damping factor

    scat.set_offsets(positions)
    return scat,

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
