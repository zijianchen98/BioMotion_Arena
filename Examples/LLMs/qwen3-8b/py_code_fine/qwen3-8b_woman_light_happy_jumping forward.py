
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

# Define the 15 point-light positions (representing joints)
# These are approximate positions for a human body in a jumping motion
# Positions are relative to the center of the body
joint_positions = np.array([
    [0.0, 0.0],        # Spine
    [0.1, 0.1],        # Right shoulder
    [-0.1, 0.1],       # Left shoulder
    [0.15, 0.2],       # Right elbow
    [-0.15, 0.2],      # Left elbow
    [0.2, 0.3],        # Right wrist
    [-0.2, 0.3],       # Left wrist
    [0.0, 0.4],        # Head
    [0.05, 0.25],      # Right hip
    [-0.05, 0.25],     # Left hip
    [0.1, 0.15],       # Right knee
    [-0.1, 0.15],      # Left knee
    [0.15, 0.05],      # Right ankle
    [-0.15, 0.05],     # Left ankle
    [0.0, 0.0]         # Pelvis
])

# Define a biomechanically plausible jumping motion
def jump_motion(t, amplitude=0.2, frequency=0.5, phase=0):
    # Create a time-dependent motion for the body
    # This is a simplified model of a jumping motion
    # The spine and pelvis move up and down, while limbs follow
    spine_y = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    pelvis_y = amplitude * np.sin(2 * np.pi * frequency * t + phase - np.pi / 2)
    head_y = amplitude * np.sin(2 * np.pi * frequency * t + phase) + 0.05
    shoulder_y = amplitude * np.sin(2 * np.pi * frequency * t + phase) - 0.05
    hip_y = amplitude * np.sin(2 * np.pi * frequency * t + phase - np.pi / 2) - 0.05
    knee_y = amplitude * np.sin(2 * np.pi * frequency * t + phase - np.pi / 2) - 0.05
    ankle_y = amplitude * np.sin(2 * np.pi * frequency * t + phase - np.pi) - 0.05

    # Apply the motion to each joint
    positions = joint_positions.copy()
    positions[:, 1] += spine_y
    positions[0, 1] = spine_y
    positions[8, 1] = pelvis_y
    positions[1, 1] = shoulder_y
    positions[2, 1] = shoulder_y
    positions[3, 1] = shoulder_y
    positions[4, 1] = shoulder_y
    positions[5, 1] = shoulder_y
    positions[6, 1] = shoulder_y
    positions[7, 1] = head_y
    positions[9, 1] = hip_y
    positions[10, 1] = hip_y
    positions[11, 1] = hip_y
    positions[12, 1] = hip_y
    positions[13, 1] = hip_y
    positions[14, 1] = pelvis_y

    return positions

# Create the point-light circles
circles = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for circle in circles:
    ax.add_patch(circle)

# Animation function
def animate(t):
    positions = jump_motion(t)
    for i, circle in enumerate(circles):
        circle.center = positions[i]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
