
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point lights
num_points = 15

# Initial coordinates for the point lights (hand, waist, feet)
points = np.zeros((num_points, 2))

# Define initial positions
# Just example positions, these should be adjusted based on a waving motion
points[0]  = [0, 0.5]      # shoulder
points[1]  = [0.5, 1.0]    # hand
points[2]  = [0, 1.0]      # hand
points[3]  = [-0.5, 0.5]   # shoulder
points[4]  = [-0.5, 0.3]   # elbow
points[5]  = [0.5, 0.3]    # elbow
points[6]  = [0.15, 0.0]    # neck
points[7]  = [0.2, -0.5]  # left knee
points[8]  = [-0.2, -0.5]  # right knee
points[9]  = [0.2, -1.0]  # left foot
points[10] = [-0.2, -1.0]  # right foot
points[11] = [0.0, -1.0]   # center of mass
points[12] = [0.7, 0.1]    # hand (waving)
points[13] = [0.1, -0.2]   # hand (waving)
points[14] = [-0.1, -0.2]  # hand (waving)

# Create a scatter plot for the point lights
scattered_points = ax.scatter(points[:, 0], points[:, 1], c='white')

def update(frame):
    # Simulate waving motion
    wave_amplitude = 0.2
    wave_frequency = 16

    # Update the hand position in a waving motion
    points[1, 1] = 1.0 + wave_amplitude * np.sin(frame / wave_frequency)  # hand up-down
    points[2, 1] = 1.0 + wave_amplitude * np.sin(frame / wave_frequency + np.pi/4)  # hand up-down in sync

    # Update scatter plot
    scattered_points.set_offsets(points)
    return scattered_points,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()
