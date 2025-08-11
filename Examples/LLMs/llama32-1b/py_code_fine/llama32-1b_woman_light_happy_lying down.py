
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the subject's pose
subject_pose = np.array([
    [0, 0, 0, 1],  # x, y, z, w (eye position in world space)
    [1, 0, 0, 0],  # x, y, z, w (x, y, z, eye position in world space)
    [0, 1, 0, 0],  # x, y, z, w (x, y, z, eye position in world space)
    [0, 0, 1, 0]   # x, y, z, w (x, y, z, eye position in world space)
])

# Define the action's pose
action_pose = np.array([
    [0, 0, 0, 1],  # x, y, z, w (eye position in world space)
    [0, 0, 0, 0],  # x, y, z, w (x, y, z, eye position in world space)
    [0, 1, 0, 0],  # x, y, z, w (x, y, z, eye position in world space)
    [0, 0, 1, 0]   # x, y, z, w (x, y, z, eye position in world space)
])

# Define the point-light stimulus
class PointLight:
    def __init__(self, x, y, z, intensity):
        self.x = x
        self.y = y
        self.z = z
        self.intensity = intensity

    def update(self, t):
        self.x = t * 10
        self.y = t * 10
        self.z = t * 10

# Create the point-light stimulus
point_light = PointLight(0, 0, 0, 1)

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the function to update the point-light stimulus
def update(frame):
    point_light.update(frame)
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.scatter(*subject_pose[:3], c='r', s=50)
    ax.scatter(*action_pose[:3], c='g', s=50)
    ax.plot3D(*zip(subject_pose[3:], action_pose[3:]), c='b', lw=2)
    ax.plot3D(*zip(subject_pose[:3], subject_pose[3:]), c='r', lw=2)
    ax.plot3D(*zip(action_pose[:3], action_pose[3:]), c='g', lw=2)
    plt.draw()
    plt.pause(0.01)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=10)

plt.show()
