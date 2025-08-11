
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up parameters
num_points = 15
frames = 100
duration = 5  # duration in seconds
fps = frames / duration

# Create a function to generate the point-light positions
def point_light_positions(frame):
    positions = []

    # Assuming a simple running motion with some offsets
    # The vertical position represents height
    height = np.sin(frame * 2 * np.pi / frames) * 0.1  # Simulated vertical swing
    horizontal_offset = (frame / frames) * 2 - 1  # Horizontal movement

    # Define the basic structure of point-lights (Y axis for running)
    for i in range(num_points):
        x = horizontal_offset
        y = (i - num_points / 2) * 0.1 + height  # Spread points vertically
        positions.append((x, y))

    return positions

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Turn off the axis

# Create point-lights
point_lights, = ax.plot([], [], 'o', color='white', markersize=10)

# Animation update function
def update(frame):
    positions = point_light_positions(frame)
    x_data, y_data = zip(*positions)  # Unzip positions
    point_lights.set_data(x_data, y_data)
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()
