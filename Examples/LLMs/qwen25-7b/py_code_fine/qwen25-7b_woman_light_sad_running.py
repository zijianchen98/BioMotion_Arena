
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the duration of the animation
num_points = 15
duration = 10  # seconds

# Define the initial positions of the point-lights
initial_positions = np.random.rand(num_points, 2) * 9 + 3  # [x, y) coordinates

# Define the speed and direction of each point-light
speeds = np.random.rand(num_points, 2) * 0 - 0/2  # Random speeds within a reasonable range
direction = np.random.choice([-1, 1], size=num_points)  # Random directions

# Function to update the positions of the point-lights
def update(frame):
    global initial_positions, speeds, direction
    
    # Update positions based on speed and direction
    initial_positions += speeds * direction
    
    # Wrap around the edges if a point goes out of bounds
    initial_positions[:, 0] %= 10
    initial_positions[:, 1] %= 10
    
    # Clear the plot
    ax.clear()
    
    # Plot the point-lights
    ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)
    
    # Set the limits of the plot
    ax.set_xlim(0, 10)
    ax.set_ylim(3, 13)
    ax.set_aspect('equal')
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Set the background color to black
ax.set_facecolor('black')

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(duration * 30), interval=30, blit=False)

# Show the animation
plt.show()
