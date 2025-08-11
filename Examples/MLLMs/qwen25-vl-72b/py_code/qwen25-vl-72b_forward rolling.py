
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points for a forward roll
initial_positions = np.array([
    [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
    [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
    [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]
])

# Define the target positions after a full rotation (forward roll)
target_positions = np.array([
    [4, 2], [3, 2], [2, 2], [1, 2], [0, 2],
    [4, 1], [3, 1], [2, 1], [1, 1], [0, 1],
    [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]
])

# Function to interpolate between initial and target positions over time
def interpolate_positions(t):
    return (1 - t) * initial_positions + t * target_positions

# Set up the figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
scat = ax.scatter([], [], s=50, color='white')

# Animation update function
def update(frame):
    t = frame / 100  # Normalize frame number to [0, 1] for interpolation
    new_positions = interpolate_positions(t)
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

plt.show()
