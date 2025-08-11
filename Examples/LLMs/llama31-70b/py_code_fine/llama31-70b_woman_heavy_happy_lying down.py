
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent a woman lying down with heavy weight
# The points are ordered to represent the head, shoulders, elbows, wrists, hips, knees, and ankles
points = np.array([
    [0.5, 0.8],  # head
    [0.4, 0.7], [0.6, 0.7],  # shoulders
    [0.3, 0.6], [0.7, 0.6],  # elbows
    [0.2, 0.5], [0.8, 0.5],  # wrists
    [0.5, 0.4],  # hips
    [0.4, 0.3], [0.6, 0.3],  # knees
    [0.3, 0.2], [0.7, 0.2],  # ankles
    [0.4, 0.1], [0.6, 0.1],  # feet
    [0.5, 0.1]  # body
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Calculate the new positions of the points based on the frame number
    # This is a simple example and does not represent realistic motion
    # For a realistic motion, you would need to use a more complex model
    new_points = points.copy()
    for i in range(len(points)):
        if i < 4:  # head and shoulders
            new_points[i, 1] = points[i, 1] + 0.01 * np.sin(frame / 10.0 + i)
        elif i < 8:  # elbows and wrists
            new_points[i, 0] = points[i, 0] + 0.02 * np.sin(frame / 10.0 + i)
            new_points[i, 1] = points[i, 1] + 0.01 * np.cos(frame / 10.0 + i)
        else:  # hips, knees, ankles, and feet
            new_points[i, 0] = points[i, 0] + 0.01 * np.sin(frame / 10.0 + i)
            new_points[i, 1] = points[i, 1] + 0.02 * np.cos(frame / 10.0 + i)

    # Plot the new positions of the points
    ax.scatter(new_points[:, 0], new_points[:, 1], color='white', s=5)

# Create the figure and axis
fig, ax = plt.subplots(facecolor='black')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
