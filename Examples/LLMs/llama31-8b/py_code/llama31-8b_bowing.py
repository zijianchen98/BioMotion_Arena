
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
n_points = 15

# Define the initial positions of the points
initial_positions = np.random.rand(n_points, 2)

# Define the target positions of the points
target_positions = np.zeros((n_points, 2))

# Define the action: bowing
# The points will move in a smooth, curved motion
# We'll use a sine function to create the motion
def bowing_action(t, initial_positions):
    # Define the amplitude and frequency of the motion
    amplitude = 0.1
    frequency = 0.1
    
    # Calculate the target positions
    target_positions[:, 0] = initial_positions[:, 0] + amplitude * np.sin(2 * np.pi * frequency * t)
    target_positions[:, 1] = initial_positions[:, 1] + amplitude * np.sin(2 * np.pi * frequency * t + np.pi/2)
    
    return target_positions

# Create a new figure
fig, ax = plt.subplots()

# Create a scatter plot of the points
sc = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='w', s=10)

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Set the axis off
ax.axis('off')

# Define the animation function
def animate(i):
    global sc
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')
    ax.axis('off')
    target_positions = bowing_action(i/50, initial_positions)
    sc = ax.scatter(target_positions[:, 0], target_positions[:, 1], c='w', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=20)

# Show the animation
plt.show()
