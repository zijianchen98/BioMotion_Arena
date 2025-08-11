
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 2.0],   # Head
    [-0.3, 1.5],  # Left Shoulder
    [0.3, 1.5],   # Right Shoulder
    [-0.7, 0.8],  # Left Elbow
    [0.7, 0.8],   # Right Elbow
    [-1.0, 0.2],  # Left Wrist
    [1.0, 0.2],   # Right Wrist
    [-0.1, 0.7],  # Hip Center
    [-0.4, 0.1],  # Left Hip
    [0.4, 0.1],   # Right Hip
    [-0.7, -0.7], # Left Knee
    [0.7, -0.7], # Right Knee
    [-0.8, -1.3], # Left Ankle
    [0.8, -1.3], # Right Ankle
    [0, -1.7]    # Foot center
])

# Define the motion of the point-lights for a turning-around action with heavy weight
def update_points(frame_num):
    # Simulate a turning-around motion with some sadness and heavy weight by oscillating positions
    rotation_angle = np.sin(2 * np.pi * frame_num / num_frames) * 0.5  # Small angle to show "sad" look

    # Apply rotation to all points around center (0,0)
    rotated_positions = np.array([
        [x * np.cos(rotation_angle) - y * np.sin(rotation_angle),
         x * np.sin(rotation_angle) + y * np.cos(rotation_angle)]
        for x, y in initial_positions
    ])

    # Subtle head bobbing and shoulder swaying to emphasize the weight
    rotated_positions[0, 1] += 0.03 * np.sin(4 * np.pi * frame_num / num_frames)  # Head bobbing
    rotated_positions[1:3, 0] += 0.05 * np.cos(2 * np.pi * frame_num / num_frames)  # Shoulders swaying

    # Update scatter plot data
    scatter.set_offsets(rotated_positions)
    return scatter,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=20)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, blit=True, save_count=num_frames)

# Save the animation or display it
# To save:
# ani.save("sadwoman_turning.mp4", writer='ffmpeg', fps=30) # or .gif with Pillow
# To display:
plt.show()
