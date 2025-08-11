
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
num_points = 15
num_frames = 60
frame_rate = 30

# Define the positions of the points
points = np.zeros((num_points, 2))
points[:, 0] = np.linspace(0.2, 0.8, num_points)
points[:, 1] = np.linspace(0.2, 0.8, num_points)

# Define the movement of the points
def move_points(points, frame):
    # Move the points in a way that represents a walking motion
    for i in range(num_points):
        if frame < 10:
            points[i, 1] = 0.2 + 0.2 * np.sin(2 * np.pi * frame / 10)
        elif frame < 20:
            points[i, 1] = 0.8 - 0.2 * np.sin(2 * np.pi * (frame - 10) / 10)
        elif frame < 30:
            points[i, 1] = 0.8 - 0.2 * np.sin(2 * np.pi * (frame - 20) / 10)
        else:
            points[i, 1] = 0.2 + 0.2 * np.sin(2 * np.pi * (frame - 30) / 10)
    return points

# Create the figure and axis
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_axis_off()

# Initialize the points
points = move_points(points, 0)

# Plot the points
scatter = ax.scatter(points[:, 0], points[:, 1], s=100, c='w', zorder=10)

# Animate the points
def animate(frame):
    points = move_points(points, frame)
    scatter.set_offsets(points)
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/frame_rate, blit=True)

plt.show()
