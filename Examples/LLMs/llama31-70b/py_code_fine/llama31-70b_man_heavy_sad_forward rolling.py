
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
point_lights = np.array([
    [0, 0],  # head
    [-0.2, 0.3], [0.2, 0.3],  # shoulders
    [-0.4, 0.1], [0.4, 0.1],  # elbows
    [-0.6, -0.1], [0.6, -0.1],  # hands
    [0, -0.4],  # torso
    [-0.2, -0.6], [0.2, -0.6],  # hips
    [-0.4, -0.8], [0.4, -0.8],  # knees
    [-0.6, -1.0], [0.6, -1.0],  # feet
    [0, -1.2],  # weight
])

# Define the animation function
def animate(i):
    global point_lights
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1.5, 0.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the point-lights positions
    for j, point_light in enumerate(point_lights):
        if j == 0:  # head
            point_lights[j] = [point_light[0], point_light[1] + 0.01 * np.sin(i / 10.0)]
        elif j < 4:  # shoulders and elbows
            point_lights[j] = [point_light[0] + 0.01 * np.cos(i / 10.0 + j), point_light[1] + 0.01 * np.sin(i / 10.0 + j)]
        elif j < 8:  # hands
            point_lights[j] = [point_light[0] + 0.02 * np.cos(i / 10.0 + j), point_light[1] + 0.02 * np.sin(i / 10.0 + j)]
        elif j == 8:  # torso
            point_lights[j] = [point_light[0], point_light[1] + 0.01 * np.sin(i / 10.0)]
        elif j < 12:  # hips and knees
            point_lights[j] = [point_light[0] + 0.01 * np.cos(i / 10.0 + j), point_light[1] + 0.01 * np.sin(i / 10.0 + j)]
        elif j < 14:  # feet
            point_lights[j] = [point_light[0] + 0.02 * np.cos(i / 10.0 + j), point_light[1] + 0.02 * np.sin(i / 10.0 + j)]
        else:  # weight
            point_lights[j] = [point_light[0], point_light[1] + 0.01 * np.sin(i / 10.0)]

    # Draw the point-lights
    ax.scatter(point_lights[:, 0], point_lights[:, 1], s=10, c='white')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
