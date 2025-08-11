
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Initialize positions for point-lights
# The positions array holds y-coordinates of the points
# The positions would represent a basic human figure like a waving action
positions = np.array([
    [0, 1],   # Head
    [-1, 0],  # Left shoulder
    [1, 0],   # Right shoulder
    [-1, -1], # Left elbow
    [1, -1],  # Right elbow
    [-1.5, -2], # Left hand
    [1.5, -2],  # Right hand
    [0, -2],   # Torso
    [-1, -3],  # Left knee
    [1, -3],   # Right knee
    [-1, -4],  # Left foot
    [1, -4],   # Right foot
])

# Make a copy of the base positions for animation
def update_positions(frame):
    # Create a waving effect for right hand (index 5)
    wave_amplitude = 0.5 * np.sin(frame / 10)
    right_hand = positions[6]
    right_hand[1] += wave_amplitude  # Alter y-coordinate for waving
    new_positions = positions.copy()
    new_positions[6] = right_hand
    return new_positions

# Initialize the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialization function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    pos = update_positions(frame)
    points.set_data(pos[:, 0], pos[:, 1])  # Update points data
    return points,

# Call the animator
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
