
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15
duration = 2  # seconds
fps = 30  # frames per second
frames = duration * fps

# Point positions for the sadman with heavy weight jumping forward
# Initial position for points (representing head, body, limbs)
initial_positions = np.array([
    [0, 2],   # Head
    [-1, 1],  # Left shoulder
    [1, 1],   # Right shoulder
    [-1, 0],  # Left elbow
    [1, 0],   # Right elbow
    [-1, -1], # Left hand
    [1, -1],  # Right hand 
    [0, 0],   # Body (torso)
    [-0.5, -2], # Left hip
    [0.5, -2],  # Right hip
    [-0.5, -3], # Left knee
    [0.5, -3],  # Right knee
    [-0.5, -4], # Left foot
    [0.5, -4],  # Right foot
    [-0.5, -2.5], # Extra point for balance
    [0.5, -2.5]   # Extra point for balance
])

# Adjust positions for the jumping motion
def generate_frames():
    for i in range(frames):
        t = i / frames
        height = np.sin(t * np.pi)  # Height of the jump
        forward_movement = t * 4  # Forward linear motion (4 units)
        positions = initial_positions.copy()
        positions[:, 0] += forward_movement  # Move forward
        positions[:, 1] += height          # Jump height
        yield positions

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = plt.plot([], [], 'o', color='white')

# Animation initialization
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    positions = next(generate_frames())
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

# Display the animation
plt.show()
