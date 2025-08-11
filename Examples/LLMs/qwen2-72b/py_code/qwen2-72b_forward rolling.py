
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
np.random.seed(0)
initial_positions = np.random.uniform(-50, 50, size=(15, 2))

# Define the velocities of the 15 point-lights
velocities = np.random.uniform(-1, 1, size=(15, 2))

# Function to update the positions of the point-lights for each frame
def update_position(positions):
    # Update positions based on velocities
    positions += velocities
    # Ensure the point-lights stay within the bounds of the plot area
    positions = np.clip(positions, -50, 50)
    return positions

# Function to animate the point-lights
def animate(i):
    global initial_positions
    # Update the positions of the point-lights
    initial_positions = update_position(initial_positions)
    # Clear the current plot
    ax.clear()
    # Plot the updated positions of the point-lights
    ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')
    # Set the plot limits
    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])

# Create a new figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')

# Animate the point-lights
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
