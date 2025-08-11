
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 200  # Duration of the animation in frames
frames_per_cycle = 30  # Number of frames for one running cycle

# Define positions for 15 point-lights for the running action
def get_running_positions(frame):
    t = frame / frames_per_cycle * 2 * np.pi  # Normalizing to a complete cycle
    # Define a vertical straight line for the body with slight horizontal movement
    y_positions = np.linspace(-6, 3, num_points)
    x_positions = np.sin(t) * (1 + np.linspace(0, 1, num_points))
    return x_positions, y_positions

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)  # Set x limits
ax.set_ylim(-7, 1)  # Set y limits
ax.set_facecolor('black')  # Background
ax.set_xticks([])  # Remove x ticks
ax.set_yticks([])  # Remove y ticks

# Create point-lights
points, = ax.plot([], [], 'o', color='white')  # Point-light representation

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    x, y = get_running_positions(frame)
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=duration, init_func=init,
                              blit=True, interval=50)

# Show animation
plt.show()
