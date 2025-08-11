
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100  # Number of frames in the animation
repeat_count = 3  # Number of times the animation runs
weight_y_offset = -0.5  # Offset for the heavy weight
walking_amplitude = 0.05  # Amplitude of the walking motion

# Initial positions of point-lights for a walking motion
initial_positions = np.array([
    [0, 0],  # Head
    [-0.1, -0.5],  # Left shoulder
    [0.1, -0.5],  # Right shoulder
    [-0.1, -0.8],  # Left elbow
    [0.1, -0.8],  # Right elbow
    [-0.1, -1.1],  # Left wrist
    [0.1, -1.1],  # Right wrist
    [0, -1.6],  # Spine
    [-0.2, -1.5],  # Left hip
    [0.2, -1.5],  # Right hip
    [-0.2, -2.0],  # Left knee
    [0.2, -2.0],  # Right knee
    [-0.2, -2.5],  # Left ankle
    [0.2, -2.5],  # Right ankle
    [0, -2.8],  # Weight position (center of the weight)
])

# Walking motion function (simple x-axis bobbing)
def update_point_lights(frame):
    # Clear the previous positions
    for i in range(num_points):
        pos[i][1] = initial_positions[i][1] + walking_amplitude * np.sin(2 * np.pi * (frame / frames) + i)
        pos[i][0] = initial_positions[i][0] + (0.02 * np.sin(2 * np.pi * (frame / frames) + (i / 2)))  # Side to side

    points.set_offsets(pos)

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-3, 0)
ax.set_facecolor('black')

# Initialize point-lights
pos = np.zeros((num_points, 2))
points = ax.scatter(pos[:, 0], pos[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_point_lights, frames=frames,
                              repeat=repeat_count, interval=1000/30)

# Show the animation
plt.show()
