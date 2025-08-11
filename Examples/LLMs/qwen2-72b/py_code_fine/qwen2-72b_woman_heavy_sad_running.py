
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create a list to hold the point-lights
point_lights = []

# Function to initialize the animation
def init():
    global point_lights
    for _ in range(15):
        # Create a scatter plot for each point-light
        point_light = ax.scatter([], [], color='white')
        point_lights.append(point_light)

# Function to update the animation frame
def animate(i):
    # Update the positions of the point-lights
    for j, light in enumerate(point_lights):
        x = i + j * 0.2  # Simple linear motion for demonstration
        y = np.sin(x) * 3 + 5  # Some vertical oscillation to mimic running
        light.set_offsets([(x % 10, y)])  # Wrap around the screen horizontally

# Call the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=False, interval=40)

plt.show()
