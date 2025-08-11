
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define joint positions relative to a person in a standing pose (in arbitrary units)
# We will animate these positions to simulate running

# Joints (15 points): left and right hip, knee, ankle, shoulder, elbow, wrist, head, spine
# Each joint is [x, y] in relative coordinates, with y increasing upwards

def standing_pose():
    return np.array([
        [ -1.0, 0.0 ],  # left hip
        [ -0.5, -0.5 ], # left knee
        [ 0.0, -1.0 ],  # left ankle
        [ 1.0, 0.0 ],   # right hip
        [ 0.5, -0.5 ],  # right knee
        [ 0.0, -1.0 ],  # right ankle
        [ -0.5, 1.0 ],  # left shoulder
        [ -0.25, 1.5 ], # left elbow
        [ 0.0, 2.0 ],   # left wrist
        [ 0.5, 1.0 ],   # right shoulder
        [ 0.25, 1.5 ],  # right elbow
        [ 0.0, 2.0 ],   # right wrist
        [ 0.0, 2.5 ],   # head
        [ 0.0, 1.5 ],   # spine
        [ 0.0, 0.0 ]    # center of motion (pelvis)
    ])

# Function to animate the running motion by shifting and rotating limbs
def animate_running(frame, points, center, speed=0.05):
    t = frame * speed

    # Simple sinusoidal motion for legs and arms to simulate running
    leg_angle = np.sin(t)
    arm_angle = np.sin(t + np.pi / 2)

    # Update positions based on animation
    points[0] = center + [ -1.0, 0.0 + 0.5 * np.sin(t + np.pi / 2) ]
    points[1] = center + [ -0.5 + 0.25 * np.cos(leg_angle), -0.5 + 0.25 * np.sin(leg_angle) ]
    points[2] = center + [ 0.0 + 0.25 * np.cos(leg_angle), -1.0 + 0.25 * np.sin(leg_angle) ]
    points[3] = center + [ 1.0, 0.0 + 0.5 * np.sin(t - np.pi / 2) ]
    points[4] = center + [ 0.5 - 0.25 * np.cos(leg_angle), -0.5 + 0.25 * np.sin(leg_angle) ]
    points[5] = center + [ 0.0 - 0.25 * np.cos(leg_angle), -1.0 + 0.25 * np.sin(leg_angle) ]
    points[6] = center + [ -0.5, 1.0 + 0.5 * np.sin(arm_angle) ]
    points[7] = center + [ -0.25, 1.5 + 0.5 * np.sin(arm_angle + np.pi / 2) ]
    points[8] = center + [ 0.0, 2.0 + 0.5 * np.sin(arm_angle) ]
    points[9] = center + [ 0.5, 1.0 + 0.5 * np.sin(arm_angle) ]
    points[10] = center + [ 0.25, 1.5 + 0.5 * np.sin(arm_angle + np.pi / 2) ]
    points[11] = center + [ 0.0, 2.0 + 0.5 * np.sin(arm_angle) ]
    points[12] = center + [ 0.0, 2.5 + 0.25 * np.sin(arm_angle) ]
    points[13] = center + [ 0.0, 1.5 + 0.25 * np.sin(arm_angle) ]
    points[14] = center  # center of motion (pelvis)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
ax.axis('off')

# Create white point-light circles
points = standing_pose().copy()
center = points[14].copy()

circles = [plt.Circle((x, y), 0.05, color='white') for x, y in points]
for circle in circles:
    ax.add_patch(circle)

# Update function for animation
def update(frame):
    animate_running(frame, points, center)
    for i, circle in enumerate(circles):
        circle.center = (points[i][0], points[i][1])
    return circles

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
