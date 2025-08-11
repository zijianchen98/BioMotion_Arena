
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point light parameters
point_lights = [
    (0, 0, 0),  # Initial position
    (1, 0, 0),
    (2, 0, 0),
    (3, 0, 0),
    (4, 0, 0),
    (5, 0, 0),
    (6, 0, 0),
    (7, 0, 0),
    (8, 0, 0),
    (9, 0, 0),
    (10, 0, 0),
    (11, 0, 0),
    (12, 0, 0),
    (13, 0, 0),
    (14, 0, 0),
    (15, 0, 0),
]

# Define the animation parameters
frame_rate = 30  # Frames per second
duration = 1  # Duration of the animation in seconds

# Create a figure and axes
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Create a black background
ax.set_facecolor('black')

# Create a list to store the animation frames
frames = []

# Create the animation
def animate(i):
    # Calculate the position of the point lights
    for j in range(len(point_lights)):
        x = point_lights[j][0]
        y = point_lights[j][1]
        z = point_lights[j][2]
        # Add some random noise to the position
        x += np.random.rand() * 0.1
        y += np.random.rand() * 0.1
        z += np.random.rand() * 0.1
        # Draw the point light
        ax.plot(x, y, z, 'w', marker='o', markersize=0.1)

    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration * frame_rate, interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()
