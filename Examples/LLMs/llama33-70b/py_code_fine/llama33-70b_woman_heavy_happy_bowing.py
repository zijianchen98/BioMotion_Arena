
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
# These points represent the major joints of the human body
point_lights = np.array([
    [0, 0.5],  # head
    [-0.2, 0.4],  # left shoulder
    [0.2, 0.4],  # right shoulder
    [-0.3, 0.2],  # left elbow
    [0.3, 0.2],  # right elbow
    [-0.4, 0.1],  # left wrist
    [0.4, 0.1],  # right wrist
    [0, 0.3],  # torso
    [-0.2, 0.1],  # left hip
    [0.2, 0.1],  # right hip
    [-0.3, 0],  # left knee
    [0.3, 0],  # right knee
    [-0.4, -0.1],  # left ankle
    [0.4, -0.1],  # right ankle
    [0, -0.2]  # feet
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    # Calculate the new positions of the point-lights based on the bowing action
    # The movement should be smooth and natural
    new_point_lights = np.copy(point_lights)
    new_point_lights[0, 1] = 0.5 - 0.2 * np.sin(np.radians(frame))  # head
    new_point_lights[1, 1] = 0.4 - 0.1 * np.sin(np.radians(frame))  # left shoulder
    new_point_lights[2, 1] = 0.4 - 0.1 * np.sin(np.radians(frame))  # right shoulder
    new_point_lights[3, 1] = 0.2 - 0.1 * np.sin(np.radians(frame))  # left elbow
    new_point_lights[4, 1] = 0.2 - 0.1 * np.sin(np.radians(frame))  # right elbow
    new_point_lights[5, 1] = 0.1 - 0.1 * np.sin(np.radians(frame))  # left wrist
    new_point_lights[6, 1] = 0.1 - 0.1 * np.sin(np.radians(frame))  # right wrist
    new_point_lights[7, 1] = 0.3 - 0.1 * np.sin(np.radians(frame))  # torso
    new_point_lights[8, 1] = 0.1 - 0.1 * np.sin(np.radians(frame))  # left hip
    new_point_lights[9, 1] = 0.1 - 0.1 * np.sin(np.radians(frame))  # right hip
    new_point_lights[10, 1] = 0 - 0.1 * np.sin(np.radians(frame))  # left knee
    new_point_lights[11, 1] = 0 - 0.1 * np.sin(np.radians(frame))  # right knee
    new_point_lights[12, 1] = -0.1 - 0.1 * np.sin(np.radians(frame))  # left ankle
    new_point_lights[13, 1] = -0.1 - 0.1 * np.sin(np.radians(frame))  # right ankle
    new_point_lights[14, 1] = -0.2 - 0.1 * np.sin(np.radians(frame))  # feet
    
    # Plot the new positions of the point-lights
    ax.scatter(new_point_lights[:, 0], new_point_lights[:, 1], c='white', s=10)

# Create a new figure
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(0, 360), interval=50)

plt.show()
