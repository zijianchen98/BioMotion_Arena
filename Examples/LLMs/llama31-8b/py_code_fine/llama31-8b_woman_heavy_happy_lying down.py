
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
initial_positions = np.random.rand(num_lights, 2) * 100  # Random initial positions within a 100x100 square

# Define the movement of the point lights
def move_points(points, t):
    # Define the movement parameters
    duration = 10  # Total duration of the animation in seconds
    period = 1  # Period of the movement in seconds
    frequency = 1 / period  # Frequency of the movement
    amplitude = 10  # Amplitude of the movement
    phase_shift = 0  # Phase shift for the movement

    # Calculate the movement of each point
    movement = np.sin(2 * np.pi * frequency * t + phase_shift) * amplitude

    # Update the positions of the points
    new_positions = points + movement

    # Ensure the points stay within the boundaries
    new_positions = np.clip(new_positions, 0, 100)

    return new_positions

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the initial positions of the point lights
ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, c='w', alpha=1)

# Set the limits of the plot
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the limits of the plot
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_facecolor('black')

    # Move the point lights
    new_positions = move_points(initial_positions, i / 30)  # 30 frames per second

    # Plot the point lights at their new positions
    ax.scatter(new_positions[:, 0], new_positions[:, 1], s=100, c='w', alpha=1)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=300, interval=1000 // 30, repeat=True)

# Show the animation
plt.show()
