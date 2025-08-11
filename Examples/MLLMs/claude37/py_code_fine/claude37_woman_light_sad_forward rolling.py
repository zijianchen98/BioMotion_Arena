
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
num_frames = 100
roll_radius = 1.0

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize the point positions
def init():
    points.set_data([], [])
    return points,

# Function to update the animation
def update(frame):
    # Calculate positions for forward rolling motion
    angles = np.linspace(0, 2 * np.pi, num_points) + frame * np.pi / 50
    x = roll_radius * np.cos(angles)
    y = roll_radius * np.sin(angles) - frame / 30 + 2  # downward transition

    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init,
                              blit=True, interval=50)

plt.show()
