
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_points = 15
duration = 100  # Frames
frame_rate = 30  # Frames per second
radius = 0.05  # Radius of the points
speed = 0.1  # Rolling speed

# Define the rolling motion
def rolling_motion(t):
    """Generates coordinates for the point-lights based on a rolling motion."""
    x = radius * np.cos(2 * np.pi * t * speed)
    y = radius * np.sin(2 * np.pi * t * speed)
    z = radius * (1 - np.cos(2 * np.pi * t * speed))
    return x, y, z

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
points = []
for _ in range(num_points):
    points.append(plt.plot([], [], 'w')[0])

# Animation function
def animate(frame):
    """Updates the position of the point-lights for each frame."""
    t = frame / frame_rate
    x, y, z = rolling_motion(t)
    for i in range(num_points):
        points[i].set_data(x[i], y[i])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration * frame_rate, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("forward_roll.gif", writer='pillow', fps=frame_rate)

plt.show()
