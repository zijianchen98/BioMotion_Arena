
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial position of the points
positions = np.zeros((15, 2))

# Define the initial velocities of the points
velocities = np.random.uniform(-1, 1, size=(15, 2))

# Define the acceleration due to gravity
acceleration = np.array([0, -9.8])

# Define the time step
dt = 0.1

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_facecolor('black')

# Define the scatter plot
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

def update(frame):
    # Update the positions of the points
    global positions, velocities
    velocities += acceleration * dt
    positions += velocities * dt

    # Update the scatter plot
    scatter.set_offsets(positions)

    # Add a jump condition
    if frame == num_frames // 2:
        velocities += np.array([0, 10])

    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
