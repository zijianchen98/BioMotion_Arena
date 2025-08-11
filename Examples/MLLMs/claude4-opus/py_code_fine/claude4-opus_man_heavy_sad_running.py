
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_lights = 15

# Initialize positions of point-lights
# Using a simple running cycle
points = np.zeros((num_lights, 2))

# Model a simple running cycle
def update_points(frame):
    step_size = 0.1  # How much to change per frame
    global points

    # Update y positions to simulate running
    for i in range(num_lights):
        if i % 3 == 0:  # legs
            points[i, 1] = np.sin(frame * step_size + i) * 0.5  # up-down motion
            points[i, 0] += 0.02  # forward motion
        else:  # arms or torso
            points[i, 1] += 0.02 * (-1)**(i // 3)  # simple coordinated arm motion

    # Ensure points are within screen bounds
    points[:, 0] = np.clip(points[:, 0], -5, 5)
    points[:, 1] = np.clip(points[:, 1], -3, 3)

# Create the figure
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')

# Create a scatter plot for points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Animation update function
def animate(frame):
    update_points(frame)
    scat.set_offsets(points)

# Create animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=50)

plt.axis('off')  # Turn off axis
plt.show()
