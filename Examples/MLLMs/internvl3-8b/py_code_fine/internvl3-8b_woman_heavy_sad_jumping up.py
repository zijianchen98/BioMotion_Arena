
import numpy as np
import matplotlib.pyplot as plt

# Set animation parameters
frame_duration = 0.1  # duration of each frame in seconds
num_frames = 50
total_animation_time = frame_duration * num_frames

# Define the path for the woman
path_points = np.array([
    [0.0, 0.5], [0.1, 0.45], [0.2, 0.3], [0.25, 0.1], [0.4, 0.05],
    [0.5, 0.2], [0.7, 0.25], [0.8, 0.4], [0.9, 0.5], [0.95, 0.65],
    [0.85, 0.8], [0.75, 0.9], [0.8, 0.95], [0.9, 0.95], [0.95, 0.95],
    [1.0, 0.8], [0.9, 0.7], [0.8, 0.6], [0.7, 0.5], [0.6, 0.45],
    [0.45, 0.3], [0.4, 0.2], [0.3, 0.1], [-0.1, 0.05], [-0.2, 0.2],
    [-0.3, 0.3], [-0.4, 0.45], [-0.5, 0.6], [-0.7, 0.8], [-0.8, 0.9],
    [-0.9, 0.95], [-0.95, 0.95], [-1.0, 0.80], [-0.9, 0.7], [-0.8, 0.65]
])

# Calculate the step size for each frame
step_size = total_animation_time / (len(path_points) - 1)

# Create frames
frames = np.linspace(0, total_animation_time, num_frames)

# Plotting setup
fig = plt.figure(figsize=(5, 5), dpi=80)
ax = fig.add_axes([0,0,1,1], frame_on=False, xticks=[], yticks=[])

for frame_num in range(num_frames):
    ax.cla()
    ax.set_facecolor('black')
    current_position = np.where(frames[frame_num] >= step_size)[0][0]
    current_point = path_points[current_position]

    # Draw a dot representing the woman
    ax.add_patch(plt.Circle((current_point[0], current_point[1]), 0.01, color='white'))

    # Display the frame
    plt.pause(frame_duration)

plt.ioff()
plt.show()
