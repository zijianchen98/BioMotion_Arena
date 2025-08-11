
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_lights = 15
frame_rate = 30
duration = 5  # seconds
time_steps = int(frame_rate * duration)

# Initialize the positions of the lights
np.random.seed(42)
light_positions = np.random.rand(num_lights, 2) * 2 - 1  # Random positions in [-1, 1]

# Define the function to update the animation frame
def update(frame):
    global light_positions
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Update the positions of the lights based on the sadman waving his hand
    light_positions[:, 0] += 0.02 * np.sin(frame / 10)
    light_positions[:, 1] -= 0.02 * np.cos(frame / 10)
    
    # Ensure the lights stay within bounds
    light_positions[light_positions > 1] = 1
    light_positions[light_positions < -1] = -1
    
    # Plot the updated positions of the lights
    ax.scatter(light_positions[:, 0], light_positions[:, 1], color='white')

# Create the figure and axis for the animation
fig, ax = plt.subplots()

# Create the animation object
ani = FuncAnimation(fig, update, frames=time_steps, interval=1000 / frame_rate)

# Show the animation
plt.show()
