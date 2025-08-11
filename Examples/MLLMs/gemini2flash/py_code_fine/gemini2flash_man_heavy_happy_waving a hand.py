
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 7],  # Head
    [-1, 6], [1, 6],  # Shoulders
    [-2, 5], [2, 5],  # Elbows
    [-3, 4], [3, 4],  # Wrists
    [0, 5],  # Torso top
    [0, 4],  # Torso middle
    [-0.5, 3], [0.5, 3],  # Hips
    [-0.5, 2], [0.5, 2],  # Knees
    [-0.5, 1], [0.5, 1]   # Ankles
])

# Define the amplitude of the waving motion
wave_amplitude = 0.5

# Define the frequency of the waving motion
wave_frequency = 0.1

# Define the function that updates the positions of the point-lights for each frame
def update_points(frame_num, points):
    # Calculate the x-offset of the left wrist based on the frame number
    left_wrist_x_offset = wave_amplitude * np.sin(wave_frequency * frame_num)

    # Calculate the x-offset of the right wrist based on the frame number
    right_wrist_x_offset = -wave_amplitude * np.sin(wave_frequency * frame_num)

    # Update the positions of the left and right wrists
    points.set_offsets([
        [initial_positions[5, 0] + left_wrist_x_offset, initial_positions[5, 1]],  # Left wrist
        [initial_positions[6, 0] + right_wrist_x_offset, initial_positions[6, 1]]  # Right wrist
    ])

    return points,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Set the limits of the axes
ax.set_xlim([-5, 5])
ax.set_ylim([0, 8])

# Hide the axes labels and ticks
ax.set_xticks([])
ax.set_yticks([])

# Create the scatter plot for the 15 point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points,), blit=False, frames=num_frames, repeat=True)

# Save the animation to a GIF file
# ani.save('waving_man.gif', writer='imagemagick', fps=30)

# Show the animation
plt.show()
