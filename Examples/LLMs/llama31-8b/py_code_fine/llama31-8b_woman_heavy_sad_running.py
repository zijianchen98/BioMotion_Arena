
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_points = 15
num_frames = 100
fps = 30

# Define the point positions
points = np.random.rand(num_points, 2) * 2 - 1  # Random initial positions

# Define the action (running)
def run(action):
    if action == 'running':
        speed = 0.05
        angle = 0.5
    else:
        raise ValueError("Invalid action")

    for i in range(num_frames):
        for j in range(num_points):
            # Move the point along a circular path
            x = points[j, 0] + np.cos(i / fps + j / num_points * angle) * speed
            y = points[j, 1] + np.sin(i / fps + j / num_points * angle) * speed
            points[j, :] = [x, y]

# Create the figure and axis
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_axis_off()

# Create the point lights
lights = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.set_axis_off()
    lights.set_offsets(points)
    ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

# Run the animation
run('running')
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000 // fps)

# Display the animation
plt.show()
