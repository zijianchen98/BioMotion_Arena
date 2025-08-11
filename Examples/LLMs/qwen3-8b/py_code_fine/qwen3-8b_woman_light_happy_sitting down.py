
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the body parts and their positions (simplified for a sitting woman)
body_parts = {
    'hips': np.array([0, 0]),
    'left_knee': np.array([0.2, -0.3]),
    'right_knee': np.array([-0.2, -0.3]),
    'left_ankle': np.array([0.3, -0.5]),
    'right_ankle': np.array([-0.3, -0.5]),
    'left_shoulder': np.array([0.2, 0.3]),
    'right_shoulder': np.array([-0.2, 0.3]),
    'left_elbow': np.array([0.3, 0.1]),
    'right_elbow': np.array([-0.3, 0.1]),
    'left_wrist': np.array([0.4, -0.1]),
    'right_wrist': np.array([-0.4, -0.1]),
    'head': np.array([0, 0.5]),
    'neck': np.array([0, 0.4]),
    'left_hand': np.array([0.4, -0.2]),
    'right_hand': np.array([-0.4, -0.2]),
    'left_hip': np.array([0.1, -0.1]),
    'right_hip': np.array([-0.1, -0.1]),
}

# Define the point-light positions (15 points)
point_lights = [
    body_parts['hips'],
    body_parts['left_knee'],
    body_parts['right_knee'],
    body_parts['left_ankle'],
    body_parts['right_ankle'],
    body_parts['left_shoulder'],
    body_parts['right_shoulder'],
    body_parts['left_elbow'],
    body_parts['right_elbow'],
    body_parts['left_wrist'],
    body_parts['right_wrist'],
    body_parts['head'],
    body_parts['neck'],
    body_parts['left_hand'],
    body_parts['right_hand'],
]

# Define a function to simulate the sitting motion
def animate(i):
    # Define a time-dependent motion for the sitting action
    t = i / 100.0  # Normalize time

    # Define the motion for each body part
    for part in body_parts:
        if part == 'hips':
            # Hips move down slightly as the person sits
            body_parts[part][1] = -0.1 * (1 - np.cos(t * np.pi))
        elif part == 'left_knee' or part == 'right_knee':
            # Knees bend as the person sits
            body_parts[part][1] = -0.3 + 0.2 * (1 - np.cos(t * np.pi))
        elif part == 'left_ankle' or part == 'right_ankle':
            # Ankles move down as the person sits
            body_parts[part][1] = -0.5 + 0.2 * (1 - np.cos(t * np.pi))
        elif part == 'left_shoulder' or part == 'right_shoulder':
            # Shoulders move slightly down as the person sits
            body_parts[part][1] = 0.3 - 0.1 * (1 - np.cos(t * np.pi))
        elif part == 'left_elbow' or part == 'right_elbow':
            # Elbows bend slightly
            body_parts[part][1] = 0.1 - 0.05 * (1 - np.cos(t * np.pi))
        elif part == 'left_wrist' or part == 'right_wrist':
            # Wrists move slightly down
            body_parts[part][1] = -0.2 + 0.1 * (1 - np.cos(t * np.pi))
        elif part == 'head':
            # Head slightly lowers
            body_parts[part][1] = 0.5 - 0.1 * (1 - np.cos(t * np.pi))
        elif part == 'neck':
            # Neck slightly lowers
            body_parts[part][1] = 0.4 - 0.05 * (1 - np.cos(t * np.pi))
        elif part == 'left_hand' or part == 'right_hand':
            # Hands move slightly down
            body_parts[part][1] = -0.2 + 0.1 * (1 - np.cos(t * np.pi))

    # Clear the previous points
    for circle in point_light_circles:
        circle.remove()

    # Create new point lights
    point_light_circles = []
    for pos in point_lights:
        circle = Circle((pos[0], pos[1]), 0.02, color='white')
        ax.add_patch(circle)
        point_light_circles.append(circle)

    return point_light_circles

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

plt.show()
