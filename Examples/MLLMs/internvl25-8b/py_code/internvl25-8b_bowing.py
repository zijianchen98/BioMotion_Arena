
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants for the figure size and points
FIG_SIZE = 10
POINTS = 15

# Define the bowing movement by computing the points' coordinates
def get_points(frame):
    bowing_angles = np.linspace(0, 3.14159, POINTS)
    x = FIG_SIZE * np.cos(bowing_angles[frame])
    y = FIG_SIZE * np.sin(bowing_angles[frame])
    return list(zip(x, y))

# Create the initial figure with a black background
fig, ax = plt.subplots(figsize=(FIG_SIZE, FIG_SIZE))
ax.set_aspect('equal')
ax.set_xlim([-FIG_SIZE, FIG_SIZE])
ax.set_ylim([-FIG_SIZE, FIG_SIZE])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Bowing Point-Light Stimulus')
ax.axis('off')
points, = ax.plot([], [], 'o', color='white')

# Function to update the animation frame
def update(frame):
    points.set_data(get_points(frame))
    return points,

# Animation with 80 frames per second
ani = FuncAnimation(fig, update, frames=np.arange(0, POINTS), blit=True, interval=1000 // 80)

# Save and show the animation
ani.save('bowing_animation.gif', writer='imagemagick')

# Display the final frame
plt.show()
