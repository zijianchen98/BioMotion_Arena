
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 60

# Define the initial positions of the point lights
np.random.seed(42)
initial_positions = np.random.rand(15, 2)

# Define the target positions for the sad woman lying down
target_positions = np.array([
    [0.2, 0.8], [0.3, 0.7], [0.4, 0.6], [0.5, 0.5], [0.6, 0.4],
    [0.7, 0.3], [0.8, 0.2], [0.9, 0.1], [0.1, 0.9], [0.2, 0.8],
    [0.3, 0.7], [0.4, 0.6], [0.5, 0.5], [0.6, 0.4], [0.7, 0.3]
])

# Define the velocity of each point light
velocities = np.zeros((15, 2))

# Define the acceleration due to gravity
gravity = np.array([0, -0.01])

# Define the function to update the positions of the point lights
def update(frame):
    global velocities
    
    # Apply gravity to each point light
    velocities += gravity
    
    # Update the positions of the point lights
    initial_positions += velocities
    
    # Wrap around the edges of the plot
    initial_positions %= 1
    
    # Clear the previous frame
    ax.clear()
    
    # Set the background color to black
    ax.set_facecolor('black')
    
    # Plot the point lights as white dots
    ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)
    
    # Draw the target positions as red crosses
    ax.plot(target_positions[:, 0], target_positions[:, 1], 'rx')

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')

# Create the animation using the update function
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

# Show the animation
plt.show()
