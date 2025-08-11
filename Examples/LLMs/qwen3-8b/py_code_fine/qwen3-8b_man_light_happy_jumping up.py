
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
    'torso': 1,
    'left_upper_arm': 2,
    'left_lower_arm': 3,
    'left_hand': 4,
    'right_upper_arm': 5,
    'right_lower_arm': 6,
    'right_hand': 7,
    'left_upper_leg': 8,
    'left_lower_leg': 9,
    'left_foot': 10,
    'right_upper_leg': 11,
    'right_lower_leg': 12,
    'right_foot': 13,
    'hips': 14
}

# Define the joint connections
joint_connections = [
    (body_parts['head'], body_parts['torso']),
    (body_parts['torso'], body_parts['hips']),
    (body_parts['hips'], body_parts['left_upper_leg']),
    (body_parts['hips'], body_parts['right_upper_leg']),
    (body_parts['left_upper_leg'], body_parts['left_lower_leg']),
    (body_parts['left_lower_leg'], body_parts['left_foot']),
    (body_parts['right_upper_leg'], body_parts['right_lower_leg']),
    (body_parts['right_lower_leg'], body_parts['right_foot']),
    (body_parts['torso'], body_parts['left_upper_arm']),
    (body_parts['left_upper_arm'], body_parts['left_lower_arm']),
    (body_parts['left_lower_arm'], body_parts['left_hand']),
    (body_parts['torso'], body_parts['right_upper_arm']),
    (body_parts['right_upper_arm'], body_parts['right_lower_arm']),
    (body_parts['right_lower_arm'], body_parts['right_hand'])
]

# Define the initial positions of the body parts
positions = np.zeros((15, 2))
positions[body_parts['hips']] = [0, -0.5]
positions[body_parts['torso']] = [0, -0.3]
positions[body_parts['head']] = [0, 0.2]
positions[body_parts['left_upper_leg']] = [-0.2, -0.5]
positions[body_parts['left_lower_leg']] = [-0.2, -0.7]
positions[body_parts['left_foot']] = [-0.2, -0.9]
positions[body_parts['right_upper_leg']] = [0.2, -0.5]
positions[body_parts['right_lower_leg']] = [0.2, -0.7]
positions[body_parts['right_foot']] = [0.2, -0.9]
positions[body_parts['left_upper_arm']] = [-0.2, -0.3]
positions[body_parts['left_lower_arm']] = [-0.2, -0.1]
positions[body_parts['left_hand']] = [-0.2, 0.1]
positions[body_parts['right_upper_arm']] = [0.2, -0.3]
positions[body_parts['right_lower_arm']] = [0.2, -0.1]
positions[body_parts['right_hand']] = [0.2, 0.1]

# Define the animation parameters
num_frames = 100
frame_rate = 30
amplitude = 0.2
frequency = 0.1

# Create circles for the point lights
circles = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for circle in circles:
    ax.add_patch(circle)

# Animation function
def animate(frame):
    global positions
    # Simulate jumping motion
    y_offset = amplitude * np.sin(2 * np.pi * frequency * frame)
    # Apply the offset to relevant body parts
    for part in [body_parts['hips'], body_parts['torso'], body_parts['head'],
                 body_parts['left_upper_leg'], body_parts['left_lower_leg'],
                 body_parts['left_foot'], body_parts['right_upper_leg'],
                 body_parts['right_lower_leg'], body_parts['right_foot'],
                 body_parts['left_upper_arm'], body_parts['left_lower_arm'],
                 body_parts['left_hand'], body_parts['right_upper_arm'],
                 body_parts['right_lower_arm'], body_parts['right_hand']]:
        positions[part][1] = positions[part][1] + y_offset
    # Update the positions of the point lights
    for i, circle in enumerate(circles):
        circle.center = positions[i]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/frame_rate, blit=False)

# Show the animation
plt.show()
