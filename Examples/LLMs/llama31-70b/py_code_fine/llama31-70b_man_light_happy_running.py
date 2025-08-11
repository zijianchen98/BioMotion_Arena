
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happy man
point_lights = np.array([
    [0.5, 0.9],  # head
    [0.4, 0.8],  # left shoulder
    [0.6, 0.8],  # right shoulder
    [0.4, 0.7],  # left elbow
    [0.6, 0.7],  # right elbow
    [0.4, 0.6],  # left hand
    [0.6, 0.6],  # right hand
    [0.5, 0.5],  # torso
    [0.4, 0.4],  # left hip
    [0.6, 0.4],  # right hip
    [0.4, 0.3],  # left knee
    [0.6, 0.3],  # right knee
    [0.4, 0.2],  # left ankle
    [0.6, 0.2],  # right ankle
    [0.5, 0.1],  # feet
])

# Define the movement of the point-lights
def move_point_lights(frame):
    # Calculate the movement of each point-light based on the frame number
    movement = np.zeros((15, 2))
    movement[0] = [0.05 * np.sin(frame * 0.1), 0]  # head
    movement[1] = [-0.05 * np.sin(frame * 0.1), 0.05 * np.sin(frame * 0.05)]  # left shoulder
    movement[2] = [0.05 * np.sin(frame * 0.1), -0.05 * np.sin(frame * 0.05)]  # right shoulder
    movement[3] = [-0.1 * np.sin(frame * 0.1), 0.1 * np.sin(frame * 0.05)]  # left elbow
    movement[4] = [0.1 * np.sin(frame * 0.1), -0.1 * np.sin(frame * 0.05)]  # right elbow
    movement[5] = [-0.15 * np.sin(frame * 0.1), 0.15 * np.sin(frame * 0.05)]  # left hand
    movement[6] = [0.15 * np.sin(frame * 0.1), -0.15 * np.sin(frame * 0.05)]  # right hand
    movement[7] = [0, 0.05 * np.sin(frame * 0.05)]  # torso
    movement[8] = [-0.05 * np.sin(frame * 0.1), 0.05 * np.sin(frame * 0.05)]  # left hip
    movement[9] = [0.05 * np.sin(frame * 0.1), -0.05 * np.sin(frame * 0.05)]  # right hip
    movement[10] = [-0.1 * np.sin(frame * 0.1), 0.1 * np.sin(frame * 0.05)]  # left knee
    movement[11] = [0.1 * np.sin(frame * 0.1), -0.1 * np.sin(frame * 0.05)]  # right knee
    movement[12] = [-0.15 * np.sin(frame * 0.1), 0.15 * np.sin(frame * 0.05)]  # left ankle
    movement[13] = [0.15 * np.sin(frame * 0.1), -0.15 * np.sin(frame * 0.05)]  # right ankle
    movement[14] = [0, 0.05 * np.sin(frame * 0.05)]  # feet

    return point_lights + movement

# Create a new figure
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_axis_off()

# Initialize the plot with the initial point-lights
points = ax.scatter(point_lights[:, 0], point_lights[:, 1], c='w', s=10)

# Animation function
def animate(frame):
    points.set_offsets(move_point_lights(frame))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
