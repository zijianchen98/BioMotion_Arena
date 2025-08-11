
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 0],
    [0.1, 0.2],
    [0.1, -0.2],
    [0.3, 0.3],
    [0.3, -0.3],
    [0.6, 0.4],
    [0.6, -0.4],
    [0.9, 0.2],
    [0.9, -0.2],
    [1.2, 0.3],
    [1.2, -0.3],
    [1.5, 0.1],
    [1.5, -0.1],
    [1.7, 0.2],
    [1.7, -0.2]
])

# Define the forward rolling motion function
def forward_rolling_motion(t):
    theta = 0.1 * np.pi * t
    rolling_positions = initial_positions.copy()
    for i in range(15):
        x, y = initial_positions[i]
        rolling_positions[i] = [x - 0.05 * np.sin(theta), y * np.cos(theta)]
    return rolling_positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 1)
points, = ax.plot([], [], 'wo', markersize=10)

# Initialize the animation
def init():
    points.set_data([], [])
    return points,

def animate(t):
    positions = forward_rolling_motion(t)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, 100, 0.1), interval=50, blit=True)

# Display the animation
plt.axis('off')
plt.show()
