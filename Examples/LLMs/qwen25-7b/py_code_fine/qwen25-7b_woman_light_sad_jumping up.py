
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the total duration of the animation
num_points = 15
total_frames = 10

# Define the time steps and positions for the jump
time_steps = np.linspace(0, 1, total_frames)
positions = np.zeros((total_frames, num_points, 2))

# Define the initial position of the points (sad woman shape)
initial_positions = np.array([
    [0.2, -0.2], [0.4, -0.1], [0.6, -0.1], (0.8, -0.1), (1.0, -0.1),
    (1.2, -0.2), (1.4, -0.3), (1.6, -0.4), (1.8, -0.4), (2.0, -0.3),
    (2.2, -0.2), (2.4, -0.1), (2.6, -0.1), (2.8, -0.1), (3.0, -0.1)
])

# Define the jump motion
for t in range(total_frames):
    alpha = t / (total_frames - 1)
    positions[t] = initial_positions + np.array([
        [0.5 * (1 - np.sin(10 * np.pi * alpha)), 0.5 * (1 - np.sin(10 * np.pi * alpha))],
        [1.5 * (1 - np.sin(10 * np.pi * alpha)), 1.5 * (1 - np.sin(10 * np.pi * alpha))],
        (2.5 * (1 - np.sin(10 * np.pi * alpha)), 2.5 * (1 - np.sin(10 * np.pi * alpha)))]
    ])

# Create the figure and axis
fig, ax = plt.subplots()
ax.ax.set_xlim(-5, 5)
1.ax.set_ylim(-5, 5)
1.ax.set_aspect('equal')
1.ax.axis('off')

# Initialize the scatter plot
points, = 1.ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    x_points.set_data(positions[i, :, 0], positions[i, :, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=total_frames, interval=50)

# Show the animation
plt.show()
