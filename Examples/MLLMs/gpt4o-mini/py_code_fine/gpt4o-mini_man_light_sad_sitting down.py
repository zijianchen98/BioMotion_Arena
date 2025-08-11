
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Define the initial positions of the points (15 points representing a sad man sitting down)
num_points = 15
initial_positions = np.array([
    [5, 8],  # head
    [4.5, 7], [5, 7], [5.5, 7],  # shoulders
    [4, 6], [4.5, 6], [5, 6], [5.5, 6], [6, 6],  # upper body
    [4, 5], [4.5, 5], [5, 5], [5.5, 5], [6, 5],  # lower body
    [5, 4],  # sitting position (butt)
    [4.5, 4], [5.5, 4]  # feet
])

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to animate
def animate(frame):
    # Amplitude of the sway (for a natural sitting down motion)
    sway_amplitude = 0.1
    sway = np.sin(frame / 10) * sway_amplitude

    # Update positions to represent the sitting motion
    positions = initial_positions.copy()
    # Simulate a slight bounce/ sway
    positions[:, 1] += sway

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
