
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
# These are just placeholder values; you'll need to adjust them
# to match the desired pose and motion.
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [-1, 4], [-2, 4],
    [0, 3], [1, 2], [2, 2], [-1, 2], [-2, 2],
    [0, 1], [1, 0], [-1, 0], 
    [0, -2], [0, -3]
])

# Number of frames in the animation
num_frames = 50

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo')


# Animation update function
def update(frame):
    # Calculate the new positions of the point lights for the current frame
    # Here's a simple example of oscillating motion
    x = initial_positions[:, 0] + np.sin(2 * np.pi * frame / num_frames) * np.array([0,0.5,0,-0.5,0,0,0.2,0,-0.2,0,0,0,0,0,0])
    y = initial_positions[:, 1] 


    # Simulate waving hand movement for point lights 5 and 6
    
    hand_x_offset = 0.5 * np.sin(4 * np.pi * frame / num_frames)
    x[4] += hand_x_offset  # Right hand
    x[3] -= hand_x_offset

    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=40)

# Show the animation or save as a gif

plt.show()



