
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
duration = 5  # Duration of the animation in seconds
fps = 30  # Frames per second
num_frames = duration * fps

# Initial positions of the point lights (15 points)
initial_positions = np.array([
    [0, 5], [1, 4], [-1, 4], [0, 3],  # Head and shoulders
    [1, 2], [-1, 2], [0, 1],  # Upper body
    [0.5, 0], [-0.5, 0],  # Hips
    [1, -1], [-1, -1],  # Thighs
    [1.5, -2], [-1.5, -2],  # Knees
    [0, -3],  # Feet
])

# Create an empty array for the positions over time
positions = np.zeros((num_frames, num_points, 2))

# Generate the forward roll motion
for frame in range(num_frames):
    t = frame / num_frames
    roll_position = np.array([
        initial_positions[:, 0] + (t-0.5) * 4,  # Horizontal shift
        initial_positions[:, 1] - 5 * (t - 0.5)**2  # Vertical motion for roll effect
    ]).T
    positions[frame] = roll_position

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create the point lights
points, = ax.plot([], [], 'o', color='white')

# Initialize the animation
def init():
    points.set_data([], [])
    return points,

# Update function for the animation
def update(frame):
    points.set_data(positions[frame, :, 0], positions[frame, :, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=1000/fps)

# Show the animation
plt.show()
