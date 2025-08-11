
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the time parameters
dt = 0.02
t_max = 10
time = np.arange(0, t_max, dt)

# Define the movement parameters
amplitude = 0.5
frequency = 1

# Define the initial positions of the point-lights
# These positions are based on a typical running motion
x0 = np.array([
    -0.3, -0.2, -0.1,  0.1,  0.2,  0.3,  # Left leg
     0.1,  0.2,  0.3, -0.3, -0.2, -0.1,  # Right leg
    -0.1,  0.1, -0.2,  0.2, -0.1,  0.1   # Torso and arms
])
y0 = np.array([
     0.5,  0.4,  0.3,  0.3,  0.4,  0.5,  # Left leg
    -0.5, -0.4, -0.3, -0.3, -0.4, -0.5,  # Right leg
     0.8,  0.7,  0.6,  0.6,  0.7,  0.8   # Torso and arms
])

# Define the movement of each point-light
x = np.zeros((len(time), n_points))
y = np.zeros((len(time), n_points))
for i in range(n_points):
    x[:, i] = x0[i] + amplitude * np.sin(2 * np.pi * frequency * time)
    y[:, i] = y0[i] + amplitude * np.sin(2 * np.pi * frequency * time + np.pi / 2)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points = ax.scatter(x[0, :], y[0, :], c='white', s=10)

# Define the animation function
def animate(i):
    points.set_offsets(np.column_stack((x[i, :], y[i, :])))
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(time), interval=dt*1000, blit=True)

plt.show()
