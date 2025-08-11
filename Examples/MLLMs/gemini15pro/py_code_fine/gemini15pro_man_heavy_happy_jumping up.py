
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint positions over time
# This is a simplified example and would need more frames for a smooth animation
joint_positions = {
    "head": [(0, 5), (0, 5.5), (0, 6)],
    "left_shoulder": [(-1, 4), (-1, 4.5), (-1, 5)],
    "right_shoulder": [(1, 4), (1, 4.5), (1, 5)],
    "left_elbow": [(-2, 3), (-2, 3.5), (-2, 4)],
    "right_elbow": [(2, 3), (2, 3.5), (2, 4)],
    "left_hand": [(-3, 2), (-3, 2.5), (-3, 3)],
    "right_hand": [(3, 2), (3, 2.5), (3, 3)],
    "left_hip": [(-1, 2), (-1, 1.5), (-1, 1)],
    "right_hip": [(1, 2), (1, 1.5), (1, 1)],
    "left_knee": [(-2, 0), (-2, -0.5), (-2, -1)],
    "right_knee": [(2, 0), (2, -0.5), (2, -1)],
    "left_foot": [(-3, -2), (-3, -2.5), (-3, -3)],
    "right_foot": [(3, -2), (3, -2.5), (3, -3)],
    "center": [(0, 2), (0, 2.5), (0, 3)],
    "center_lower": [(0,1), (0, 1.5), (0, 2)],
}



num_frames = len(list(joint_positions.values())[0])

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)  # Set x-axis limits
ax.set_ylim(-4, 6)  # Set y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])



# Initialize the points
points = []
for joint in joint_positions:
    point, = ax.plot([], [], 'o', color='white')
    points.append(point)


# Update function for the animation
def update(frame):
    for i, joint in enumerate(joint_positions):
        x, y = joint_positions[joint][frame]
        points[i].set_data(x, y)
    return points


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)



plt.show()
