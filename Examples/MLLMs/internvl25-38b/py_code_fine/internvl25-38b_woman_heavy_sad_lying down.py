
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Number of lights
num_lights = 15

# Initial positions for the point-lights
positions = np.array([
    [0, 0],
    [1, 0.5],
    [-1, 0.5],
    [1.5, -1],
    [-1.5, -1],
    [0.5, -2],
    [-0.5, -2],
    [2, -3],
    [-2, -3],
    [1, -4],
    [-1, -4],
    [0.5, -5],
    [-0.5, -5],
    [0.25, -6],
    [-0.25, -6]
])

# Initial velocities (to simulate realistic movement)
velocities = np.zeros_like(positions)

# Function to update positions
def update(frame):
    global positions, velocities

    # Update positions based on velocities
    positions += velocities

    # Simulate a slow lying down motion
    if frame < 25:
        velocities += np.array([0, -0.02])
    elif 25 <= frame < 50:
        velocities += np.array([0, 0.02])

    # Boundary conditions to prevent lights from moving out of frame
    for i in range(len(positions)):
        if positions[i][1] < -6:
            velocities[i][1] = 0.02
        elif positions[i][1] > 0:
            velocities[i][1] = -0.02

    # Clear the axis and redraw the lights
    ax.clear()
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=75, interval=50)

# Display the animation
plt.show()
