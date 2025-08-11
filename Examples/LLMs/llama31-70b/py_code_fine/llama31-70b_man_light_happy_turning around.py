
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# Each row represents a point-light, with the first column being the x-coordinate and the second column being the y-coordinate
lights = np.array([
    [-0.5, -0.5],  # left foot
    [0.5, -0.5],   # right foot
    [-0.25, -0.25],# left knee
    [0.25, -0.25], # right knee
    [-0.5, 0.25],  # left hip
    [0.5, 0.25],   # right hip
    [0, 0.5],      # center of mass
    [-0.25, 0.75], # left shoulder
    [0.25, 0.75],  # right shoulder
    [-0.5, 1.0],   # left elbow
    [0.5, 1.0],    # right elbow
    [-0.25, 1.25], # left hand
    [0.25, 1.25],  # right hand
    [-0.25, 0.25], # head
    [0, 1.5]       # top of head
])

# Define the rotation angles for the different body parts
# Each row represents a time step, with the columns representing the rotation angles for the different body parts
angles = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # initial position
    [0, 0, -np.pi/4, np.pi/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # turn left
    [0, 0, -np.pi/2, np.pi/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # turn left
    [0, 0, -3*np.pi/4, 3*np.pi/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # turn left
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # back to initial position
])

# Define the rotation centers for the different body parts
# Each row represents a body part, with the first column being the x-coordinate of the rotation center and the second column being the y-coordinate
rotation_centers = np.array([
    [0, 0],  # left foot
    [0, 0],  # right foot
    [-0.25, -0.25],  # left knee
    [0.25, -0.25],  # right knee
    [-0.5, 0.25],  # left hip
    [0.5, 0.25],  # right hip
    [0, 0.5],  # center of mass
    [-0.25, 0.75],  # left shoulder
    [0.25, 0.75],  # right shoulder
    [-0.5, 1.0],  # left elbow
    [0.5, 1.0],  # right elbow
    [-0.25, 1.25],  # left hand
    [0.25, 1.25],  # right hand
    [-0.25, 0.25],  # head
    [0, 1.5]  # top of head
])

# Define the function to update the positions of the point-lights
def update(frame):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

    # Calculate the positions of the point-lights at the current time step
    positions = np.copy(lights)
    for i in range(len(lights)):
        if i == 0 or i == 1:  # feet
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 0]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 0]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 0]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 0]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 2 or i == 3:  # knees
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 1]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 1]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 1]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 1]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 4 or i == 5:  # hips
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 2]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 2]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 2]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 2]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 6:  # center of mass
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 3]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 3]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 3]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 3]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 7 or i == 8:  # shoulders
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 4]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 4]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 4]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 4]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 9 or i == 10:  # elbows
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 5]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 5]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 5]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 5]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 11 or i == 12:  # hands
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 6]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 6]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 6]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 6]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 13:  # head
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 7]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 7]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 7]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 7]) * (lights[i, 1] - rotation_centers[i, 1])])
        elif i == 14:  # top of head
            positions[i, :] = np.array([rotation_centers[i, 0] + np.cos(angles[frame, 8]) * (lights[i, 0] - rotation_centers[i, 0]) - np.sin(angles[frame, 8]) * (lights[i, 1] - rotation_centers[i, 1]),
                                        rotation_centers[i, 1] + np.sin(angles[frame, 8]) * (lights[i, 0] - rotation_centers[i, 0]) + np.cos(angles[frame, 8]) * (lights[i, 1] - rotation_centers[i, 1])])

    # Plot the point-lights
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=len(angles), interval=1000, repeat=True)
plt.show()
