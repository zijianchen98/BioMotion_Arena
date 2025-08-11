
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)

# Define the subject's hand
hand_length = 100
hand_width = 20
hand_angle = np.radians(30)  # degrees

# Define the action's movement
def movement(t):
    # Calculate the x and y coordinates of the hand
    x = 100 + 20 * np.cos(t)
    y = 100 + 20 * np.sin(t)

    # Calculate the hand's position and rotation
    hand_x = x * np.cos(hand_angle) - y * np.sin(hand_angle)
    hand_y = x * np.sin(hand_angle) + y * np.cos(hand_angle)

    return hand_x, hand_y, hand_angle

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the points and velocities
points = []
velocities = []

# Generate the movement
t = np.linspace(0, 2 * np.pi, 1000)
for i in range(1000):
    # Calculate the hand's position and rotation
    hand_x, hand_y, hand_angle = movement(t[i])

    # Calculate the points and velocities
    point_x = hand_x
    point_y = hand_y
    point_z = 0

    velocity_x = 0
    velocity_y = 0
    velocity_z = 0

    # Append the points and velocities to the lists
    points.append([point_x, point_y, point_z])
    velocities.append([velocity_x, velocity_y, velocity_z])

# Plot the points and velocities
for i in range(len(points)):
    ax.plot3D(points[i][0], points[i][1], points[i][2], c='w')
    ax.quiver(points[i][0], points[i][1], points[i][2], velocities[i][0], velocities[i][1], velocities[i][2], color='w')

# Set the axis limits and labels
ax.set_xlim(-WIDTH/2, WIDTH/2)
ax.set_ylim(-HEIGHT/2, HEIGHT/2)
ax.set_zlim(-HEIGHT/2, HEIGHT/2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
