
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and the figure size
num_points = 15
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Initialize positions for the point-lights
def initialize_points():
    # Setup y-coordinates for a tall figure representation of a sad man
    y_coords = np.array([-0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    return np.zeros(num_points), y_coords

# Initialize point-lights on the canvas
points = ax.scatter([], [], color='white', s=100)

# Define the waving motion
def wave_motion(i):
    # X position oscillates to create a waving effect
    x_positions = np.array([0, 0, 0, np.sin(i / 10), np.sin(i / 10), np.sin(i / 10), 0, 0, 0, -np.sin(i / 10), -np.sin(i / 10), -np.sin(i / 10), 0, 0, 0])
    y_positions = y_coords.copy()
    points.set_offsets(np.column_stack((x_positions, y_positions)))

# Create animation object
ani = animation.FuncAnimation(fig, wave_motion, frames=np.arange(0, 200), interval=50)

# Show the animation
plt.show()
