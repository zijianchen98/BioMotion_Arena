
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 60  # Number of frames in the animation

# Define the initial positions of the point-lights (skeleton)
base_positions = np.array([
    [-0.1, 0.5], [0.1, 0.5],  # Head
    [-0.15, 0.3], [0.15, 0.3],  # Shoulders
    [-0.1, 0.2], [0.1, 0.2],  # Elbows
    [-0.1, 0], [0.1, 0],      # Hands
    [-0.05, -0.1], [0.05, -0.1],  # Hips
    [-0.1, -0.3], [0.1, -0.3],  # Knees
    [-0.15, -0.5], [0.15, -0.5],  # Feet
])

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-0.3, 0.3)
ax.set_ylim(-0.6, 0.6)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # points in white

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Simple motion to simulate lying down (sway)
    sway_amplitude = 0.05 * np.sin(frame * 2 * np.pi / frames)
    
    # Update positions for the 'lying down' animation
    positions = base_positions.copy()
    positions[:, 1] += sway_amplitude  # Move the points up and down
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/30)

# Display the animation
plt.show()
