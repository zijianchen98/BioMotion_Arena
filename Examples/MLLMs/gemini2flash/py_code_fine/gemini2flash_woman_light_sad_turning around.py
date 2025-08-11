
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation and the frame rate
num_frames = 200
fps = 30

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 3],    # Head
    [-0.5, 2.5], # Left Shoulder
    [0.5, 2.5],  # Right Shoulder
    [-1, 2],   # Left Elbow
    [1, 2],    # Right Elbow
    [-1.5, 1.5], # Left Hand
    [1.5, 1.5],  # Right Hand
    [-0.2, 2],  # Torso 1
    [0.2, 2],   # Torso 2
    [0, 1.5],    # Waist
    [-0.3, 0.5], # Left Hip
    [0.3, 0.5],  # Right Hip
    [-0.7, 0],   # Left Knee
    [0.7, 0],    # Right Knee
    [0, -0.5]   # Foot

])

# Define the animation function
def animate(i):
    # Clear the current frame
    plt.cla()

    # Define the rotation angle for the current frame
    angle = np.sin(i / num_frames * 2 * np.pi) * 10 # Adjust amplitude for smaller turn

    # Create a rotation matrix
    rotation_matrix = np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
                                [np.sin(np.radians(angle)), np.cos(np.radians(angle))]])

    # Apply the rotation to the initial positions
    rotated_positions = np.dot(initial_positions, rotation_matrix)

    # Plot the point-lights
    plt.plot(rotated_positions[:, 0], rotated_positions[:, 1], 'wo', markersize=8)

    # Set the axis limits
    plt.xlim([-2, 2])
    plt.ylim([-1, 4])

    # Set the background color
    plt.gca().set_facecolor('k')

    # Remove the axis labels and ticks
    plt.xticks([])
    plt.yticks([])

    # Set the title
    plt.title('Sad Woman Turning Around', color='white')

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/fps)

# Show the animation
plt.show()
