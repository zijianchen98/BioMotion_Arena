
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_frames = 60
frame_rate = 30
num_lights = 15
weight_factor = 0.8
angle_range = np.pi / 4

# Initialize the positions of the lights
positions = np.random.rand(num_lights, 2) * 2 - 1
velocities = np.zeros((num_lights, 2))

# Define the function to update the positions of the lights
def update(frame):
    global positions, velocities
    
    # Calculate the acceleration due to gravity and weight
    acceleration = np.array([0, -9.8]) * weight_factor
    
    # Update the velocities
    velocities += acceleration / frame_rate
    
    # Update the positions
    positions += velocities / frame_rate
    
    # Wrap around the positions
    positions %= 2
    
    # Clear the previous plot
    ax.clear()
    
    # Set the limits of the plot
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    
    # Plot the lights
    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=10)
    
    return positions,

# Create the figure and axis for the plot
fig, ax = plt.subplots()

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate, blit=True)

# Show the plot
plt.show()
