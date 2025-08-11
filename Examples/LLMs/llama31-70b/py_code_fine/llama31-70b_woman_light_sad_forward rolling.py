
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
lights = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.4],  # left elbow
    [0.6, 0.4],  # right elbow
    [0.4, 0.2],  # left hand
    [0.6, 0.2],  # right hand
    [0.5, 0.8],  # neck
    [0.5, 0.9],  # top of head
    [0.3, 0.5],  # left hip
    [0.7, 0.5],  # right hip
    [0.3, 0.3],  # left knee
    [0.7, 0.3],  # right knee
    [0.3, 0.1],  # left ankle
    [0.7, 0.1]   # right ankle
])

# Define the movement of each point-light
def move_lights(frame):
    # Calculate the rotation angle based on the frame number
    angle = np.radians(frame * 5)

    # Move the point-lights to simulate the rolling motion
    moved_lights = lights.copy()
    moved_lights[:, 0] = moved_lights[:, 0] + np.sin(angle) * 0.1
    moved_lights[:, 1] = moved_lights[:, 1] + np.cos(angle) * 0.1

    # Simulate the forward rolling motion
    moved_lights[0, 1] = moved_lights[0, 1] + np.sin(angle) * 0.05
    moved_lights[1, 1] = moved_lights[1, 1] + np.sin(angle) * 0.03
    moved_lights[2, 1] = moved_lights[2, 1] + np.sin(angle) * 0.03
    moved_lights[3, 1] = moved_lights[3, 1] + np.sin(angle) * 0.02
    moved_lights[4, 1] = moved_lights[4, 1] + np.sin(angle) * 0.02
    moved_lights[5, 1] = moved_lights[5, 1] + np.sin(angle) * 0.01
    moved_lights[6, 1] = moved_lights[6, 1] + np.sin(angle) * 0.01
    moved_lights[7, 1] = moved_lights[7, 1] + np.sin(angle) * 0.01
    moved_lights[8, 1] = moved_lights[8, 1] + np.sin(angle) * 0.01
    moved_lights[9, 1] = moved_lights[9, 1] + np.sin(angle) * 0.01
    moved_lights[10, 1] = moved_lights[10, 1] + np.sin(angle) * 0.01
    moved_lights[11, 1] = moved_lights[11, 1] + np.sin(angle) * 0.01
    moved_lights[12, 1] = moved_lights[12, 1] + np.sin(angle) * 0.01
    moved_lights[13, 1] = moved_lights[13, 1] + np.sin(angle) * 0.01
    moved_lights[14, 1] = moved_lights[14, 1] + np.sin(angle) * 0.01

    return moved_lights

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the initial position of the point-lights
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_axis_off()
scatter = ax.scatter(lights[:, 0], lights[:, 1], s=10, c='white')

# Animation function
def animate(frame):
    moved_lights = move_lights(frame)
    scatter.set_offsets(moved_lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
