
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
dt = 0.02  # Time step
duration = 10  # Animation duration (seconds)
fps = 30  # Frames per second

# Define the joint angles for the jumping action
# These angles will drive the point movement
t = np.arange(0, duration, dt)
angles = np.zeros(len(t))

# Simulate the jumping motion
for i in range(len(t)):
    if t[i] < duration * 0.5:
        angles[i] = 0.5 * (1 + np.sin(np.pi * (t[i] / (duration * 0.5))))  # Upward movement
    else:
        angles[i] = -0.5 * (1 + np.sin(np.pi * ((t[i] - duration * 0.5) / (duration - duration * 0.5)))) # Downward movement


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Create the points
points = []
for _ in range(num_points):
    points.append(plt.scatter([], [], s=50, color='white'))

# Animation function
def animate(i):
    # Update the positions of the points based on the angles
    for j in range(num_points):
        x = 100 * np.cos(angles[i]) + 50 * np.cos(2 * np.pi * angles[i])
        y = 100 * np.sin(angles[i]) + 50 * np.sin(2 * np.pi * angles[i])
        points[j].set_offsets([x, y])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

# Save the animation (optional)
# ani.save("jumping_motion.gif", writer='pillow', fps=fps)

plt.show()
