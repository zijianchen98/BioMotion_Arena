
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the running man
points = np.array([
    [0, 0],  # head
    [-0.1, 0.2],  # left shoulder
    [0.1, 0.2],  # right shoulder
    [-0.2, 0.1],  # left elbow
    [0.2, 0.1],  # right elbow
    [-0.3, 0],  # left hand
    [0.3, 0],  # right hand
    [0, -0.2],  # left hip
    [0, -0.2],  # right hip
    [-0.1, -0.4],  # left knee
    [0.1, -0.4],  # right knee
    [-0.2, -0.6],  # left ankle
    [0.2, -0.6],  # right ankle
    [-0.1, -0.8],  # left foot
    [0.1, -0.8],  # right foot
])

# Define the movement of each point
def animate(frame):
    global points
    new_points = np.copy(points)

    # Head movement
    new_points[0, 1] = 0.05 * np.sin(frame / 10)

    # Shoulder movement
    new_points[1, 1] = 0.2 + 0.05 * np.sin(frame / 10)
    new_points[2, 1] = 0.2 + 0.05 * np.cos(frame / 10)

    # Elbow movement
    new_points[3, 1] = 0.1 + 0.1 * np.sin(frame / 10)
    new_points[4, 1] = 0.1 + 0.1 * np.cos(frame / 10)

    # Hand movement
    new_points[5, 1] = 0 + 0.2 * np.sin(frame / 10)
    new_points[6, 1] = 0 + 0.2 * np.cos(frame / 10)

    # Hip movement
    new_points[7, 1] = -0.2 + 0.05 * np.sin(frame / 10)
    new_points[8, 1] = -0.2 + 0.05 * np.cos(frame / 10)

    # Knee movement
    new_points[9, 1] = -0.4 + 0.1 * np.sin(frame / 10)
    new_points[10, 1] = -0.4 + 0.1 * np.cos(frame / 10)

    # Ankle movement
    new_points[11, 1] = -0.6 + 0.2 * np.sin(frame / 10)
    new_points[12, 1] = -0.6 + 0.2 * np.cos(frame / 10)

    # Foot movement
    new_points[13, 1] = -0.8 + 0.1 * np.sin(frame / 10)
    new_points[14, 1] = -0.8 + 0.1 * np.cos(frame / 10)

    # Update the points
    points = new_points

    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Plot the new points
    ax.scatter(points[:, 0], points[:, 1], color='white', s=5)

    # Set the limits of the plot
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # Hide the axis
    ax.axis('off')

# Create a new figure
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

# Show the animation
plt.show()
