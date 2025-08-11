
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5],  # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0],  # Left Elbow
    [1.0, 1.0],  # Right Elbow
    [-1.5, 0.5],  # Left Wrist
    [1.5, 0.5],  # Right Wrist
    [-0.2, 1.0],  # Left Hip
    [0.2, 1.0],  # Right Hip
    [-0.7, 0.0],  # Left Knee
    [0.7, 0.0],  # Right Knee
    [-0.7, -1.0], # Left Ankle
    [0.7, -1.0], # Right Ankle
    [-0.5, -1.5], # Left Foot
    [0.5, -1.5]   # Right Foot
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    plt.cla()

    # Define the point-light positions for the current frame
    # This is where the animation logic goes
    # For simplicity, let's make the person sway back and forth
    angle = np.sin(2 * np.pi * i / num_frames) * 0.2
    offset_x = np.array([angle, angle, angle, angle, angle, angle, angle, angle, angle, angle, angle, angle, angle, angle, angle])
    positions = initial_positions + np.stack([offset_x, np.zeros(15)], axis=1)

    # Rotate the lower legs and feet as the person sits down and gets up
    sit_angle = np.sin(2 * np.pi * i / (4 * num_frames)) * np.pi / 4
    knee_angle = np.sin(2 * np.pi * i / (4 * num_frames)) * np.pi / 2

    # Rotate the legs around the knees
    left_knee_x, left_knee_y = positions[9, 0], positions[9, 1]
    right_knee_x, right_knee_y = positions[10, 0], positions[10, 1]
    left_ankle_x = left_knee_x + (positions[11, 0] - left_knee_x) * np.cos(knee_angle) - (positions[11, 1] - left_knee_y) * np.sin(knee_angle)
    left_ankle_y = left_knee_y + (positions[11, 0] - left_knee_x) * np.sin(knee_angle) + (positions[11, 1] - left_knee_y) * np.cos(knee_angle)
    right_ankle_x = right_knee_x + (positions[12, 0] - right_knee_x) * np.cos(knee_angle) - (positions[12, 1] - right_knee_y) * np.sin(knee_angle)
    right_ankle_y = right_knee_y + (positions[12, 0] - right_knee_x) * np.sin(knee_angle) + (positions[12, 1] - right_knee_y) * np.cos(knee_angle)
    positions[11, 0], positions[11, 1] = left_ankle_x, left_ankle_y
    positions[12, 0], positions[12, 1] = right_ankle_x, right_ankle_y

    # Rotate the feet around the ankles
    left_ankle_x, left_ankle_y = positions[11, 0], positions[11, 1]
    right_ankle_x, right_ankle_y = positions[12, 0], positions[12, 1]
    left_foot_x = left_ankle_x + (positions[13, 0] - left_ankle_x) * np.cos(sit_angle) - (positions[13, 1] - left_ankle_y) * np.sin(sit_angle)
    left_foot_y = left_ankle_y + (positions[13, 0] - left_ankle_x) * np.sin(sit_angle) + (positions[13, 1] - left_ankle_y) * np.cos(sit_angle)
    right_foot_x = right_ankle_x + (positions[14, 0] - right_ankle_x) * np.cos(sit_angle) - (positions[14, 1] - right_ankle_y) * np.sin(sit_angle)
    right_foot_y = right_ankle_y + (positions[14, 0] - right_ankle_x) * np.sin(sit_angle) + (positions[14, 1] - right_ankle_y) * np.cos(sit_angle)
    positions[13, 0], positions[13, 1] = left_foot_x, left_foot_y
    positions[14, 0], positions[14, 1] = right_foot_x, right_foot_y

    # Plot the point-lights
    plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

    # Set the plot limits
    plt.xlim([-2, 2])
    plt.ylim([-2, 2.5])

    # Set the background color
    plt.gca().set_facecolor('black')

    # Remove the axis labels and ticks
    plt.xticks([])
    plt.yticks([])

    return plt.gca(),

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=False, repeat=True)

# Save the animation as a GIF
ani.save('sitting_animation.gif', writer='pillow', fps=24)

# Show the animation
plt.show()
