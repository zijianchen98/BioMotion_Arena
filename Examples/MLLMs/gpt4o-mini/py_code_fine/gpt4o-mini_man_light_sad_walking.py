
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize parameters
num_points = 15
frames = 60
speed = 0.05
height = 10
width = 6

# Walking points coordinates (initial positions)
# Representing a simplified model of a sadman walking
base_positions = np.array([
    [0, 2], [1, 3], [-1, 3],  # Head
    [0, 1],                   # Neck
    [0, 0], [1, 0], [-1, 0],  # Body
    [0, -1], [1, -1], [-1, -1],  # Hips
    [0, -2], [1, -2], [-1, -2],  # Legs
    [0, -3], [1, -3], [-1, -3]   # Feet
])

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-width/2, width/2)
ax.set_ylim(-height/2, height/2)
ax.set_facecolor('black')

# Create points
points, = ax.plot([], [], 'o', color='white')

def update(frame):
    # Calculate the new positions based on walking motion
    time = frame * speed
    # Sinusoidal movement to mimic walking
    offsets = np.array([np.sin(time + i) * 0.1 for i in range(num_points)])
    new_positions = base_positions.copy()
    new_positions[:, 1] += offsets  # Apply vertical movement
    
    # Update data for animation
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/30, blit=True)

plt.show()
