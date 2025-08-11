
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()

# Define the point lights
point_lights = {
    'head': [0, 0],
    'left_eye': [-0.1, 0.1],
    'right_eye': [0.1, 0.1],
    'left_shoulder': [-0.3, -0.2],
    'right_shoulder': [0.3, -0.2],
    'left_elbow': [-0.4, -0.4],
    'right_elbow': [0.4, -0.4],
    'left_hand': [-0.45, -0.45],
    'right_hand': [0.45, -0.45],
    'left_hip': [-0.3, -0.6],
    'right_hip': [0.3, -0.6],
    'left_knee': [-0.35, -0.7],
    'right_knee': [0.35, -0.7],
    'left_foot': [-0.4, -0.8],
    'right_foot': [0.4, -0.8]
}

# Define the action
def sit_down(point_lights, frame):
    # Calculate the movement of each point light
    t = frame / 30  # 30 frames for the animation
    head_x = 0
    left_eye_x = -0.1 + 0.2 * np.sin(2 * np.pi * t)
    right_eye_x = 0.1 + 0.2 * np.sin(2 * np.pi * t)
    left_shoulder_x = -0.3 - 0.2 * np.sin(2 * np.pi * t)
    right_shoulder_x = 0.3 + 0.2 * np.sin(2 * np.pi * t)
    left_elbow_x = -0.4 - 0.2 * np.sin(2 * np.pi * t)
    right_elbow_x = 0.4 + 0.2 * np.sin(2 * np.pi * t)
    left_hand_x = -0.45 - 0.2 * np.sin(2 * np.pi * t)
    right_hand_x = 0.45 + 0.2 * np.sin(2 * np.pi * t)
    left_hip_x = -0.3 - 0.2 * np.sin(2 * np.pi * t)
    right_hip_x = 0.3 + 0.2 * np.sin(2 * np.pi * t)
    left_knee_x = -0.35 - 0.2 * np.sin(2 * np.pi * t)
    right_knee_x = 0.35 + 0.2 * np.sin(2 * np.pi * t)
    left_foot_x = -0.4 - 0.2 * np.sin(2 * np.pi * t)
    right_foot_x = 0.4 + 0.2 * np.sin(2 * np.pi * t)

    # Update the point lights
    point_lights['head'][0] = head_x
    point_lights['left_eye'][0] = left_eye_x
    point_lights['right_eye'][0] = right_eye_x
    point_lights['left_shoulder'][0] = left_shoulder_x
    point_lights['right_shoulder'][0] = right_shoulder_x
    point_lights['left_elbow'][0] = left_elbow_x
    point_lights['right_elbow'][0] = right_elbow_x
    point_lights['left_hand'][0] = left_hand_x
    point_lights['right_hand'][0] = right_hand_x
    point_lights['left_hip'][0] = left_hip_x
    point_lights['right_hip'][0] = right_hip_x
    point_lights['left_knee'][0] = left_knee_x
    point_lights['right_knee'][0] = right_knee_x
    point_lights['left_foot'][0] = left_foot_x
    point_lights['right_foot'][0] = right_foot_x

# Create the point lights
def create_point_lights(point_lights):
    for point, position in point_lights.items():
        ax.plot(position[0], position[1], 'wo', markersize=10)

# Animate the point lights
def animate(frame):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-1, 0)
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    sit_down(point_lights, frame)
    create_point_lights(point_lights)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=30, interval=50, repeat=False)

# Show the animation
plt.show()
