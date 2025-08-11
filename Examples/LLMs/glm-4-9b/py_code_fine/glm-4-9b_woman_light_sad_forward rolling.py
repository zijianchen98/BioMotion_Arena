
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 200  # frames
fps = 30

# Initialize the positions of the points
# Randomly distribute the points around a figure resembling a person
np.random.seed(0)
theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
r = 1.0 + 0.1 * np.random.rand(num_points)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Time-varying positions to simulate forward rolling motion
def update(frame):
    global x, y
    t = frame / fps
    # Simulate forward rolling motion by rotating the points
    angle = t * 2  # angular speed
    x Rotated = x * np.cos(angle) - y * np.sin(angle)
    y_rotated = x * np.sin(angle) + y * np.cos(angle)
    # Translate the points forward
    x_rotated += t * 0.1
    scatter.set_offsets(np.setColumn(np.c_[x_rotated, y_rotated], 0, x[:, 1], y_rotated[:, 1])
plt.axis('equal')
plt.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Create the scatter plot
scatter = plt.scatter(x, y, c='white', s=50, edgecolors='none')

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=duration, interval=1000/fps, blit=True)

# Save the animation as a video file
ani.save('point_light_stimulus.mp4', writer='ffmpeg', fps=fps)

# Display the animation
plt.show()
