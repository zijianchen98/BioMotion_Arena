
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
n_points = 15
fps = 30
duration = 3 # seconds
frames = fps * duration

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create the points
points = [plt.Circle((np.random.rand(), np.random.rand()), 0.1, color='white') for _ in range(n_points)]
for point in points:
    ax.add_patch(point)

# Define the walking pattern
def walk(t):
    return 0.5*np.sin(2*np.pi*t/4) + 5, 0.5*np.cos(2*np.pi*t/4) + 5

# Update function for the animation
def update(frame):
    t = frame / fps
    for i, point in enumerate(points):
        x, y = walk(t + i*0.1)
        point.center = (x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()
