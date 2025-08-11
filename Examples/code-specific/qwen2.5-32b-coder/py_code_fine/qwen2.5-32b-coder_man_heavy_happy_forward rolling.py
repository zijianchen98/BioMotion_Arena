
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
background_color = 'black'
point_color = 'white'
figsize = (8, 8)

# Initial positions of the lights (simplified model)
initial_positions = np.array([
    [0, 0], [-1, 1], [1, 1], [-2, 2], [2, 2], [-1, 2], [1, 2],
    [-1, -1], [1, -1], [-2, -2], [2, -2], [-1, -2], [1, -2],
    [0, 3], [0, -3]
])

# Function to simulate forward rolling motion
def forward_rolling(t):
    # Simplified motion equations
    x = initial_positions[:, 0] + 0.5 * np.sin(0.1 * t + np.linspace(0, 2 * np.pi, num_lights))
    y = initial_positions[:, 1] + 0.5 * np.cos(0.1 * t + np.linspace(0, 2 * np.pi, num_lights))
    return np.column_stack((x, y))

# Initialize plot
fig, ax = plt.subplots(figsize=figsize)
ax.set_facecolor(background_color)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

# Scatter plot for the points
scatter = ax.scatter([], [], s=100, c=point_color)

# Update function for animation
def update(frame):
    positions = forward_rolling(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
