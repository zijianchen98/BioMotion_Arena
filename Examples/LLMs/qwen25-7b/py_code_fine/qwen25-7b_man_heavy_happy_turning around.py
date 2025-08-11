
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the total duration of the animation
num_points = 15
duration = 4  # seconds

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
axax.set_facecolor('black')

# Define the initial positions of the points
initial_positions = np.random.uniform(0extent=[-.5, 1.5], size=(num_points, 2))

# Define the turning radius and speed
radius = 0.5
speed = 0.1

# Define the center of rotation
center_x, center_y = 0, 1

# Define the angle change per frame
angle_change_per_frame = 0.1

# Initialize the positions of the points
positions = initial_positions.copy()

def update(frame):
    global positions, angle_change_per_frame
    
    # Calculate the angle for each point
    angles = np.linspace(0, 2 * np.pi + angle_change_per_frame * frame, num_points)
    
    # Update the positions based on the new angles
    positions[:, 0] = center_x + radius * np.cos(angles)
    positions[:, 1] = center_y + radius * np.sin(angles)
    
    # Plot the points
    ax.clear()
    ax.set_facecolor('black')
    ax.scatter(positions[:, 0], positions[:, 1], s=100, color='w')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0 * duration), interval=10, blit=False)

# Show the animation
plt.show()
