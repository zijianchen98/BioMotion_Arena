
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Background color
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 3)

# Initial position of the point-lights
# 15 points representing a sad woman with weight, sitting down
points_x = np.array([0, -0.5, 0, 0.5, 0, -0.4, 0.4, 0, 0.3, -0.3, 0, 0, 0, 0, 0])
points_y = np.array([2, 2.5, 2, 2.5, 2.2, 1.5, 1.5, 1.7, 0.5, 0.5, 1.7, 1.4, 1, 0.8, 0.6])

point_lights = ax.scatter(points_x, points_y, color='white', s=100)

def update(frame):
    # Smooth motion for the points to simulate sitting down
    global points_y
    points_y -= 0.02  # Move all points downward slightly
    points_x += np.random.normal(0, 0.01, size=points_x.shape)  # Random x jitter for realism

    # Update the point-light positions
    point_lights.set_offsets(np.c_[points_x, points_y])
    
    # Stop the animation when the points have descended sufficiently
    if points_y[0] < 0:
        ani.event_source.stop()

    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=50, blit=True)

plt.axis('off')  # Turn off the axis
plt.show()
