
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# Each row represents a point-light, with the first column being the x-coordinate and the second column being the y-coordinate
initial_positions = np.array([
    [-0.3, -0.2],  # left shoulder
    [0.3, -0.2],   # right shoulder
    [-0.2, 0.1],   # left elbow
    [0.2, 0.1],    # right elbow
    [-0.1, 0.3],   # left wrist
    [0.1, 0.3],    # right wrist
    [-0.2, -0.3],  # left hip
    [0.2, -0.3],   # right hip
    [-0.1, -0.5],  # left knee
    [0.1, -0.5],   # right knee
    [-0.1, -0.7],  # left ankle
    [0.1, -0.7],   # right ankle
    [0, 0.5],      # head
    [-0.1, 0.2],   # left hand
    [0.1, 0.2]     # right hand
])

# Define the movement of each point-light over time
# Each row represents a time step, with each column representing the x and y coordinates of a point-light
movement = np.zeros((100, 15, 2))  # 100 time steps, 15 point-lights, 2 coordinates

for i in range(100):
    angle = i / 100 * np.pi * 2  # angle of rotation
    weight_angle = i / 100 * np.pi  # angle of weight movement

    # Sad woman with heavy weight turning around
    for j, pos in enumerate(initial_positions):
        if j < 6:  # upper body
            movement[i, j, 0] = pos[0] * np.cos(angle) - pos[1] * np.sin(angle)
            movement[i, j, 1] = pos[0] * np.sin(angle) + pos[1] * np.cos(angle)
        elif j < 10:  # lower body
            movement[i, j, 0] = pos[0] * np.cos(angle) - pos[1] * np.sin(angle)
            movement[i, j, 1] = pos[0] * np.sin(angle) + pos[1] * np.cos(angle) - 0.1 * np.sin(weight_angle)
        elif j < 12:  # feet
            movement[i, j, 0] = pos[0] * np.cos(angle) - pos[1] * np.sin(angle)
            movement[i, j, 1] = pos[0] * np.sin(angle) + pos[1] * np.cos(angle) - 0.2 * np.sin(weight_angle)
        elif j < 14:  # hands
            movement[i, j, 0] = pos[0] * np.cos(angle) - pos[1] * np.sin(angle)
            movement[i, j, 1] = pos[0] * np.sin(angle) + pos[1] * np.cos(angle) + 0.1 * np.sin(weight_angle)
        else:  # head
            movement[i, j, 0] = pos[0] * np.cos(angle) - pos[1] * np.sin(angle)
            movement[i, j, 1] = pos[0] * np.sin(angle) + pos[1] * np.cos(angle)

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

point_lights = ax.scatter(movement[0, :, 0], movement[0, :, 1], color='white')

def animate(i):
    point_lights.set_offsets(movement[i, :, :])
    return point_lights,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
