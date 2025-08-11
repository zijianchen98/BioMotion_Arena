
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    """Initialize the position and velocity of points."""
    global points
    points.set_data(points[:, 0], points[:, 1])
    vel[0] = [0, 0]  # Start the velocity loop
    return points,

def update(frame):
    """Update positions using the velocities."""
    vel = np.roll(vel, 1)
    vel[0] = [0, 0]  # Maintain the loop for continuous running

    dx = 500 * np.cos(2 * np.pi * 0.02 * frame)
    dy = 500 * np.sin(2 * np.pi * 0.02 * frame)
    for i in range(15):
        x = points[i, 0] + dx * np.cos(np.linspace(0, 2 * np.pi, 7))
        y = points[i, 1] + dx * np.sin(np.linspace(0, 2 * np.pi, 7))
        points[i] = x + vel[frame % 15][i] * dy / 7

    return points,

# Setup figure
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# Create point-lights
points = [[np.cos(np.linspace(0, 2 * np.pi, 15))[j] * 0.7,
           np.sin(np.linspace(0, 2 * np.pi, 15))[j] * 0.7]
          for j in range(15)]
vel = np.zeros((15, 2))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=500, init_func=init, blit=True)

# Show the animation
plt.subplots_adjust(bottom=0, top=1)
plt.show()
