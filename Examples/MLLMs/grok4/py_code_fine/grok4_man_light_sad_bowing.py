
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
num_points = 15  # Number of point-lights
duration = 100   # Duration of the animation in ms
fps = 30         # Frames per second
num_frames = fps * (duration / 1000)  # Total number of frames

# Define initial positions of point-lights (static).
# This is a simplified representation for a bowing motion.
initial_positions = np.array([
    [0, 5], [1, 5], [-1, 5],   # Head
    [0, 4], [1, 4], [-1, 4],   # Shoulders
    [0, 3], [1, 3], [-1, 3],   # Upper body
    [0, 1], [1, 1], [-1, 1],   # Knees
    [0, 0], [1, 0], [-1, 0],   # Feet
])

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 6)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Create the animation function
def animate(frame):
    # Calculate the bowing motion
    bowing_effect = np.sin(np.pi * frame / num_frames) * 0.5  # Simple bowing effect
    moved_positions = initial_positions.copy()
    moved_positions[:, 1] -= bowing_effect  # Move points downwards to simulate bowing
    points.set_data(moved_positions[:, 0], moved_positions[:, 1])
    return points,

# Initialize animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000 / fps, blit=True)

# Show the animation
plt.show()
