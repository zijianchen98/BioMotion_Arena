
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
def initial_positions():
    positions = np.zeros((15, 2))

    # Head
    positions[0] = np.array([0, 10])

    # Torso
    positions[1] = np.array([0, 7])
    positions[2] = np.array([0, 4])

    # Right arm
    positions[3] = np.array([2, 6])
    positions[4] = np.array([4, 5])
    positions[5] = np.array([6, 4])
    positions[6] = np.array([8, 3])  # Hand

    # Left arm
    positions[7] = np.array([-2, 6])
    positions[8] = np.array([-4, 5])
    positions[9] = np.array([-6, 4])
    positions[10] = np.array([-8, 3])  # Hand

    # Right leg
    positions[11] = np.array([2, 2])
    positions[12] = np.array([4, 0])
    positions[13] = np.array([6, -2])

    # Left leg
    positions[14] = np.array([-2, 2])

    return positions

# Define the movement of the point-lights
def move_points(positions, frame):
    new_positions = positions.copy()

    # Move the head
    new_positions[0, 1] = 10 + 0.5 * np.sin(frame / 10.0)

    # Move the torso
    new_positions[1, 1] = 7 + 0.2 * np.sin(frame / 10.0)
    new_positions[2, 1] = 4 + 0.1 * np.sin(frame / 10.0)

    # Move the right arm
    new_positions[3, 0] = 2 + 0.5 * np.sin(frame / 5.0)
    new_positions[3, 1] = 6 + 0.2 * np.sin(frame / 5.0)
    new_positions[4, 0] = 4 + 0.7 * np.sin(frame / 5.0)
    new_positions[4, 1] = 5 + 0.3 * np.sin(frame / 5.0)
    new_positions[5, 0] = 6 + 0.9 * np.sin(frame / 5.0)
    new_positions[5, 1] = 4 + 0.4 * np.sin(frame / 5.0)
    new_positions[6, 0] = 8 + 1.1 * np.sin(frame / 5.0)
    new_positions[6, 1] = 3 + 0.5 * np.sin(frame / 5.0)

    # Move the left arm
    new_positions[7, 0] = -2 + 0.5 * np.sin(frame / 5.0 + np.pi)
    new_positions[7, 1] = 6 + 0.2 * np.sin(frame / 5.0 + np.pi)
    new_positions[8, 0] = -4 + 0.7 * np.sin(frame / 5.0 + np.pi)
    new_positions[8, 1] = 5 + 0.3 * np.sin(frame / 5.0 + np.pi)
    new_positions[9, 0] = -6 + 0.9 * np.sin(frame / 5.0 + np.pi)
    new_positions[9, 1] = 4 + 0.4 * np.sin(frame / 5.0 + np.pi)
    new_positions[10, 0] = -8 + 1.1 * np.sin(frame / 5.0 + np.pi)
    new_positions[10, 1] = 3 + 0.5 * np.sin(frame / 5.0 + np.pi)

    # Move the legs
    new_positions[11, 1] = 2 + 0.2 * np.sin(frame / 10.0)
    new_positions[12, 1] = 0 + 0.3 * np.sin(frame / 10.0)
    new_positions[13, 1] = -2 + 0.4 * np.sin(frame / 10.0)
    new_positions[14, 1] = 2 + 0.2 * np.sin(frame / 10.0 + np.pi)

    return new_positions

# Create a new figure
fig, ax = plt.subplots()

# Initialize the point-lights
positions = initial_positions()
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='w')

# Set the limits and background color
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 15)
ax.set_facecolor('k')
ax.set_aspect('equal')

# Animation function
def animate(frame):
    new_positions = move_points(positions, frame)
    scatter.set_offsets(new_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
