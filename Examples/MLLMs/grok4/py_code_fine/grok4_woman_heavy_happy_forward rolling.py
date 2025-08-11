
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Parameters for the animation
n_points = 15
frames = 100  # Total frames for animation

# Initial positions of the points representing body parts
def init():
    points.set_data([], [])
    return points,

# Generate a forward roll motion pattern
def forward_roll(frame):
    t = frame / frames * np.pi * 2  # Normalize to 2π for the full cycle
    # Position calculations
    y_positions = np.sin(t + np.linspace(0, np.pi, n_points)) * 0.5
    x_positions = np.linspace(-0.5, 0.5, n_points)
    
    points.set_data(x_positions, y_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, forward_roll, init_func=init, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
