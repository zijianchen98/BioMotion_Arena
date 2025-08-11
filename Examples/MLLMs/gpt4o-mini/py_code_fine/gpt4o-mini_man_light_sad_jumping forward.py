
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initial positions of the point lights representing the sadman
# 15 points in a roughly humanoid shape
num_points = 15
initial_positions = np.array([
    [0, 5],   # Head
    [-1, 4], [0, 4], [1, 4],   # Shoulders
    [-1, 3], [0, 3], [1, 3],   # Upper body
    [-1, 2], [0, 2], [1, 2],   # Lower body
    [-1, 1], [0, 1], [1, 1],   # Thighs
    [-0.5, 0], [0.5, 0]        # Feet
])

# Define jump parameters
jump_height = 3
jump_duration = 20
forward_distance = 8
frames = 100

# Create a function to update the animation
def update(frame):
    t = frame / frames
    # Calculate position based on a jumping motion
    # Y position oscillates as a sine wave
    y_offsets = jump_height * (np.sin(np.pi * t) - 1)
    # Forward displacement effect
    forward_shift = forward_distance * t
    # Update point positions
    new_positions = initial_positions + np.array([forward_shift, y_offsets]).T
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=50)

# Show the animation
plt.show()
