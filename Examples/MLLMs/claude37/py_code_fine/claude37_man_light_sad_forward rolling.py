
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_lights = 15
frames = 100
speed = 0.1  # speed of forward rolling

# Point-light positions for the sadman during forward roll
def generate_positions(frame):
    base_positions = np.array([
        [0, 3],   # Head
        [-1, 2],  [1, 2],  # Shoulders
        [-1, 1],  [1, 1],  # Arms
        [-0.5, 0], [0.5, 0],  # Body
        [-0.5, -1], [0.5, -1], # Legs
        [-0.3, -2], [0.3, -2],  # Feet
        [-0.2, -3], [0.2, -3],  # Lower Body
    ])
    
    # Roll forward movement
    z_movement = np.linspace(0, -2, frames)
    positions = base_positions + np.array([0, z_movement[frame]])
    
    return positions

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    positions = generate_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
