
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Function to generate 15 point-lights at random positions
def generate_point_lights():
    x = np.random.uniform(-1, 1, 15)
    y = np.random.uniform(-1, 1, 15)
    return x, y

# Function to update the positions of the point-lights at each frame
def update(frame):
    if frame == 0:
        # Reset the positions after a full cycle
        x, y = generate_point_lights()
    else:
        x, y = points.get_offsets().T
        # Update the positions based on the wave animation
        y = np.sin(x * (frame + 1) / 10)


# Create a figure and plot
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set the background color to black
ax.set_xlim(-1, 1)  # Set x axis limits
ax.set_ylim(-1, 1)  # Set y axis limits
ax.set_aspect('equal')  # Set the aspect ratio to equal
ax.axis('off')  # Hide axis

x, y = generate_point_lights()
points, = ax.plot(x, y, 'w.')  # Plot the point-lights in white

# Create the animation with FuncAnimation
ani = FuncAnimation(fig, update, interval=10)

plt.show()

