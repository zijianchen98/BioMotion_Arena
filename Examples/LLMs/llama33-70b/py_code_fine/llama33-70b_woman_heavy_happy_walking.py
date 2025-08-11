
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the happy woman with heavy weight
# Each point-light is represented by its x, y, and z coordinates
point_lights = {
    'head': np.array([0, 1.5, 0]),
    'left_shoulder': np.array([-0.5, 1.2, 0]),
    'right_shoulder': np.array([0.5, 1.2, 0]),
    'left_elbow': np.array([-0.7, 0.8, 0]),
    'right_elbow': np.array([0.7, 0.8, 0]),
    'left_wrist': np.array([-0.9, 0.5, 0]),
    'right_wrist': np.array([0.9, 0.5, 0]),
    'left_hip': np.array([-0.3, 0.2, 0]),
    'right_hip': np.array([0.3, 0.2, 0]),
    'left_knee': np.array([-0.3, -0.2, 0]),
    'right_knee': np.array([0.3, -0.2, 0]),
    'left_ankle': np.array([-0.3, -0.5, 0]),
    'right_ankle': np.array([0.3, -0.5, 0]),
    'left_foot': np.array([-0.3, -0.7, 0]),
    'right_foot': np.array([0.3, -0.7, 0]),
}

# Define the walking motion
def walking_motion(t):
    # Define the phase of the walking motion
    phase = t % 1

    # Define the movement of each point-light
    movements = {
        'head': np.array([0, 0, 0]),
        'left_shoulder': np.array([-0.1 * np.sin(2 * np.pi * phase), 0, 0]),
        'right_shoulder': np.array([0.1 * np.sin(2 * np.pi * phase), 0, 0]),
        'left_elbow': np.array([-0.2 * np.sin(2 * np.pi * phase), 0, 0]),
        'right_elbow': np.array([0.2 * np.sin(2 * np.pi * phase), 0, 0]),
        'left_wrist': np.array([-0.3 * np.sin(2 * np.pi * phase), 0, 0]),
        'right_wrist': np.array([0.3 * np.sin(2 * np.pi * phase), 0, 0]),
        'left_hip': np.array([-0.1 * np.sin(2 * np.pi * phase), 0, 0]),
        'right_hip': np.array([0.1 * np.sin(2 * np.pi * phase), 0, 0]),
        'left_knee': np.array([-0.2 * np.sin(2 * np.pi * phase), 0, 0]),
        'right_knee': np.array([0.2 * np.sin(2 * np.pi * phase), 0, 0]),
        'left_ankle': np.array([-0.3 * np.sin(2 * np.pi * phase), 0, 0]),
        'right_ankle': np.array([0.3 * np.sin(2 * np.pi * phase), 0, 0]),
        'left_foot': np.array([-0.3 * np.sin(2 * np.pi * phase), 0, 0]),
        'right_foot': np.array([0.3 * np.sin(2 * np.pi * phase), 0, 0]),
    }

    return movements

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the point-lights
point_light_positions = {key: value for key, value in point_lights.items()}

# Define the update function for the animation
def update(t):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 2.5)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the point-light positions
    movements = walking_motion(t)
    for key, value in point_lights.items():
        point_light_positions[key] = value + movements[key]

    # Plot the point-lights
    for key, value in point_light_positions.items():
        ax.plot(value[0], value[1], 'o', markersize=5, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50)

plt.show()
