
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the point light source
def create_point_light(x, y, z, intensity):
    return np.array([x, y, z, intensity])

# Define the camera position and orientation
camera_position = np.array([0, 0, 2])
camera_rotation = np.array([0, 0, 0])

# Define the subject's pose
subject_pose = np.array([0, 0, 0])

# Define the action's pose
action_pose = np.array([1, 0, 0])  # x-axis represents forward motion, y-axis represents weight

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the point lights
point_lights = [
    create_point_light(0, 0, 2, 1),  # Front point light
    create_point_light(2, 0, 2, 1),  # Right point light
    create_point_light(2, 2, 2, 1),  # Back point light
    create_point_light(0, 2, 2, 1)   # Left point light
]

# Define the camera's position and orientation
camera = np.eye(4)
camera[:3, 3] = 2  # Set the z-coordinate to 2 to match the subject's height

# Define the action's pose
action_pose = np.array([0, 0, 0])  # x-axis represents weight, y-axis represents forward motion

# Define the time step and total time
dt = 0.01
t_max = 10

# Define the animation function
def animate(i):
    global subject_pose, action_pose, point_lights, camera

    # Update the camera's position
    camera[:3, 3] = subject_pose + action_pose

    # Update the point lights' positions
    for light in point_lights:
        light[:3, 3] = camera[:3, 3]

    # Update the subject's pose
    subject_pose += np.array([0, 1, 0]) * dt

    # Update the action's pose
    action_pose += np.array([0, 0, 0]) * dt

    # Check for the end of the animation
    if i > t_max:
        return False

    return True

# Animate the subject's motion
while True:
    if not animate(0):
        break

# Plot the scene
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_title("Biological Motion: Jumping Forward")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Show the plot
plt.show()
