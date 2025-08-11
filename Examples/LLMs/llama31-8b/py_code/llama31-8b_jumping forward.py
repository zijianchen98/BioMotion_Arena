
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points
initial_positions = np.random.rand(num_points, 2) * 2 - 1  # Random positions within a 2x2 square

# Define the target positions of the points
target_positions = np.random.rand(num_points, 2) * 2 - 1  # Random target positions within a 2x2 square

# Define the time parameters
duration = 2  # Duration of the animation in seconds
fps = 60  # Frames per second

# Define the time array
time = np.linspace(0, duration, int(fps * duration))

# Define the animation function
def animate(i):
    # Calculate the current time
    t = time[i]
    
    # Calculate the current positions of the points using sinusoidal motion
    current_positions = (initial_positions + 0.5 * (target_positions - initial_positions) * np.sin(2 * np.pi * t / duration)) * 2 - 1
    
    # Clear the current axes
    ax.clear()
    
    # Set the axis limits
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    # Set the axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Plot the points
    ax.scatter(current_positions[:, 0], current_positions[:, 1], s=100, c='white', zorder=10)

# Create a new figure
fig, ax = plt.subplots()

# Set the background color
ax.set_facecolor('black')

# Animate the points
ani = animation.FuncAnimation(fig, animate, frames=len(time), interval=1000 // fps, blit=False)

# Show the animation
plt.show()
