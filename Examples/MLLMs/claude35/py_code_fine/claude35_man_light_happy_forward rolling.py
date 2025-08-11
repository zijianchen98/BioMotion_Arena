
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize parameters
num_points = 15
frames = 100
interval = 50  # milliseconds

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create point-light positions
def create_initial_positions():
    positions = np.zeros((num_points, 2))
    # Define initial positions for a forward roll
    # You can tweak these for a more realistic motion
    for i in range(num_points):
        positions[i, 0] = (i % 3) - 1  # x-coordinates
        positions[i, 1] = -1 - (i // 3) * 0.5  # y-coordinates
    return positions

# Generate the motion path
def update_positions(frame):
    # Calculate new positions
    for i in range(num_points):
        # Simulate forward rolling motion using sine and cosine functions
        positions[i, 0] += 0.05 * np.cos(frame * 0.1 + i)
        positions[i, 1] += 0.05 * np.sin(frame * 0.1 + i)

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Initial positions
positions = create_initial_positions()
points, = plt.plot([], [], 'o', color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=frames, interval=interval, blit=True)

# Show the animation
plt.show()
