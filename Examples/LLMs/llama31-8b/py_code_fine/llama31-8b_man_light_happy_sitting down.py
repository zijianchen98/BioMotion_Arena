
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the action parameters
num_lights = 15
num_frames = 100
fps = 30
duration = num_frames / fps

# Define the 3D coordinates of the point-lights
lights = np.zeros((num_lights, num_frames, 3))

# Sitting down motion parameters
# Based on the study by Troje (2002) on the biomechanics of human sitting
# The motion is a combination of rotation around the x and y axes
theta_x = np.linspace(0, np.pi/2, num_frames)
theta_y = np.linspace(0, np.pi/2, num_frames)

# Define the 3D coordinates of the point-lights
for i in range(num_lights):
    # Hip joint location
    hip_x = 0.2 * np.sin(theta_x)
    hip_y = 0.2 * np.cos(theta_y)
    hip_z = 0.5

    # Knee joint location
    knee_x = 0.1 * np.sin(theta_x)
    knee_y = 0.1 * np.cos(theta_y)
    knee_z = 0.3

    # Ankle joint location
    ankle_x = 0.05 * np.sin(theta_x)
    ankle_y = 0.05 * np.cos(theta_y)
    ankle_z = 0.4

    # Light locations
    lights[i, :, 0] = hip_x + 0.1 * np.sin(theta_x + i * np.pi / 6)
    lights[i, :, 1] = hip_y + 0.1 * np.cos(theta_y + i * np.pi / 6)
    lights[i, :, 2] = hip_z + 0.2 * np.sin(theta_x + i * np.pi / 6)

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 1)
ax.set_axis_off()

# Animate the plot
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 1)
    ax.set_axis_off()
    for i in range(num_lights):
        ax.plot(lights[i, frame, 0], lights[i, frame, 1], lights[i, frame, 2], 'o', markersize=5, color='white')

ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/fps)

plt.show()
