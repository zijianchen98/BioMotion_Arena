
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=8)


# Define the animation function
def animate(i):
    # Define the coordinates of the points
    x = np.array([
        0.0,  # Head
        -0.2, # Left Shoulder
        0.2,  # Right Shoulder
        -0.4, # Left Elbow
        0.4,  # Right Elbow
        -0.6, # Left Wrist
        0.6,  # Right Wrist
        -0.1, # Left Hip
        0.1,  # Right Hip
        -0.3, # Left Knee
        0.3,  # Right Knee
        -0.5, # Left Ankle
        0.5,  # Right Ankle
        -0.05, # Spine Base
        0.05  # Spine Mid
    ])

    y = np.array([
        0.9,  # Head
        0.7,  # Left Shoulder
        0.7,  # Right Shoulder
        0.5,  # Left Elbow
        0.5,  # Right Elbow
        0.3,  # Left Wrist
        0.3,  # Right Wrist
        0.3,  # Left Hip
        0.3,  # Right Hip
        0.1,  # Left Knee
        0.1,  # Right Knee
        -0.1, # Left Ankle
        -0.1, # Right Ankle
        0.1,  # Spine Base
        0.5  # Spine Mid
    ])

    # Apply bowing motion
    bow_angle = np.sin(i * 0.1) * 0.3 # Adjust amplitude and frequency as needed
    y = y - bow_angle * y # shift y values according to angle
    y = y - 0.1 * bow_angle  # additional downward shift to center the bowing

    # Update the points
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True, repeat=True)

# Show the animation
plt.show()
