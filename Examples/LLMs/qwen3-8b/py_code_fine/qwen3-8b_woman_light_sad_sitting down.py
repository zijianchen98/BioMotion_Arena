
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

# Define the body parts and their indices
body_parts = {
    'head': 0,
    'neck': 1,
    'torso': 2,
    'upper_left_arm': 3,
    'lower_left_arm': 4,
    'upper_right_arm': 5,
    'lower_right_arm': 6,
    'left_hip': 7,
    'left_knee': 8,
    'left_ankle': 9,
    'right_hip': 10,
    'right_knee': 11,
    'right_ankle': 12,
    'left_shoulder': 13,
    'right_shoulder': 14
}

# Initial positions (approximate coordinates for a sad woman sitting down)
initial_positions = np.array([
    [0, 0.5],   # head
    [0, 0.3],   # neck
    [0, 0.1],   # torso
    [-0.2, 0.1], # upper_left_arm
    [-0.3, 0.05], # lower_left_arm
    [0.2, 0.1],  # upper_right_arm
    [0.3, 0.05], # lower_right_arm
    [-0.2, -0.2], # left_hip
    [-0.2, -0.4], # left_knee
    [-0.2, -0.6], # left_ankle
    [0.2, -0.2], # right_hip
    [0.2, -0.4], # right_knee
    [0.2, -0.6], # right_ankle
    [-0.2, 0.1], # left_shoulder
    [0.2, 0.1]   # right_shoulder
])

# Define a function to simulate motion over time
def animate(frame):
    # Simulate sitting down motion
    t = frame / 100.0  # Normalize time to 0-1
    # Define motion for each body part
    positions = initial_positions.copy()

    # Head and neck move slightly down
    positions[body_parts['head'], 1] = 0.5 - 0.3 * t
    positions[body_parts['neck'], 1] = 0.3 - 0.2 * t

    # Torso moves down
    positions[body_parts['torso'], 1] = 0.1 - 0.2 * t

    # Upper arms move down and inward
    positions[body_parts['upper_left_arm'], 1] = 0.1 - 0.2 * t
    positions[body_parts['upper_left_arm'], 0] = -0.2 + 0.1 * t
    positions[body_parts['lower_left_arm'], 1] = 0.05 - 0.15 * t
    positions[body_parts['lower_left_arm'], 0] = -0.3 + 0.1 * t

    positions[body_parts['upper_right_arm'], 1] = 0.1 - 0.2 * t
    positions[body_parts['upper_right_arm'], 0] = 0.2 - 0.1 * t
    positions[body_parts['lower_right_arm'], 1] = 0.05 - 0.15 * t
    positions[body_parts['lower_right_arm'], 0] = 0.3 - 0.1 * t

    # Legs move down
    positions[body_parts['left_hip'], 1] = -0.2 - 0.2 * t
    positions[body_parts['left_knee'], 1] = -0.4 - 0.2 * t
    positions[body_parts['left_ankle'], 1] = -0.6 - 0.2 * t

    positions[body_parts['right_hip'], 1] = -0.2 - 0.2 * t
    positions[body_parts['right_knee'], 1] = -0.4 - 0.2 * t
    positions[body_parts['right_ankle'], 1] = -0.6 - 0.2 * t

    # Shoulders move slightly inward
    positions[body_parts['left_shoulder'], 0] = -0.2 + 0.1 * t
    positions[body_parts['right_shoulder'], 0] = 0.2 - 0.1 * t

    # Update positions of point lights
    for i, (x, y) in enumerate(positions):
        point_lights[i].center = (x, y)
        point_lights[i].set_color('white')

    return point_lights

# Create point light circles
point_lights = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for light in point_lights:
    ax.add_patch(light)

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
