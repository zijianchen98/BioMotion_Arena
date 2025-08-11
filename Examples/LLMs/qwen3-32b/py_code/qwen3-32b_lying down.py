
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define 15 key joints (biomechanical points) for a human figure
# These are normalized joint positions for a person lying down
# The joints are: head, neck, spine1, spine2, spine3, left shoulder, left elbow, left hand,
#                right shoulder, right elbow, right hand, left hip, left knee, left foot,
#                right hip, right knee, right foot
# We'll animate them from standing to lying down

def lying_down_animation(t, duration=1.0):
    # t is the time in [0, 1]
    # We'll simulate a smooth transition from standing to lying down
    t = np.clip(t, 0, 1)
    ease = t**2 / (2 - t)  # smooth transition

    # Define joint positions for standing and lying down
    standing = np.array([
        [0, 0.8],     # head
        [0, 0.6],     # neck
        [0, 0.4],     # spine1
        [0, 0.2],     # spine2
        [0, 0.0],     # spine3
        [-0.1, 0.2],  # left shoulder
        [-0.2, 0.0],  # left elbow
        [-0.3, -0.2], # left hand
        [0.1, 0.2],   # right shoulder
        [0.2, 0.0],   # right elbow
        [0.3, -0.2],  # right hand
        [-0.2, 0.0],  # left hip
        [-0.2, -0.2], # left knee
        [-0.2, -0.4], # left foot
        [0.2, 0.0],   # right hip
        [0.2, -0.2],  # right knee
        [0.2, -0.4],  # right foot
    ])

    lying = np.array([
        [0, 0.0],     # head
        [0, 0.0],     # neck
        [0, 0.0],     # spine1
        [0, 0.0],     # spine2
        [0, 0.0],     # spine3
        [-0.1, 0.0],  # left shoulder
        [-0.2, 0.0],  # left elbow
        [-0.3, 0.0],  # left hand
        [0.1, 0.0],   # right shoulder
        [0.2, 0.0],   # right elbow
        [0.3, 0.0],   # right hand
        [-0.2, 0.0],  # left hip
        [-0.2, -0.2], # left knee
        [-0.2, -0.4], # left foot
        [0.2, 0.0],   # right hip
        [0.2, -0.2],  # right knee
        [0.2, -0.4],  # right foot
    ])

    # Interpolate between standing and lying down
    return (1 - ease) * standing + ease * lying

# Create 15 white points (circles)
points = [patches.Circle((0, 0), 0.01, color='white') for _ in range(15)]
for point in points:
    ax.add_patch(point)

# Update function for animation
def update(frame):
    t = frame / 100  # 100 frames = 1 full animation
    positions = lying_down_animation(t)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
