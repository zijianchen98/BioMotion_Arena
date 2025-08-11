
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial coordinates of the 15 point-lights
initial_coordinates = np.array([
    [0, 3],  # Head
    [-0.5, 2.5],  # Left Shoulder
    [0.5, 2.5],  # Right Shoulder
    [-1, 2],  # Left Elbow
    [1, 2],  # Right Elbow
    [-1.5, 1.5],  # Left Wrist
    [1.5, 1.5],  # Right Wrist
    [-0.2, 2],  # Spine Top
    [0.2, 2],  # Spine Top
    [-0.2, 1],  # Spine Bottom
    [0.2, 1],  # Spine Bottom
    [-0.5, 0],  # Left Hip
    [0.5, 0],  # Right Hip
    [-0.2, -0.5],  # Left Knee
    [0.2, -0.5],  # Right Knee
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the plot limits
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 4])

    # Set the background color to black
    ax.set_facecolor('black')

    # Remove the axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Define the walking motion
    x_offset = np.sin(i / 10) * 0.5
    y_offset = np.cos(i / 10) * 0.2

    # Update the coordinates of the point-lights
    coordinates = initial_coordinates.copy()

    # Make the woman walk
    coordinates[:, 0] += x_offset

    # Move legs
    coordinates[13, 1] += np.sin(i / 5) * 0.3  # Left Knee
    coordinates[14, 1] -= np.sin(i / 5) * 0.3  # Right Knee

    coordinates[11, 1] += np.sin(i / 5) * 0.2  # Left Hip
    coordinates[12, 1] -= np.sin(i / 5) * 0.2  # Right Hip

    # Move arms
    coordinates[3, 1] += np.cos(i / 5) * 0.2  # Left Elbow
    coordinates[4, 1] -= np.cos(i / 5) * 0.2  # Right Elbow

    coordinates[5, 1] += np.cos(i / 5) * 0.3  # Left Wrist
    coordinates[6, 1] -= np.cos(i / 5) * 0.3  # Right Wrist

    # Move body
    coordinates[0, 1] += y_offset * 0.1

    # Plot the point-lights
    ax.plot(coordinates[:, 0], coordinates[:, 1], 'wo', markersize=8)

    # Return the updated plot
    return ax.plot([], [], 'wo', markersize=8)

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
