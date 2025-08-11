
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Initial positions (x, y) for the 15 point-lights
positions = np.array([
    (0.5, 0.9), (0.4, 0.8), (0.6, 0.8), 
    (0.3, 0.7), (0.7, 0.7), (0.4, 0.6), (0.6, 0.6), 
    (0.3, 0.5), (0.7, 0.5), (0.2, 0.4), (0.8, 0.4), 
    (0.5, 0.3), (0.4, 0.2), (0.6, 0.2), (0.5, 0.1)
])

# Function to update the positions for the running motion
def update_positions(i):
    global positions
    theta = np.pi / 4 * np.sin(i / 40 * np.pi)
    positions[:, 1] = positions[:, 1] + (0.02 * np.sin(i / 20))
    positions[:, 0] += 0.01 * np.cos(theta + positions[:, 1] * np.pi)
    return positions

# Function to animate the points
def animate(i):
    global positions
    positions = update_positions(i)
    scat.set_offsets(positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Turn off axis

# Initialize scatter plot
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=30, blit=True)

# Display the animation
plt.show()
