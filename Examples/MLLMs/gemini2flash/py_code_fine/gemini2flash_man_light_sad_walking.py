
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 points
initial_positions = np.array([
    [0, 10],  # Head
    [-2, 8],  # Left Shoulder
    [2, 8],  # Right Shoulder
    [-4, 6],  # Left Elbow
    [4, 6],  # Right Elbow
    [-6, 4],  # Left Wrist
    [6, 4],  # Right Wrist
    [0, 6],  # Torso Top
    [0, 2],  # Torso Bottom
    [-1, 0],  # Left Hip
    [1, 0],  # Right Hip
    [-3, -2], # Left Knee
    [3, -2], # Right Knee
    [-5, -4], # Left Ankle
    [5, -4]   # Right Ankle
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    plt.cla()

    # Set the background color to black
    plt.gca().set_facecolor('black')

    # Set the axis limits
    plt.xlim(-10, 10)
    plt.ylim(-6, 12)
    plt.axis('off')

    # Calculate the new positions of the points based on the frame number
    positions = initial_positions.copy()

    # Make the figure walk, moving left and right, with some vertical bob
    x_offset = np.sin(i * 0.1) * 2
    y_offset = np.cos(i * 0.05) * 0.5

    positions[:, 0] += x_offset
    positions[:, 1] += y_offset

    # Simulate arm movement during walking
    positions[3, 0] += np.sin(i * 0.2) * 1  # Left Elbow
    positions[5, 0] += np.sin(i * 0.2) * 1.5 # Left Wrist
    positions[4, 0] -= np.sin(i * 0.2) * 1  # Right Elbow
    positions[6, 0] -= np.sin(i * 0.2) * 1.5 # Right Wrist

    # Simulate leg movement during walking
    positions[11, 0] += np.sin(i * 0.2) * 0.8 # Left Knee
    positions[13, 0] += np.sin(i * 0.2) * 1.2 # Left Ankle
    positions[12, 0] -= np.sin(i * 0.2) * 0.8 # Right Knee
    positions[14, 0] -= np.sin(i * 0.2) * 1.2 # Right Ankle

    # Make it look sadder and weigh less by moving the head and torso
    positions[0, 1] -= np.abs(np.sin(i * 0.1)) * 0.5  # Head
    positions[7, 1] -= np.abs(np.sin(i * 0.1)) * 0.3 # Torso Top
    positions[8, 1] -= np.abs(np.sin(i * 0.1)) * 0.3  # Torso Bottom

    # Plot the points
    plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Save the animation as a GIF
# ani.save('walking_sadman.gif', writer='pillow', fps=20)

plt.show()
