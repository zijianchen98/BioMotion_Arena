
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
points, = ax.plot([], [], 'wo')

# Number of points
n_points = 15

# Define initial positions of points
# Using a simplified stick figure representation
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Upper body
    [0.6, 0.8],
    [0.45, 0.75],  # Lower body
    [0.55, 0.75],
    [0.45, 0.7],  # Hips
    [0.55, 0.7],
    [0.3, 0.6],  # Left arm
    [0.4, 0.6],
    [0.6, 0.6],  # Right arm
    [0.7, 0.6],
    [0.4, 0.5],  # Left leg
    [0.45, 0.4],
    [0.55, 0.4],  # Right leg
    [0.6, 0.5],
])

# Define target positions during jump
target_positions = initial_positions.copy()
target_positions[:, 1] += 0.2  # Jump height

# Function to update positions
def update(frame):
    t = frame / frames
    positions = (1 - t) * initial_positions + t * target_positions
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Animation parameters
frames = 60
interval = 50

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames*2, 
                                  interval=interval, blit=True)

plt.axis('off')
plt.show()
