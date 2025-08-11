
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the animation parameters
frame_rate = 30  # Frames per second
duration = 1  # Duration of the animation in seconds

# Define the movement parameters
speed = 0.1  # Speed of the movement
angle_increment = 0.05  # Angle increment for each frame

# Create a figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create the point lights
points = np.zeros((num_points, 2))
for i in range(num_points):
    points[i, 0] = np.random.uniform(-1, 1)
    points[i, 1] = np.random.uniform(-1, 1)

# Define the function to update the animation
def animate(i):
    global points
    # Calculate the angle for each point
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    
    # Update the position of each point
    for i in range(num_points):
        points[i, 0] = points[i, 0] + speed * np.cos(angles[i] + angle_increment * i)
        points[i, 1] = points[i, 1] + speed * np.sin(angles[i] + angle_increment * i)

    # Update the plot
    ax.clear()
    ax.scatter(points[:, 0], points[:, 1], s=10, c='white')
    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(duration * frame_rate), interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()
