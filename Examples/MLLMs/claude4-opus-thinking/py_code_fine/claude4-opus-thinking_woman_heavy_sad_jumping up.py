
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

# Initialize point lights (15 points)
num_points = 15
points = np.zeros((num_points, 2))

# Function to initialize the points (initial positions)
def init():
    # Initial positions of lights in a vertical arrangement
    for i in range(num_points):
        if i < 5:
            points[i] = [5 + 0.5 * i, 1]  # Upper body
        elif i < 10:
            points[i] = [5 + 0.5 * (i - 5), 5]  # Lower body
        else:
            points[i] = [5 + 0.5 * (i - 10), 3]  # Feet
    scat.set_offsets(points)
    return scat,

# Create a scatter plot for point lights
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for the animation
def update(frame):
    # Update Y positions to simulate jumping
    for i in range(num_points):
        y_offset = np.sin((frame + i) * 0.3) * 2  # Jumping effect
        points[i][1] = points[i][1] + y_offset if points[i][1] < 7 else 5  # Reset after maximum height
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init,
                              blit=True, interval=50)

# Show the animation
plt.show()
