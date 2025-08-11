
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters for the animation
num_points = 15
frames = 100
interval = 50  # milliseconds

# Define the initial positions of point-lights (x, y)
initial_positions = np.array([
    [0, 2],   # Head
    [-0.5, 1.5], [0.5, 1.5],  # Shoulders
    [-0.75, 1], [0.75, 1],  # Upper arms
    [-0.5, 0.5], [0.5, 0.5],  # Elbows
    [-0.25, 0], [0.25, 0],  # Wrists
    [-0.5, -1], [0.5, -1],  # Hips
    [-0.75, -2], [0.75, -2],  # Thighs
    [-0.5, -3], [0.5, -3],  # Knees
    [-0.25, -4], [0.25, -4]   # Feet
])

# Function to simulate the sitting down motion
def update_positions(frame):
    # Calculate the downward motion effects
    y_shift = -0.03 * frame  # Controls how fast the subjects sit down
    new_positions = initial_positions.copy()
    new_positions[:, 1] += y_shift
    return new_positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-5, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize the animation
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    new_positions = update_positions(frame)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=interval, blit=True)

# Display the animation
plt.show()
