
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

# Define the initial positions of the body parts
initial_positions = np.array([
    [0, 0.5],   # head
    [0, 0.3],   # neck
    [0, 0.1],   # torso
    [-0.2, 0.1], # upper_left_arm
    [-0.4, 0.1], # lower_left_arm
    [0.2, 0.1],  # upper_right_arm
    [0.4, 0.1],  # lower_right_arm
    [-0.3, -0.3], # left_hip
    [-0.3, -0.5], # left_knee
    [-0.3, -0.7], # left_ankle
    [0.3, -0.3], # right_hip
    [0.3, -0.5], # right_knee
    [0.3, -0.7], # right_ankle
    [-0.2, 0.1], # left_shoulder
    [0.2, 0.1]   # right_shoulder
])

# Define the motion parameters for jumping
def jump_motion(t, total_time=2.0):
    # Jumping motion: up and down
    t_norm = t / total_time
    if t_norm < 0.5:
        # Jumping up
        y = 0.5 + 0.5 * np.sin(np.pi * t_norm)
    else:
        # Coming back down
        y = 0.5 + 0.5 * np.sin(np.pi * (1 - t_norm))
    return y

# Create the point lights
points = [Circle((initial_positions[i][0], initial_positions[i][1]), 0.02, color='white') for i in range(15)]
for point in points:
    ax.add_patch(point)

# Function to update the positions of the point lights
def update(frame):
    t = frame / 100.0  # Normalize time to 0-1 for 100 frames
    for i in range(15):
        # Apply jump motion to torso and head
        if i in [body_parts['head'], body_parts['neck'], body_parts['torso']]:
            y = initial_positions[i][1] + jump_motion(t)
            x = initial_positions[i][0]
        else:
            # Apply simple oscillation for limbs
            if i in [body_parts['upper_left_arm'], body_parts['lower_left_arm'],
                     body_parts['upper_right_arm'], body_parts['lower_right_arm'],
                     body_parts['left_hip'], body_parts['left_knee'], body_parts['left_ankle'],
                     body_parts['right_hip'], body_parts['right_knee'], body_parts['right_ankle'],
                     body_parts['left_shoulder'], body_parts['right_shoulder']]:
                # Add small oscillation to simulate movement
                x = initial_positions[i][0] + 0.05 * np.sin(2 * np.pi * t)
                y = initial_positions[i][1] + 0.05 * np.cos(2 * np.pi * t)
            else:
                x, y = initial_positions[i]

        # Update the position of the point light
        points[i].center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=False)

plt.show()
