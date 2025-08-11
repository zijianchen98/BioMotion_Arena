
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
lights = np.array([
    [-0.5, -0.5],  # left shoulder
    [0.5, -0.5],   # right shoulder
    [-0.5, 0.5],   # left hip
    [0.5, 0.5],    # right hip
    [-0.7, -0.2],  # left elbow
    [0.7, -0.2],   # right elbow
    [-0.7, 0.2],   # left knee
    [0.7, 0.2],    # right knee
    [-0.9, -0.1],  # left wrist
    [0.9, -0.1],   # right wrist
    [-0.9, 0.1],   # left ankle
    [0.9, 0.1],    # right ankle
    [-0.1, -0.5],  # head
    [-0.3, 0.8],   # left hand
    [0.3, 0.8]     # right hand
])

# Define the animation function
def animate(frame):
    global lights
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the positions of the point-lights based on the frame number
    updated_lights = np.copy(lights)
    updated_lights[0, 1] = -0.5 + 0.1 * np.sin(frame / 10.0)  # left shoulder
    updated_lights[1, 1] = -0.5 + 0.1 * np.sin(frame / 10.0)  # right shoulder
    updated_lights[2, 1] = 0.5 - 0.1 * np.sin(frame / 10.0)   # left hip
    updated_lights[3, 1] = 0.5 - 0.1 * np.sin(frame / 10.0)   # right hip
    updated_lights[4, 1] = -0.2 + 0.2 * np.sin(frame / 10.0)  # left elbow
    updated_lights[5, 1] = -0.2 + 0.2 * np.sin(frame / 10.0)  # right elbow
    updated_lights[6, 1] = 0.2 - 0.2 * np.sin(frame / 10.0)   # left knee
    updated_lights[7, 1] = 0.2 - 0.2 * np.sin(frame / 10.0)   # right knee
    updated_lights[8, 1] = -0.1 + 0.3 * np.sin(frame / 10.0)  # left wrist
    updated_lights[9, 1] = -0.1 + 0.3 * np.sin(frame / 10.0)  # right wrist
    updated_lights[10, 1] = 0.1 - 0.3 * np.sin(frame / 10.0)  # left ankle
    updated_lights[11, 1] = 0.1 - 0.3 * np.sin(frame / 10.0)  # right ankle
    updated_lights[12, 1] = -0.5 + 0.1 * np.sin(frame / 10.0)  # head
    updated_lights[13, 1] = 0.8 - 0.1 * np.sin(frame / 10.0)  # left hand
    updated_lights[14, 1] = 0.8 - 0.1 * np.sin(frame / 10.0)  # right hand

    ax.scatter(updated_lights[:, 0], updated_lights[:, 1], color='white')

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)
plt.show()
