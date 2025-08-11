
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points = []

# Create 15 point-lights in initial positions
num_points = 15
points_data = np.array([
    (0, 1),   # head
    (-0.5, 0.7), (0.5, 0.7), # shoulders
    (-0.7, 0.4), (0.7, 0.4), # arms
    (-0.5, 0), (0.5, 0),     # body
    (-0.3, -0.6), (0.3, -0.6), # hips
    (-0.2, -1), (0.2, -1),   # knees
    (-0.1, -1.5), (0.1, -1.5), # feet
    (-0.5, 0.3), (0.5, 0.3),  # weights
    (0, -1)    # base
])

# Placing the points on the plot
for i in range(num_points):
    point, = ax.plot([], [], 'o', color='white', markersize=10)
    points.append(point)

# Update function for animation
def update(frame):
    # Clear previous points
    for point in points:
        point.set_data([], [])
        
    # Positions for each subsequent frame
    for i, (x, y) in enumerate(points_data):
        # Sway effect with a bowing motion
        bow_factor = np.sin(frame / 10) * 0.1
        point_x = x + bow_factor
        point_y = y - (frame % 100)/100  # simulate downward movement
        points[i].set_data(point_x, point_y)

    return points

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(300), interval=50, blit=True)

# Show animation
plt.show()
