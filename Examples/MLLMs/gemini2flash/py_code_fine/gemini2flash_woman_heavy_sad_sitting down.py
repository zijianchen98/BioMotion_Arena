
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights
# These values are just placeholders. You will need to adjust them to create
# the desired motion.
initial_positions = np.array([
    [0, 20],  # Head
    [-5, 15], # Left Shoulder
    [5, 15],  # Right Shoulder
    [-8, 10], # Left Elbow
    [8, 10],  # Right Elbow
    [-10, 5], # Left Wrist
    [10, 5],  # Right Wrist
    [-2, 10], # Left Hip
    [2, 10],  # Right Hip
    [-4, 5],  # Left Knee
    [4, 5],   # Right Knee
    [-5, 0],  # Left Ankle
    [5, 0],   # Right Ankle
    [-2, 12], # Torso upper
    [0, 6]   # Torso lower
])

num_points = initial_positions.shape[0]

# Define the function that updates the positions of the point-lights for each frame
def update_points(frame_num):
    # Calculate the new positions of the point-lights based on the frame number
    # These calculations are just placeholders. You will need to adjust them to
    # create the desired motion.
    x = np.sin(frame_num * 0.1)
    y = np.cos(frame_num * 0.1)
    new_positions = initial_positions + np.array([x, -y])

    # Update the scatter plot with the new positions
    scatter.set_offsets(new_positions)
    return scatter,


# Create the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([-20, 20])
ax.set_ylim([-10, 30])
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, interval=50, blit=True, save_count=num_frames)

# Show the animation
plt.show()
