
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration for the animation
num_points = 15
duration = 200  # milliseconds
frames = 60  # total number of frames

# Define a grid of points that represent the sadman's joints
# Here we define their initial positions on a black background
initial_positions = np.array([
    [1, 4], [0, 3], [2, 3],  # Head and shoulders
    [0, 2], [1, 2], [2, 2],  # Mid body
    [0, 1], [1, 1], [2, 1],  # Thighs
    [0, 0], [1, 0], [2, 0]   # Feet
])

# Define movement for turning around with weights
turning_motion = np.array([
    [np.cos(np.linspace(0, np.pi, frames))],  # rotating around y-axis
    [np.sin(np.linspace(0, np.pi, frames))]   # lowering while turning
])

# Create a figure and axis to draw on
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 5)
ax.set_facecolor('black')
points = ax.plot([], [], 'o', color='white')[0]

# Animation function
def update(frame):
    angle = np.pi / frames * frame
    x = initial_positions[:, 0] * np.cos(angle) - initial_positions[:, 1] * np.sin(angle)
    y = initial_positions[:, 0] * np.sin(angle) + initial_positions[:, 1] * np.cos(angle) - 1  # Simulate weight
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=duration/frames, blit=True)

# Show the animation
plt.show()
