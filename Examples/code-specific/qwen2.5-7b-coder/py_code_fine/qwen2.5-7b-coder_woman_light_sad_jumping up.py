
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_points = 15
frame_rate = 30
duration = 2  # seconds
total_frames = int(frame_rate * duration)
background_color = 'black'
point_color = 'white'

# Define the initial positions and velocities of the points
initial_positions = np.random.rand(num_points, 2)
velocities = np.zeros((num_points, 2))
velocities[:, 1] = -np.linspace(0.5, -0.5, num_points)

# Define the figure and axis for the animation
fig, ax = plt.subplots(figsize=(8, 6), facecolor=background_color)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Create the scatter plot for the points
points, = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color=point_color, s=100)

# Update function for the animation
def update(frame):
    global initial_positions, velocities
    
    # Update the positions of the points based on their velocities
    initial_positions += velocities
    
    # Wrap around the points when they reach the edges of the frame
    initial_positions[initial_positions[:, 0] > 1, 0] -= 1
    initial_positions[initial_positions[:, 0] < 0, 0] += 1
    initial_positions[initial_positions[:, 1] > 1, 1] -= 1
    initial_positions[initial_positions[:, 1] < 0, 1] += 1
    
    # Update the scatter plot with the new positions
    points.set_offsets(initial_positions)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/frame_rate, blit=True)

# Show the animation
plt.show()
