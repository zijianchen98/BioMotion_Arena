
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuration
n_points = 15  # Number of point-lights
duration = 2000  # Duration in milliseconds

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Walking motion function
def walking_motion(frame):
    # Here we define the y-coordinates for the walk cycle
    # The walking pattern is designed as an example for the animation
    y_positions = np.sin(2 * np.pi * (frame + np.arange(n_points) / n_points) / 50) * 0.5 - 0.5
    x_positions = np.zeros(n_points)
    
    # Assume point-lights move to form a humanoid representation
    if frame % 40 < 20:
        x_positions[0:5] = 0.1  # right leg
        x_positions[5:10] = -0.1  # left leg
    else:
        x_positions[0:5] = -0.1  # left leg
        x_positions[5:10] = 0.1  # right leg

    # Update the points
    points.set_data(x_positions, y_positions)
    return points,

# Create the animation
ani = FuncAnimation(fig, walking_motion, frames=np.arange(0, 200), interval=50)

# Show the animation
plt.show()
