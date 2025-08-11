
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up parameters
num_points = 15
duration = 2  # seconds
fps = 30  # frames per second
num_frames = duration * fps
jump_height = 2  # Maximum height of the jump
gravity = -9.81  # Acceleration due to gravity
initial_velocity = 10  # Initial velocity of the jump

# Function to calculate the y position for the jump
def jumping_motion(frame):
    # Calculate time in seconds
    time = frame / fps
    # Calculate vertical position using physics equations
    # Using the equation: h(t) = initial_velocity * t + 0.5 * gravity * t^2
    height = initial_velocity * time + 0.5 * gravity * time**2
    if height < 0:  # stop going below ground level
        height = 0
    return height

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 3)
ax.set_facecolor('black')

# Create point-lights (initial positions)
points = np.zeros((num_points, 2))
# Distributing points vertically for the body structure
points[:, 0] = np.linspace(-0.2, 0.2, num=num_points)  # x-coordinates

# Animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 3)
    ax.set_facecolor('black')

    # Compute height for all points
    height = jumping_motion(frame)
    
    # Update y-coordinates for the points (simulating a body jumping up)
    for i in range(num_points):
        points[i, 1] = height - (i * 0.1)  # y-coordinates

    # Plot points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=100)  # point-lights

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/fps)

# Display the animation
plt.show()
