
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the point-light stimulus parameters
num_lights = 15
light_radius = 0.1
light_color = 'white'
background_color = 'black'

# Define the action parameters (walking)
num_frames = 100
frame_rate = 30  # frames per second
duration = num_frames / frame_rate  # seconds

# Define the 3D coordinates of the point-lights
lights_x = np.zeros((num_lights, num_frames))
lights_y = np.zeros((num_lights, num_frames))
lights_z = np.zeros((num_lights, num_frames))

# Define the walking motion parameters
hip_angle = np.linspace(0, 2 * np.pi, num_frames)
knee_angle = np.linspace(0, 2 * np.pi, num_frames)
ankle_angle = np.linspace(0, 2 * np.pi, num_frames)

# Define the 3D coordinates of the point-lights for each frame
for i in range(num_frames):
    lights_x[0, i] = 0.5  # hip
    lights_y[0, i] = 0.2 * np.sin(hip_angle[i])
    lights_z[0, i] = 0.2 * np.cos(hip_angle[i])

    lights_x[1, i] = 0.3  # knee
    lights_y[1, i] = 0.2 * np.sin(knee_angle[i])
    lights_z[1, i] = 0.2 * np.cos(knee_angle[i])

    lights_x[2, i] = 0.1  # ankle
    lights_y[2, i] = 0.2 * np.sin(ankle_angle[i])
    lights_z[2, i] = 0.2 * np.cos(ankle_angle[i])

    lights_x[3, i] = 0.7  # shoulder
    lights_y[3, i] = 0.2 * np.sin(hip_angle[i])
    lights_z[3, i] = 0.2 * np.cos(hip_angle[i])

    lights_x[4, i] = 0.5  # elbow
    lights_y[4, i] = 0.2 * np.sin(knee_angle[i])
    lights_z[4, i] = 0.2 * np.cos(knee_angle[i])

    lights_x[5, i] = 0.3  # wrist
    lights_y[5, i] = 0.2 * np.sin(ankle_angle[i])
    lights_z[5, i] = 0.2 * np.cos(ankle_angle[i])

    lights_x[6, i] = 0.9  # head
    lights_y[6, i] = 0.2 * np.sin(hip_angle[i])
    lights_z[6, i] = 0.2 * np.cos(hip_angle[i])

    lights_x[7, i] = 0.7  # eye
    lights_y[7, i] = 0.2 * np.sin(knee_angle[i])
    lights_z[7, i] = 0.2 * np.cos(knee_angle[i])

    lights_x[8, i] = 0.5  # nose
    lights_y[8, i] = 0.2 * np.sin(ankle_angle[i])
    lights_z[8, i] = 0.2 * np.cos(ankle_angle[i])

    lights_x[9, i] = 0.3  # mouth
    lights_y[9, i] = 0.2 * np.sin(hip_angle[i])
    lights_z[9, i] = 0.2 * np.cos(hip_angle[i])

    lights_x[10, i] = 0.1  # toe
    lights_y[10, i] = 0.2 * np.sin(knee_angle[i])
    lights_z[10, i] = 0.2 * np.cos(knee_angle[i])

    lights_x[11, i] = 0.7  # heel
    lights_y[11, i] = 0.2 * np.sin(ankle_angle[i])
    lights_z[11, i] = 0.2 * np.cos(ankle_angle[i])

    lights_x[12, i] = 0.5  # hip2
    lights_y[12, i] = 0.2 * np.sin(hip_angle[i])
    lights_z[12, i] = 0.2 * np.cos(hip_angle[i])

    lights_x[13, i] = 0.3  # knee2
    lights_y[13, i] = 0.2 * np.sin(knee_angle[i])
    lights_z[13, i] = 0.2 * np.cos(knee_angle[i])

    lights_x[14, i] = 0.1  # ankle2
    lights_y[14, i] = 0.2 * np.sin(ankle_angle[i])
    lights_z[14, i] = 0.2 * np.cos(ankle_angle[i])

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# Function to update the plot for each frame
def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    for i in range(num_lights):
        ax.scatter(lights_x[i, frame], lights_y[i, frame], lights_z[i, frame], s=light_radius*100, c=light_color)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 / frame_rate)

# Show the animation
plt.show()
