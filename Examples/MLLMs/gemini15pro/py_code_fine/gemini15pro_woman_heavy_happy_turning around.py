
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be replaced with actual motion capture data or similar
# to achieve realistic biomechanical movement.  This example just rotates.
num_frames = 60
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

center_x = 200
center_y = 150

points = np.array([
    [0, 60], [-20, 40], [20, 40],  # Head
    [-30, 20], [30, 20],  # Shoulders
    [-20, 0], [20, 0],   # Elbows
    [-15, -20], [15, -20], # Hands
    [-20, -40], [20, -40],  # Hips
    [-15, -60], [15, -60],   # Knees
    [-10, -80], [10, -80] # Feet
])

for frame in range(num_frames):
    angle = frame * 2 * np.pi / num_frames
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    rotated_points = points @ rotation_matrix
    x[:, frame] = rotated_points[:, 0] + center_x
    y[:, frame] = rotated_points[:, 1] + center_y


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 400])
ax.set_ylim([0, 300])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-light scatter plot
scatter = ax.scatter([], [], s=20, c='white')

# Define the animation update function
def update(frame):
    scatter.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Display or save the animation (uncomment to save)
plt.show()
# ani.save('biological_motion.gif', writer='pillow', fps=30)
