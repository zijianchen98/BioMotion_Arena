
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure size
fig_size = (8, 8)

# Define the parameters
n_points = 100
n_points_per_frame = 100
n_frames = 100
dt = 0.02
t_max = 10

# Create a new figure
fig, ax = plt.subplots(figsize=fig_size)

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Define the point light positions
point_lights = np.zeros((n_points, 3))
for i in range(n_points):
    angle = np.random.uniform(0, 2 * np.pi)
    x = np.sin(angle) * 0.5 + 0.5
    y = np.cos(angle) * 0.5 + 0.5
    z = np.random.uniform(-2, 2)
    point_lights[i] = np.array([x, y, z])

# Define the camera position
camera_position = np.array([0, 0, 2])

# Define the point light movement
def move_point_lights():
    global point_lights
    for i in range(n_points):
        angle = np.random.uniform(0, 2 * np.pi)
        x = np.sin(angle) * 0.5 + 0.5
        y = np.cos(angle) * 0.5 + 0.5
        z = np.random.uniform(-2, 2)
        point_lights[i] = np.array([x, y, z]) + camera_position

    # Move the point lights against the black background
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_axis_off()
    for i in range(n_points):
        x = point_lights[i, 0]
        y = point_lights[i, 1]
        z = point_lights[i, 2]
        ax.plot([x, x + 1], [y, y + 1], 'k-')
        ax.plot([x + 0.5, x + 0.5 + 1], [y + 0.5, y + 0.5 + 1], 'k-')

ani = animation.FuncAnimation(fig, move_point_lights, frames=n_frames, interval=dt * n_frames, blit=True, save_count=True)

plt.show()
