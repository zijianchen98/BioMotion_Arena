
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters
num_points = 15
duration = 4  # seconds
fps = 30  # frames per second
num_frames = duration * fps

# Initialize positions of the point-lights
# These coordinates represent a simple point-light model for a running motion
# Positions can be derived from key body points in a running pose

# Initial positions (x, y) for 15 points representing joints
initial_positions = np.array([
    [0, 4],  # Head
    [-1, 3], [1, 3],  # Shoulders
    [-1.5, 2], [1.5, 2],  # Elbows
    [-1, 1], [1, 1],  # Hands
    [0, 0],  # Torso
    [-1, -1], [1, -1],  # Hips
    [-1.5, -2], [1.5, -2],  # Knees
    [-1, -3], [1, -3],  # Feet
    [0, -4]  # Weight
])

# Function to generate running motion
def get_running_positions(frame):
    base_y = -2 * np.sin(2 * np.pi * (frame / num_frames))
    x_movement = 0.1 * np.cos(2 * np.pi * (frame / num_frames))
    
    # Update positions to create the running motion effect
    positions = initial_positions.copy()
    positions[:, 1] += base_y  # Oscillating up and down for running effect
    positions[:, 0] += x_movement  # Shift left and right
    
    return positions

# Setup the plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Animation update function
def update(frame):
    positions = get_running_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
