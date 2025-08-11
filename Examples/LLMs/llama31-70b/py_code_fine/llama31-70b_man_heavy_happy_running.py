
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happyman
point_lights = np.array([
    [0.5, 0.5],  # head
    [0.5, 0.6],  # right shoulder
    [0.5, 0.4],  # left shoulder
    [0.6, 0.7],  # right elbow
    [0.4, 0.7],  # left elbow
    [0.7, 0.8],  # right wrist
    [0.3, 0.8],  # left wrist
    [0.5, 0.3],  # right hip
    [0.5, 0.2],  # left hip
    [0.6, 0.1],  # right knee
    [0.4, 0.1],  # left knee
    [0.7, 0.0],  # right ankle
    [0.3, 0.0],  # left ankle
    [0.5, 0.9],  # torso
    [0.5, 0.1]  # weight
])

# Define the motion for the happyman running
def update(frame):
    global point_lights
    # Update the point-light locations based on the running motion
    head = point_lights[0] + np.array([0.01 * np.sin(frame * 0.1), 0.01 * np.cos(frame * 0.1)])
    right_shoulder = point_lights[1] + np.array([0.02 * np.sin(frame * 0.1), -0.02 * np.cos(frame * 0.1)])
    left_shoulder = point_lights[2] + np.array([-0.02 * np.sin(frame * 0.1), -0.02 * np.cos(frame * 0.1)])
    right_elbow = right_shoulder + np.array([0.03 * np.sin(frame * 0.1), -0.03 * np.cos(frame * 0.1)])
    left_elbow = left_shoulder + np.array([-0.03 * np.sin(frame * 0.1), -0.03 * np.cos(frame * 0.1)])
    right_wrist = right_elbow + np.array([0.04 * np.sin(frame * 0.1), -0.04 * np.cos(frame * 0.1)])
    left_wrist = left_elbow + np.array([-0.04 * np.sin(frame * 0.1), -0.04 * np.cos(frame * 0.1)])
    right_hip = point_lights[7] + np.array([0.01 * np.sin(frame * 0.1), -0.01 * np.cos(frame * 0.1)])
    left_hip = point_lights[8] + np.array([-0.01 * np.sin(frame * 0.1), -0.01 * np.cos(frame * 0.1)])
    right_knee = right_hip + np.array([0.02 * np.sin(frame * 0.1), -0.02 * np.cos(frame * 0.1)])
    left_knee = left_hip + np.array([-0.02 * np.sin(frame * 0.1), -0.02 * np.cos(frame * 0.1)])
    right_ankle = right_knee + np.array([0.03 * np.sin(frame * 0.1), -0.03 * np.cos(frame * 0.1)])
    left_ankle = left_knee + np.array([-0.03 * np.sin(frame * 0.1), -0.03 * np.cos(frame * 0.1)])
    torso = point_lights[13] + np.array([0.005 * np.sin(frame * 0.1), 0.005 * np.cos(frame * 0.1)])
    weight = point_lights[14] + np.array([0.01 * np.sin(frame * 0.1), -0.01 * np.cos(frame * 0.1)])

    point_lights = np.array([
        head, right_shoulder, left_shoulder, right_elbow, left_elbow,
        right_wrist, left_wrist, right_hip, left_hip, right_knee, left_knee,
        right_ankle, left_ankle, torso, weight
    ])

    # Clear the previous frame
    ax.clear()

    # Plot the point-lights
    ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white', s=10)

    # Set the background color to black
    ax.set_facecolor('black')

    # Set the limits of the axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Remove the axes
    ax.set_axis_off()

# Create a new figure
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the animation
plt.show()
