
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
body_parts = [
    ('head', 0), ('shoulder_left', 1), ('elbow_left', 2), ('wrist_left', 3),
    ('shoulder_right', 4), ('elbow_right', 5), ('wrist_right', 6),
    ('hip_left', 7), ('knee_left', 8), ('ankle_left', 9),
    ('hip_right', 10), ('knee_right', 11), ('ankle_right', 12),
    ('spine', 13), ('pelvis', 14)
]

# Define the initial positions of the body parts
initial_positions = np.array([
    [0, 0.5],   # head
    [-0.2, 0.3], # shoulder_left
    [-0.4, 0.1], # elbow_left
    [-0.4, -0.1], # wrist_left
    [0.2, 0.3], # shoulder_right
    [0.4, 0.1], # elbow_right
    [0.4, -0.1], # wrist_right
    [-0.2, -0.3], # hip_left
    [-0.3, -0.5], # knee_left
    [-0.3, -0.7], # ankle_left
    [0.2, -0.3], # hip_right
    [0.3, -0.5], # knee_right
    [0.3, -0.7], # ankle_right
    [0, 0], # spine
    [0, -0.5] # pelvis
])

# Define the motion parameters for a jumping motion
def jump_motion(t, total_time=1.0):
    # Jump up and down over time
    jump_height = 0.5
    t_normalized = t / total_time
    y = -jump_height * np.cos(np.pi * t_normalized)
    return y

# Define the motion for each body part
def get_position(t, body_part_index):
    if body_part_index == 13:  # spine
        return initial_positions[body_part_index] + [0, jump_motion(t)]
    elif body_part_index == 14:  # pelvis
        return initial_positions[body_part_index] + [0, jump_motion(t)]
    elif body_part_index in [1, 4, 7, 10]:  # shoulders and hips
        return initial_positions[body_part_index] + [0, jump_motion(t)]
    elif body_part_index in [2, 5, 8, 11]:  # elbows and knees
        return initial_positions[body_part_index] + [0, jump_motion(t) * 0.5]
    elif body_part_index in [3, 6, 9, 12]:  # wrists and ankles
        return initial_positions[body_part_index] + [0, jump_motion(t) * 0.25]
    else:
        return initial_positions[body_part_index]

# Create the point lights
points = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for point in points:
    ax.add_patch(point)

# Animation function
def animate(t):
    for i, point in enumerate(points):
        x, y = get_position(t, i)
        point.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
