
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the subject's initial position and velocity
num_points = 15
initial_positions = np.random.rand(num_points, 2) * 8 - 4  # Random positions within [-4, 4]
velocities = np.random.randn(num_points, 2) / 10  # Small random velocities

# Function to update the positions of the points
def update(frame):
    global initial_positions, velocities
    
    # Update positions based on velocities
    initial_positions += velocities
    
    # Wrap around the edges to create a continuous motion effect
    initial_positions[initial_positions > 4] -= 8
    initial_positions[initial_positions < -4] += 8
    
    # Clear the previous frame
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Plot the updated positions of the points in white
    ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)
    
    # Set the limits of the plot
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, repeat=True)

# Show the animation
plt.show()
