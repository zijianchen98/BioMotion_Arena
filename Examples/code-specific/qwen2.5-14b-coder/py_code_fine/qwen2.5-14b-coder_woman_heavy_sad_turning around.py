
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.random.rand(num_lights, 2)

# Define the target positions for the point-lights to simulate turning around
target_positions = np.zeros((num_lights, 2))
for i in range(num_lights):
    angle = np.radians(i * (360 / num_lights))
    target_positions[i] = [np.cos(angle), np.sin(angle)]

# Define the animation function
def animate(frame):
    # Calculate the current positions of the point-lights
    current_positions = (1 - frame / 100) * initial_positions + (frame / 100) * target_positions
    
    # Update the scatter plot
    scatter.set_offsets(current_positions)
    
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create the animation
animation = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
