
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of point lights
NUM_LIGHTS = 15

# Define the body parts and their positions (approximate for a happy woman turning around)
body_parts = {
    'head': np.array([0, 1.5]),
    'neck': np.array([0, 1.0]),
    'torso': np.array([0, 0.5]),
    'left_shoulder': np.array([-0.5, 0.5]),
    'right_shoulder': np.array([0.5, 0.5]),
    'left_elbow': np.array([-0.8, 0.2]),
    'right_elbow': np.array([0.8, 0.2]),
    'left_wrist': np.array([-1.1, -0.1]),
    'right_wrist': np.array([1.1, -0.1]),
    'left_hip': np.array([-0.5, -0.5]),
    'right_hip': np.array([0.5, -0.5]),
    'left_knee': np.array([-0.8, -0.8]),
    'right_knee': np.array([0.8, -0.8]),
    'left_ankle': np.array([-1.1, -1.1]),
    'right_ankle': np.array([1.1, -1.1]),
}

# Define the motion parameters for turning around
def motion(t):
    # Simulate a turning motion over time
    angle = t * np.pi / 4  # 90 degrees over 4 seconds
    scale = 1.0 + 0.1 * np.sin(t * 2 * np.pi)  # Slight oscillation for realism

    # Create a rotation matrix
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)

    # Apply rotation and scaling to each body part
    rotated = {}
    for part, pos in body_parts.items():
        x, y = pos
        rotated_x = x * cos_theta - y * sin_theta
        rotated_y = x * sin_theta + y * cos_theta
        rotated[part] = np.array([rotated_x * scale, rotated_y * scale])

    return rotated

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create the point lights
lights = [ax.plot([], [], 'o', color='white', markersize=10)[0] for _ in range(NUM_LIGHTS)]

# Initialize positions
positions = [np.array([0.0, 0.0]) for _ in range(NUM_LIGHTS)]

# Function to update the animation
def update(frame):
    # Get the current positions of the body parts
    current_positions = motion(frame)

    # Assign the body parts to the lights (simple assignment for demonstration)
    for i, part in enumerate(current_positions):
        positions[i] = part
        lights[i].set_data(positions[i][0], positions[i][1])

    return lights

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
