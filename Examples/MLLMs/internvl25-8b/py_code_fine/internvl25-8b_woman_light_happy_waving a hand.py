
import matplotlib.pyplot as plt
import numpy as np

# Number of points
n_points = 15

# Duration of the animation in seconds
duration = 2

# Time step for the animation
time_step = 0.1

# Framerate for the animation
framerate = 1 / time_step

# Array of time points
t = np.arange(0, duration, time_step)

# Number of points in x and y directions
nx, ny = 3, 5

# Arrays to store x and y coordinates
x = np.zeros((len(t), n_points, nx, ny))
y = np.zeros((len(t), n_points, nx, ny))

# Define the initial positions of points
points = np.indices(n_points)

# Define the wave pattern
wave_pattern = np.linspace(0, 4 * np.pi, n_points)

# Define the wave function
def wave_function(t):
    return np.sin(wave_pattern + 2 * np.pi * 1 * t)

# Generate the animation for each point
for i in range(n_points):
    x[:, i, :, :] = wave_function(t) * 5  # x-coordinates
    y[:, i, :, :] = np.zeros_like(x[:, i, :, :])  # y-coordinates

# Function to display the points
def plot_points(ax, x, y):
    ax.clear()
    for j in range(len(x)):
        for i in range(n_points):
            ax.plot(x[j, i], y[j, i], 'o', color='white')
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])

# Create the figure and subplots
fig, axs = plt.subplots(1, n_points, figsize=(2, 2), gridspec_kw={'width_ratios': [1]*n_points})

# Create animation
ani = animation.FuncAnimation(
    fig, 
    lambda i: plot_points(axs[i], x[i], y[i]),
    frames=len(t),
    interval=1000 / framerate,
    blit=True
)

plt.xlabel('Duration (s)')
plt.show()
