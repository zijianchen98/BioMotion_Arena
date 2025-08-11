
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 5], [-1, 4], [1, 4],
    [-1, 3], [1, 3],
    [-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2],
    [-1, 0], [1, 0],
    [-1, -2], [0, -2], [1, -2]
])

# Number of frames in the animation
num_frames = 60

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)  # Set appropriate x-axis limits
ax.set_ylim(-5, 8)  # Set appropriate y-axis limits
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background color to black
points, = ax.plot([], [], 'wo', markersize=8)

# Function to update the positions of the points for each frame
def update(frame):
    # Wave motion: Simple sinusoidal wave for the hand
    wave_offset = np.sin(2 * np.pi * frame / num_frames)

    positions = initial_positions.copy()
    # Apply wave motion to the right arm points 
    positions[5:, 0] += wave_offset * 2 # Exaggerate motion
   
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=40, blit=True)


plt.show()

