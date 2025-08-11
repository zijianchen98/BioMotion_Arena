
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 1)
ax.axis('off')
fig.patch.set_facecolor('black')

# Number of point-lights
num_points = 15

# Initialize positions of the points
points_x = np.array([0, -0.2, 0.2, -0.3, 0.3, -0.4, 0.4, -0.5, 0.5, -0.6, 0.6, -0.6, 0.6, -0.4, 0.4])
points_y = np.array([0.9, 0.6, 0.6, 0.4, 0.4, 0.2, 0.2, 0.0, 0.0, -0.2, -0.2, -0.6, -0.6, -1.0, -1.0])

scatter = ax.scatter(points_x, points_y, c="white", s=50)

# Biomechanically plausible bowing motion
def update(frame):
    bow_speed = 0.02
    bow_angle = np.sin(frame * np.pi / 50) * bow_speed
    
    # Update y-coordinates to simulate bowing motion
    new_points_y = points_y + bow_angle
    
    # Head and torso tilt forward slightly
    new_points_x = points_x + bow_angle * (points_y - 0)
    scatter.set_offsets(np.c_[new_points_x, new_points_y])
    return scatter,

# Animate the figure
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show animation
plt.show()
