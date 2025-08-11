
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 point-lights
# These positions correspond to a person waving a hand
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], # Left Shoulder
    [0.3, 1.5],  # Right Shoulder
    [-0.6, 1.0], # Left Elbow
    [0.6, 1.0],  # Right Elbow
    [-0.9, 0.5], # Left Wrist
    [0.9, 0.5],  # Right Wrist
    [-0.1, 0.8], # Torso Top Left
    [0.1, 0.8],  # Torso Top Right
    [-0.1, 0.2], # Torso Bottom Left
    [0.1, 0.2],  # Torso Bottom Right
    [-0.2, -0.5], # Left Hip
    [0.2, -0.5], # Right Hip
    [-0.2, -1.2], # Left Knee
    [0.2, -1.2], # Right Knee
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Set the axis limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.axis('off')

    # Calculate the new positions of the point-lights
    # This example includes a simple waving motion
    positions = initial_positions.copy()
    positions[5, 0] += np.sin(i * 0.1) * 0.5  # Left wrist
    positions[5, 1] += np.cos(i * 0.1) * 0.2  # Left wrist
    positions[6, 0] += np.sin(i * 0.1 + np.pi) * 0.3 # Right wrist
    positions[6, 1] += np.cos(i * 0.1 + np.pi) * 0.1 # Right wrist
    positions[3, 0] += np.sin(i * 0.1) * 0.2 # Left Elbow
    positions[3, 1] += np.cos(i * 0.1) * 0.1 # Left Elbow
    positions[4, 0] += np.sin(i * 0.1 + np.pi) * 0.1 # Right Elbow
    positions[4, 1] += np.cos(i * 0.1 + np.pi) * 0.05 # Right Elbow

    # Plot the point-lights
    ax.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Save the animation as a GIF
ani.save('point_light_animation.gif', writer='pillow', fps=20)

# Show the animation
plt.show()
