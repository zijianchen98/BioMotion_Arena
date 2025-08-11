
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for point-light configuration
num_points = 15
interval = 50  # milliseconds for the animation frame rate

# Define the initial positions of the point-lights representing a jumping action
# The positions are based on a simplified skeleton model
initial_positions = np.array([
    [0, 1],   # head
    [-0.5, 0.5], [0.5, 0.5],  # shoulders
    [-0.5, 0], [0.5, 0],      # elbows
    [-0.5, -0.5], [0.5, -0.5], # hands
    [0, 0],                     # hips
    [-0.3, -1], [0.3, -1],     # knees
    [-0.2, -1.5], [0.2, -1.5],  # feet
    [0, -1]                     # additional point for the grounded reference
])

# Create the jump motion
def create_jump_motion(frames):
    heights = np.linspace(0, 1, frames)
    jump_motion = []
    for height in heights:
        # Simulate jumping motion by changing the Y coordinates
        y_pos = initial_positions[:, 1] + height * 3 * (1 - height)  # Smooth jump
        jump_motion.append(np.column_stack((initial_positions[:, 0], y_pos)))
    return jump_motion

# Setting up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # white points

# Create jump motion data
jump_frames = 60  # total number of frames for the jump
jump_motion = create_jump_motion(jump_frames)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    points_data = jump_motion[i % jump_frames]  # Loop through the frames
    points.set_data(points_data[:, 0], points_data[:, 1])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, animate, frames=jump_frames, init_func=init,
                              blit=True, interval=interval)

# Show the animation
plt.show()
