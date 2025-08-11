
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the plot limits
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Define the coordinates of the points (example: turning around motion)
    # This is a simplified example, you might need more complex functions
    # to represent the motion accurately
    angle = 2 * np.pi * (i / 100)  # Full rotation in 100 frames

    x = np.array([
        0,                  # Head
        0.2 * np.sin(angle),  # Right Shoulder
        -0.2 * np.sin(angle),  # Left Shoulder
        0.3 * np.sin(angle),  # Right Elbow
        -0.3 * np.sin(angle),  # Left Elbow
        0.4 * np.sin(angle),  # Right Hand
        -0.4 * np.sin(angle),  # Left Hand
        0,                  # Hip
        0.1 * np.sin(angle), # Right Hip
        -0.1 * np.sin(angle),  # Left Hip
        0.2 * np.sin(angle),  # Right Knee
        -0.2 * np.sin(angle),  # Left Knee
        0.3 * np.sin(angle),  # Right Foot
        -0.3 * np.sin(angle),  # Left Foot
        0
    ])

    y = np.array([
        0.9,                # Head
        0.7,                # Right Shoulder
        0.7,                # Left Shoulder
        0.5,                # Right Elbow
        0.5,                # Left Elbow
        0.3,                # Right Hand
        0.3,                # Left Hand
        0.1,                # Hip
        -0.1,                  # Right Hip
        -0.1,                 # Left Hip
        -0.3,                 # Right Knee
        -0.3,                # Left Knee
        -0.5,                # Right Foot
        -0.5,                 # Left Foot
        0.3                # Waist
    ])

    # Plot the points
    ax.plot(x, y, 'wo', markersize=8) # White circles

# Create the figure and axes
fig, ax = plt.subplots()
fig.patch.set_facecolor('black') # Setting the background color to black


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# Show the animation
plt.show()
