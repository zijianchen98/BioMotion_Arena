
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames and points
num_frames = 60
num_points = 15

# Define the initial positions of the points
initial_positions = np.random.rand(num_points, 2)

# Define the walking motion parameters
speed = 0.05
angle_step = 0.1

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
points, = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

def update(frame):
    # Update the positions of the points
    global initial_positions
    
    # Calculate the new positions based on walking motion
    for i in range(num_points):
        angle = frame * angle_step + i * (2 * np.pi / num_points)
        distance = speed * frame
        initial_positions[i] += [np.cos(angle), np.sin(angle)] * distance
    
    # Wrap around the positions if they go out of bounds
    initial_positions %= 1
    
    # Update the scatter plot
    points.set_offsets(initial_positions)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
