
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the coordinates of the point-lights
# These coordinates represent the turning around motion of a man
# Note: The coordinates are handcrafted for demonstration purposes
# In a real scenario, these would be obtained from motion capture data
coordinates = np.zeros((num_frames, 15, 2))
for i in range(num_frames):
    angle = 2 * np.pi * i / num_frames
    radius = 50
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    coordinates[i] = np.random.normal([x, y], [10, 10], size=(15, 2))

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a scatter plot for the point-lights
point_lights, = ax.plot([], [], 'o', color='white')

def update(frame):
    # Update the positions of the point-lights
    point_lights.set_data(coordinates[frame][:, 0], coordinates[frame][:, 1])
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True)

# Show the animation
plt.show()
