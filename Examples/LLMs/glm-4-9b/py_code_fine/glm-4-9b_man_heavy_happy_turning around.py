
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point-lights
num_point_lights = 15

# Define the radius of the circle around which the point-lights will move
radius = 100

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, color='white')

# Function to update the positions of the point-lights
def update(frame):
    angles = np.linspace(0, 2 * np.pi, num_point_lights, endpoint=False) + frame * 0.05
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    scatter.set_offsets(np.column_stack((x, y)))
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
