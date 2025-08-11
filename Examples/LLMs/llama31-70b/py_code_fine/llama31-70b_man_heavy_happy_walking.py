
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happyman with heavy weight
point_lights = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.4],  # left elbow
    [0.6, 0.4],  # right elbow
    [0.4, 0.3],  # left hand
    [0.6, 0.3],  # right hand
    [0.5, 0.8],  # torso top
    [0.5, 0.7],  # torso middle
    [0.5, 0.6],  # torso bottom
    [0.4, 0.2],  # left hip
    [0.6, 0.2],  # right hip
    [0.4, 0.1],  # left knee
    [0.6, 0.1],  # right knee
    [0.4, 0.0],  # left ankle
    [0.6, 0.0]   # right ankle
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update point-light locations based on the walking motion
    updated_point_lights = point_lights.copy()
    for i, point in enumerate(updated_point_lights):
        if i == 0:  # head
            updated_point_lights[i] = [point[0], point[1] + 0.01 * np.sin(frame / 10.0)]
        elif i == 1 or i == 2:  # shoulders
            updated_point_lights[i] = [point[0], point[1] + 0.01 * np.sin(frame / 10.0 + np.pi / 2 * (i - 1))]
        elif i == 3 or i == 4:  # elbows
            updated_point_lights[i] = [point[0], point[1] + 0.02 * np.sin(frame / 10.0 + np.pi / 2 * (i - 3))]
        elif i == 5 or i == 6:  # hands
            updated_point_lights[i] = [point[0], point[1] + 0.03 * np.sin(frame / 10.0 + np.pi / 2 * (i - 5))]
        elif i == 7 or i == 8 or i == 9:  # torso
            updated_point_lights[i] = [point[0], point[1] + 0.005 * np.sin(frame / 10.0 + np.pi / 3 * (i - 7))]
        elif i == 10 or i == 11:  # hips
            updated_point_lights[i] = [point[0], point[1] + 0.01 * np.sin(frame / 10.0 + np.pi / 2 * (i - 10))]
        elif i == 12 or i == 13:  # knees
            updated_point_lights[i] = [point[0], point[1] + 0.02 * np.sin(frame / 10.0 + np.pi / 2 * (i - 12))]
        elif i == 14 or i == 15:  # ankles
            updated_point_lights[i] = [point[0], point[1] + 0.03 * np.sin(frame / 10.0 + np.pi / 2 * (i - 14))]

    # Plot the updated point-lights
    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], s=50, c='white')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

# Show the animation
plt.show()
