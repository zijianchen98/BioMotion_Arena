
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These positions are placeholders and should be adjusted to match the desired animation
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for each point light
# These positions should be calculated to simulate the waving hand motion
target_positions = np.array([
    [0.5, 0.5],  # Example position for the hand
    [0.4, 0.6],  # Example position for the forearm
    [0.3, 0.7],  # Example position for the upper arm
    [0.2, 0.8],  # Example position for the shoulder
    [0.1, 0.9],  # Example position for the torso
    [0.2, 0.8],  # Example position for the other shoulder
    [0.3, 0.7],  # Example position for the other upper arm
    [0.4, 0.6],  # Example position for the other forearm
    [0.5, 0.5],  # Example position for the other hand
    [0.6, 0.4],  # Example position for the other forearm
    [0.7, 0.3],  # Example position for the other upper arm
    [0.8, 0.2],  # Example position for the other shoulder
    [0.9, 0.1],  # Example position for the torso
    [0.8, 0.2],  # Example position for the shoulder
    [0.7, 0.3]   # Example position for the upper arm
])

# Define the duration of the animation in frames
duration = 100

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'o', color='white')

# Define the update function for the animation
def update(frame):
    # Calculate the current positions of the point lights
    t = frame / duration
    current_positions = (1 - t) * initial_positions + t * target_positions
    
    # Update the positions of the point lights
    points.set_data(current_positions[:, 0], current_positions[:, 1])
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=duration, blit=True)

# Show the animation
plt.show()
