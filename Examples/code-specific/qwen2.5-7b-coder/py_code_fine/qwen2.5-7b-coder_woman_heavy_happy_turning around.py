
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
num_points = 15
frames = 100
radius = 1.5
weight_radius = 2.0
center_x, center_y = 0, 0
speed = 0.05

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Create the points
points = np.zeros((num_points, 2))
weights = np.random.rand(num_points) * 0.5 + 0.5

# Create the weight circle
weight_circle = plt.Circle((center_x, center_y), weight_radius, color='white', fill=True)

# Add the points and weight circle to the plot
for i in range(num_points):
    point, = ax.plot(points[i, 0], points[i, 1], 'o', markersize=10, color='white')
    points[i] = point.get_data()

ax.add_artist(weight_circle)

# Update function for the animation
def update(frame):
    # Clear the points
    for point in points:
        point.set_data(0, 0)
    
    # Calculate new positions
    angle = frame * speed
    for i in range(num_points):
        points[i][0] = center_x + radius * np.cos(angle + i * 2 * np.pi / num_points)
        points[i][1] = center_y + radius * np.sin(angle + i * 2 * np.pi / num_points)
        points[i] = point.get_data()
    
    # Update the weight circle
    weight_circle.center = (center_x + radius * np.cos(angle), center_y + radius * np.sin(angle))
    
    return points, weight_circle

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=False)

# Show the animation
plt.show()
