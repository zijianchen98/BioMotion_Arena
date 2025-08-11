
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create a list to hold the point lights
points = []

# Initialize the point lights
for _ in range(15):
    x, y = np.random.rand(2) * 10
    point, = ax.plot(x, y, 'wo', markersize=10)
    points.append(point)

# Animation function
def update(frame):
    # Update the position of each point light
    for i, point in enumerate(points):
        # Simulate a simple jumping motion
        new_y = 5 + np.sin(frame / 50 + i / 10) * 3
        point.set_ydata(new_y)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 2*np.pi, 0.1), interval=50)

# Show the animation
plt.show()
