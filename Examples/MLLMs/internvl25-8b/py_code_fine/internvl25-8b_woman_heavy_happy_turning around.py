
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_axis_off()

lights = ax.scatter([], [], color='white')

# Define initial positions of the point lights
initial_positions = np.random.uniform(-1.5, 1.5, (15, 2))

# Angle for turning (in radians)
angle = np.pi / 4  # 45 degrees

# Define turning motion parameterizes
turn_radius = 0.3
turn_speed = 0.05

# Rotation matrix for turning around z-axis
def rotation_matrix_z(angle):
    c, s = np.cos(angle), np.sin(angle)
    return np.array(([c, -s, 0], [s, c, 0], [0, 0, 1]))

# Function to update the position of lights
def update(frame):
    positions = initial_positions + turn_radius * rotation_matrix_z(frame * turn_speed) @ np.array([0, 0, 1])
    lights.set_offsets(positions)
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 8), interval=100, blit=True)

# Save the animation
ani.save('woman_turning.gif', writer='imagemagick', fps=10)

plt.show()
