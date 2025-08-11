
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the subject and action parameters
subject = 'sadwoman'
action = 'jumping forward'

# Define the number of points and their initial positions
num_points = 15
initial_positions = np.array([(np.random.rand() * 10 - 5, np.random.rand() * 10 - 5)
                               for _ in range(num_points)], dtype=np.float32)

# Define the background color
background_color = (0, 0, 0

# Define the frame size
frame_size = 10

# Define the time step and duration
time_step = 0.05
duration = 5

# Define the animation function
def animate(frame):
    global initial_positions
    # Calculate new positions based on the action
    # For simplicity, we'll just move the points slightly towards the center
    initial_positions += (time_step, 0
    # Ensure positions stay within the frame boundaries
    initial_positions = np.clip(initial_positions, 0, frame_size)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(frame_size, frame_size))
ax.set_xlim(0, frame_size)
ax.set_ylim(0, frame_size)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create the animation
animation = FuncAnimation(fig, animate, frames=np.arange(0, duration / time_step, interval=time_step * 1000)

# Show the animation
plt.show()

