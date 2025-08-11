
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the running figure
n_points = 15
time_steps = 200
figure_speed = 0.1

# Random starting positions for the points
positions = np.random.rand(n_points, 2) * 10

# Animation update function
def update(frame):
    ax.clear()
    ax.imshow(np.zeros((10, 10, 3)), cmap='gray')  # Black background
    # Update positions: a simple linear movement (can be replaced with a more complex motion for realism)
    global positions
    positions[:, 0] += figure_speed
    if positions[:, 0].max() > 10:
        positions[:, 0] -= 20
    ax.scatter(positions[:, 0], positions[:, 1], s=50, color='white')
    # Set limits
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# Set up the plot
fig, ax = plt.subplots()
# Create the animation
ani = FuncAnimation(fig, update, frames=time_steps, interval=50, blit=False)
plt.show()
