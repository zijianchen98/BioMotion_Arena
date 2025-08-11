
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of point-lights
num_points = 15

# Define the initial positions of the point-lights (standing pose)
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.2, 1.7], # Left shoulder
    [0.2, 1.7],  # Right shoulder
    [-0.4, 1.4], # Left elbow
    [0.4, 1.4],  # Right elbow
    [-0.6, 1.1], # Left hand
    [0.6, 1.1],  # Right hand
    [-0.1, 1.3], # Hip left
    [0.1, 1.3],  # Hip right
    [-0.3, 0.8], # Knee left
    [0.3, 0.8],  # Knee right
    [-0.4, 0.3], # Foot left
    [0.4, 0.3],  # Foot right
    [-0.1, 1.5], # Torso left
    [0.1, 1.5]   # Torso right
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Set the axis limits
    ax.set_xlim([-1.0, 1.0])
    ax.set_ylim([0.0, 2.5])

    # Turn off the axis labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Calculate the angle of rotation (rolling)
    angle = (i / num_frames) * 2 * np.pi

    # Calculate the center of rotation
    center = np.array([0.0, 1.2])

    # Define the rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Rotate the point-light positions
    rotated_positions = np.dot(initial_positions - center, rotation_matrix) + center

    # Apply some translational movement to simulate the rolling motion
    translation = np.array([0.0, (i / num_frames) * -0.01])
    translated_positions = rotated_positions + translation
    
    # Plot the point-lights in white
    ax.plot(translated_positions[:, 0], translated_positions[:, 1], 'wo', markersize=8) # White circles
    
    # Set title for the frame
    ax.set_title('Sadman Forward Rolling', color='white')

    return ax

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=False, repeat=True)

# Save the animation
# ani.save('sadman_forward_rolling.mp4', writer='ffmpeg', fps=30)  # You need ffmpeg installed

# Show the animation
plt.show()
