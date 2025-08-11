
"""
This program shows an animation of a point‐light stimulus depicting a “sadman with heavy weight” lying down.
It uses exactly 15 white “point-lights” (joints) on a black background.
The 15 points represent key joints of the body (head, neck, shoulders, elbows, wrists, torso, hips, knees, ankles)
arranged in a lying down (supine) posture. A subtle breathing motion is simulated to create a smooth,
biomechanically plausible animation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define base joint positions for a lying down posture.
# The coordinate system is chosen in normalized units (0 to 1) with origin at bottom left.
# Body is oriented horizontally (head on the right, feet on the left).
# 15 joints (indices):
# 0: Head
# 1: Neck
# 2: Left Shoulder
# 3: Right Shoulder
# 4: Left Elbow
# 5: Right Elbow
# 6: Left Wrist
# 7: Right Wrist
# 8: Torso (center)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Ankle
# 14: Right Ankle

# These base positions were chosen to give a plausible supine (lying on back) posture.
base_positions = np.array([
    [0.80, 0.50],  # 0: Head
    [0.75, 0.50],  # 1: Neck
    [0.73, 0.53],  # 2: Left Shoulder (a bit raised)
    [0.73, 0.47],  # 3: Right Shoulder (a bit lowered)
    [0.65, 0.55],  # 4: Left Elbow
    [0.65, 0.45],  # 5: Right Elbow
    [0.60, 0.57],  # 6: Left Wrist
    [0.60, 0.43],  # 7: Right Wrist
    [0.70, 0.50],  # 8: Torso (center of the body)
    [0.66, 0.52],  # 9: Left Hip
    [0.66, 0.48],  #10: Right Hip
    [0.55, 0.52],  #11: Left Knee
    [0.55, 0.48],  #12: Right Knee
    [0.45, 0.52],  #13: Left Ankle
    [0.45, 0.48]   #14: Right Ankle
])

# For added biomechanical plausibility, assign a "breathing factor" to each point.
# Points that are closer to the torso (chest) move fully while extremities move less.
breathing_factors = np.array([
    1.0,  # Head
    1.0,  # Neck
    0.9,  # Left Shoulder
    0.9,  # Right Shoulder
    0.7,  # Left Elbow
    0.7,  # Right Elbow
    0.5,  # Left Wrist
    0.5,  # Right Wrist
    1.0,  # Torso
    0.9,  # Left Hip
    0.9,  # Right Hip
    0.7,  # Left Knee
    0.7,  # Right Knee
    0.5,  # Left Ankle
    0.5   # Right Ankle
])

# Parameters for the breathing (subtle up-down motion)
breathing_amplitude = 0.01   # maximal vertical displacement
breathing_period = 5.0       # seconds for a full cycle

# Create the figure and the scatter plot with a black background.
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

# Create the scatter plot: 15 points, white color.
scatter = ax.scatter(base_positions[:, 0], base_positions[:, 1],
                     s=100, c='white', marker='o')

# Function to update the positions of the joints at time t.
def update(frame):
    # frame is the current frame number; use dt (in seconds) based on frame rate.
    t = frame / 50.0  # assume 50 frames per second approximately.
    # Compute breathing offset
    offset = breathing_amplitude * np.sin(2 * np.pi * t / breathing_period)
    
    # For biomechanical plausibility, apply a vertical offset scaled by the breathing factors.
    new_positions = base_positions.copy()
    new_positions[:, 1] = base_positions[:, 1] + breathing_factors * offset
    
    # Update scatter plot positions.
    scatter.set_offsets(new_positions)
    return scatter,

# Use FuncAnimation to animate the stimulus.
ani = FuncAnimation(fig, update, frames=np.arange(0, 250), interval=20, blit=True)

# Display the animation.
plt.show()