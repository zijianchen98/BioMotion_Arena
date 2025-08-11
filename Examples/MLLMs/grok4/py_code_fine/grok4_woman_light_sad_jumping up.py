
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Setup initial positions for the point lights (skeleton-like structure)
initial_positions = np.array([
    [0, 8],   # Head
    [-1, 6],  # Left Shoulder
    [1, 6],   # Right Shoulder
    [-1, 4],  # Left Elbow
    [1, 4],   # Right Elbow
    [-1, 2],  # Left Hand
    [1, 2],   # Right Hand
    [0, 6],   # Torso
    [0, 2],   # Hips
    [-1, 0],  # Left Knee
    [1, 0],   # Right Knee
    [-1, -2], # Left Foot
    [1, -2],  # Right Foot
])

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 10)
ax.set_facecolor('black')
points, = plt.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    # Calculate the vertical position of the jump
    jump_height = np.sin(frame / 10) * 5
    # Update y-coordinates for the jump motion
    adjusted_positions = initial_positions.copy()
    adjusted_positions[:, 1] += jump_height

    # Update points data
    points.set_data(adjusted_positions[:, 0], adjusted_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
