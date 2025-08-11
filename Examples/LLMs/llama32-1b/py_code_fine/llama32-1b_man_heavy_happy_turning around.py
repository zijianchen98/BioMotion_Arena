
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
width, height = 800, 600
fps = 30

# Define the parameters for the point lights
light_positions = [
    (100, 100),  # subject
    (300, 300),  # action
    (500, 500)   # object
]

# Define the parameters for the object
object_radius = 20

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the point lights
point_lights = []
for i, pos in enumerate(light_positions):
    light = plt.Circle(pos, 1, color='white', alpha=0.5)
    ax.add_artist(light)
    point_lights.append(light)

# Initialize the axis
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')

# Function to update the plot
def update(frame):
    for light in point_lights:
        light.set_center((light_positions[0][0] + light_positions[1][0] + light_positions[2][0]) / 3,
                         light_positions[0][1] + light_positions[1][1] + light_positions[2][1] / 3)
    
    # Update the axis
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    
    # Update the point lights
    for i, light in enumerate(point_lights):
        light.set_center((light_positions[i][0] + light_positions[i+1][0] + light_positions[i+2][0]) / 3,
                         light_positions[i][1] + light_positions[i+1][1] + light_positions[i+2][1] / 3)

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=16/fps)

plt.show()
