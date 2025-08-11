
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
# These positions are approximate and will need to be adjusted
# to create a more realistic running motion
initial_positions = np.array([
    [0, 4.0],  # Head
    [-0.5, 3.5],  # Left Shoulder
    [0.5, 3.5],  # Right Shoulder
    [-1.5, 3.0],  # Left Elbow
    [1.5, 3.0],  # Right Elbow
    [-0.5, 2.5],  # Left Wrist
    [0.5, 2.5],  # Right Wrist
    [0, 2.5],  # Hip Center
    [-0.5, 1.5],  # Left Hip
    [0.5, 1.5],  # Right Hip
    [-1.0, 0.5],  # Left Knee
    [1.0, 0.5],  # Right Knee
    [-1.0, -0.5],  # Left Ankle
    [1.0, -0.5],  # Right Ankle
    [0, -1.0], # feet
])

# Define the range of motion for each point-light
# These values are approximate and will need to be adjusted
# to create a more realistic running motion
motion_range = np.array([
    [0, 0.1],  # Head
    [0, 0.1],  # Left Shoulder
    [0, 0.1],  # Right Shoulder
    [-0.5, 0.5],  # Left Elbow
    [0.5, -0.5],  # Right Elbow
    [-0.5, 0.5],  # Left Wrist
    [0.5, -0.5],  # Right Wrist
    [0, 0.5],  # Hip Center
    [0, 0.5],  # Left Hip
    [0, -0.5],  # Right Hip
    [-0.5, 0.5],  # Left Knee
    [0.5, -0.5],  # Right Knee
    [-0.5, 0.5],  # Left Ankle
    [0.5, -0.5],  # Right Ankle
    [0, 0.1] # feet
])

# Define the phase shift for each point-light
# This value will need to be adjusted to create a more
# realistic running motion
phase_shift = np.array([
    0,  # Head
    0,  # Left Shoulder
    0,  # Right Shoulder
    np.pi / 2,  # Left Elbow
    np.pi / 2,  # Right Elbow
    np.pi,  # Left Wrist
    np.pi,  # Right Wrist
    0,  # Hip Center
    0,  # Left Hip
    0,  # Right Hip
    np.pi / 2,  # Left Knee
    np.pi / 2,  # Right Knee
    np.pi,  # Left Ankle
    np.pi,  # Right Ankle
    0
])

# Create the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Black background
ax.set_xlim([-3, 3])
ax.set_ylim([-2, 5])
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Define the animation function
def animate(i):
    # Calculate the positions of the point-lights for the current frame
    x = initial_positions[:, 0] + motion_range[:, 0] * np.sin(i / 10 + phase_shift)
    y = initial_positions[:, 1] + motion_range[:, 1] * np.cos(i / 10 + phase_shift)

    # Update the scatter plot
    data = np.stack([x, y], axis=1)
    scat.set_offsets(data)

    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Save the animation as a GIF
# ani.save('sadwoman_running.gif', writer='imagemagick', fps=30)

plt.show()
