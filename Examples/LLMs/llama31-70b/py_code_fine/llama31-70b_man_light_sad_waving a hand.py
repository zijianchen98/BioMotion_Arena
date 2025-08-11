
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
def initialize_points():
    points = np.zeros((15, 2))
    # Head
    points[0] = np.array([0, 10])
    # Torso
    points[1] = np.array([0, 5])
    points[2] = np.array([-2, 7])
    points[3] = np.array([2, 7])
    # Right arm
    points[4] = np.array([3, 5])
    points[5] = np.array([5, 3])
    points[6] = np.array([7, 1])
    # Left arm (waving)
    points[7] = np.array([-3, 5])
    points[8] = np.array([-5, 3])
    points[9] = np.array([-7, 1])
    # Right leg
    points[10] = np.array([1, 0])
    points[11] = np.array([2, -2])
    points[12] = np.array([3, -4])
    # Left leg
    points[13] = np.array([-1, 0])
    points[14] = np.array([-2, -2])
    return points

# Define the animation function
def animate(frame):
    global points
    # Move the waving arm
    angle = np.radians(frame)
    points[8] = np.array([-5 + np.cos(angle), 3 + np.sin(angle)])
    points[9] = np.array([-7 + np.cos(angle), 1 + np.sin(angle)])
    # Update the plot
    plt.clf()
    plt.axis('equal')
    plt.axis('off')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.scatter(points[:, 0], points[:, 1], color='white', s=50)
    plt.gca().set_facecolor('black')

# Initialize the points
points = initialize_points()

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), animate, frames=range(360), interval=50)

plt.show()
