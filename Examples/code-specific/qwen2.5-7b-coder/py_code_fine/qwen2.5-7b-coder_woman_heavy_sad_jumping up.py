
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
num_points = 15
time_steps = 100
frame_rate = 30

# Initialize the positions of the points
positions = np.random.rand(num_points, 2)
velocities = np.zeros((num_points, 2))
accelerations = np.zeros((num_points, 2))

# Set initial conditions for one point to simulate a sad woman with a heavy weight jumping
initial_index = num_points // 2
positions[initial_index] = [0.5, 0.2]
velocities[initial_index] = [0, -0.5]
accelerations[initial_index] = [0, 0.1]

# Function to update the positions of the points
def update(frame):
    global positions, velocities, accelerations
    
    # Update the positions based on velocities and accelerations
    positions += velocities * frame_rate / 1000 + 0.5 * accelerations * (frame_rate / 1000) ** 2
    
    # Apply gravity to all points
    accelerations[:, 1] = -9.81
    
    # Ensure points stay within bounds
    positions[:, 0] = np.clip(positions[:, 0], 0, 1)
    positions[:, 1] = np.clip(positions[:, 1], 0, 1)
    
    # Clear the previous plot
    ax.clear()
    
    # Plot the updated positions
    ax.scatter(positions[:, 0], positions[:, 1], color='white')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = FuncAnimation(fig, update, frames=time_steps, interval=1000 / frame_rate)

# Show the animation
plt.show()
