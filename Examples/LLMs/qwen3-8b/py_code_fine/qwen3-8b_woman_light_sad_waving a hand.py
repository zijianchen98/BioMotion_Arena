
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Define the body parts and their positions for a sad woman waving hand
# Coordinates are normalized to [-1, 1] for the plot
body_parts = {
    'head': np.array([0, 0.6]),
    'neck': np.array([0, 0.4]),
    'torso': np.array([0, 0.2]),
    'left_shoulder': np.array([-0.2, 0.2]),
    'right_shoulder': np.array([0.2, 0.2]),
    'left_elbow': np.array([-0.3, 0.0]),
    'right_elbow': np.array([0.3, 0.0]),
    'left_wrist': np.array([-0.4, -0.1]),
    'right_wrist': np.array([0.4, -0.1]),
    'left_hand': np.array([-0.45, -0.2]),
    'right_hand': np.array([0.45, -0.2]),
    'left_hip': np.array([-0.2, -0.4]),
    'right_hip': np.array([0.2, -0.4]),
    'left_knee': np.array([-0.3, -0.6]),
    'right_knee': np.array([0.3, -0.6]),
    'left_ankle': np.array([-0.4, -0.8]),
    'right_ankle': np.array([0.4, -0.8]),
}

# Define the point-light positions as a list of body parts
point_lights = list(body_parts.values())

# Create circles for each point-light
circles = [Circle((x, y), 0.02, color='white') for x, y in point_lights]
for circle in circles:
    ax.add_patch(circle)

# Define a function to animate the motion
def animate(frame):
    # Define a simple waving motion for the right hand
    hand_x = 0.45 + 0.1 * np.sin(0.05 * frame)
    hand_y = -0.2 + 0.05 * np.sin(0.05 * frame)
    body_parts['right_hand'][0] = hand_x
    body_parts['right_wrist'][0] = hand_x + 0.05
    body_parts['right_elbow'][0] = hand_x + 0.1
    body_parts['right_shoulder'][0] = hand_x + 0.2

    # Update positions of all point-lights
    for i, (x, y) in enumerate(body_parts.values()):
        circles[i].center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
