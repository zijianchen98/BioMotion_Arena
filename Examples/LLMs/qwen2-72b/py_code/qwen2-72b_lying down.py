
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 100
num_points = 15

# Define the initial positions of the points randomly
positions = np.random.rand(num_points, 2)

# Define the velocities of the points
velocities = np.random.randn(num_points, 2) * 0.1

# Function to update the position of the points
def update_position(positions):
    global velocities
    # Update the position of each point based on its velocity
    positions += velocities
    # Keep the points within the bounds of the plot
    positions %= 1
    # Introduce some randomness in velocities to make the motion more natural
    velocities += np.random.randn(num_points, 2) * 0.01
    return positions

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_facecolor('black')

# Create a scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Animation function
def animate(i):
    global positions
    positions = update_position(positions)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
