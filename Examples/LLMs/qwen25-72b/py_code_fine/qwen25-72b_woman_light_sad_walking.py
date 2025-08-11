
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the key joints of a walking woman
# These points are simplified and may need to be adjusted for realism
points = [
    [0, 0],  # Head
    [-0.1, -0.1],  # Left Shoulder
    [0.1, -0.1],  # Right Shoulder
    [-0.2, -0.3],  # Left Elbow
    [0.2, -0.3],  # Right Elbow
    [-0.3, -0.5],  # Left Hand
    [0.3, -0.5],  # Right Hand
    [0, -0.6],  # Spine
    [-0.1, -0.8],  # Left Hip
    [0.1, -0.8],  # Right Hip
    [-0.2, -1.0],  # Left Knee
    [0.2, -1.0],  # Right Knee
    [-0.3, -1.4],  # Left Foot
    [0.3, -1.4],  # Right Foot
    [0, -1.2]  # Pelvis
]

# Convert points to a NumPy array
points = np.array(points)

# Define the walking cycle
def walking_cycle(t):
    # Adjust the points based on the walking cycle
    # This is a simplified model and may need to be refined
    head_bob = 0.05 * np.sin(2 * np.pi * t)
    leg_swing = 0.2 * np.sin(2 * np.pi * t)
    arm_swing = 0.2 * np.sin(2 * np.pi * t + np.pi)

    points[0, 1] += head_bob  # Head bobbing
    points[8, 1] += leg_swing  # Left hip
    points[9, 1] -= leg_swing  # Right hip
    points[10, 1] += 2 * leg_swing  # Left knee
    points[11, 1] -= 2 * leg_swing  # Right knee
    points[12, 1] += 3 * leg_swing  # Left foot
    points[13, 1] -= 3 * leg_swing  # Right foot
    points[3, 1] += arm_swing  # Left elbow
    points[4, 1] -= arm_swing  # Right elbow
    points[5, 1] += 2 * arm_swing  # Left hand
    points[6, 1] -= 2 * arm_swing  # Right hand

    return points

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-1.5, 0.1)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Update function for the animation
def update(frame):
    new_points = walking_cycle(frame / 100)
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
