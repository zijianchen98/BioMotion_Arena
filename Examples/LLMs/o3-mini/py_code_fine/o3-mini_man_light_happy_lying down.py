
"""
This program displays a point‐light stimulus animation representing biological motion.
It depicts a happy man with light weight lying down using 15 white point-lights on a black background.
Each point represents a key joint of the body (e.g., head, neck, shoulders, elbows, wrists,
pelvis, knees, ankles, toes) and they move with smooth sinusoidal oscillations simulating natural “breathing”
and subtle limb motion. The parameters (amplitude and phase) have been chosen for biomechanical plausibility.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the fixed skeleton layout
# Coordinates are chosen for a man lying horizontally (head on the left, feet on the right)
# Each tuple is (x, y). The y-coordinate small offsets simulate left/right differences.
# Points (index):
#  0: Head
#  1: Neck
#  2: Right Shoulder
#  3: Left Shoulder
#  4: Right Elbow
#  5: Left Elbow
#  6: Right Wrist
#  7: Left Wrist
#  8: Pelvis (hip center)
#  9: Right Knee
# 10: Left Knee
# 11: Right Ankle
# 12: Left Ankle
# 13: Right Toe
# 14: Left Toe

base_positions = np.array([
    [1.0,  0.0],    # Head
    [2.0,  0.0],    # Neck
    [2.5, -0.5],    # Right Shoulder
    [2.5,  0.5],    # Left Shoulder
    [3.5, -0.5],    # Right Elbow
    [3.5,  0.5],    # Left Elbow
    [4.5, -0.5],    # Right Wrist
    [4.5,  0.5],    # Left Wrist
    [4.0,  0.0],    # Pelvis
    [5.0, -0.3],    # Right Knee
    [5.0,  0.3],    # Left Knee
    [6.0, -0.3],    # Right Ankle
    [6.0,  0.3],    # Left Ankle
    [6.5, -0.3],    # Right Toe
    [6.5,  0.3]     # Left Toe
])

# For a natural effect, assign each point a (small) oscillatory amplitude and phase.
# The amplitudes are larger for torso points and smaller for distal limb points.
oscillation_params = [
    (0.10, 0.0),    # Head
    (0.12, 0.2),    # Neck
    (0.10, 0.4),    # Right Shoulder
    (0.10, 0.4),    # Left Shoulder
    (0.07, 0.6),    # Right Elbow
    (0.07, 0.6),    # Left Elbow
    (0.05, 0.8),    # Right Wrist
    (0.05, 0.8),    # Left Wrist
    (0.12, 1.0),    # Pelvis
    (0.08, 1.2),    # Right Knee
    (0.08, 1.2),    # Left Knee
    (0.05, 1.4),    # Right Ankle
    (0.05, 1.4),    # Left Ankle
    (0.03, 1.6),    # Right Toe
    (0.03, 1.6)     # Left Toe
]

# Animation settings
period = 5  # seconds for a full oscillatory cycle
omega = 2 * np.pi / period

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8,4))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(0, 8)
ax.set_ylim(-1.5, 1.5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Point-Light Biological Motion (Lying Down)", color='white')

# Create the scatter plot with 15 points (white circles)
scat = ax.scatter(base_positions[:,0], base_positions[:,1], s=100, c='white')

def animate(frame):
    t = frame / 30.0  # assuming 30 fps; adjust time step accordingly
    new_positions = base_positions.copy()
    
    # Apply a smooth sinusoidal vertical oscillation to each point.
    for i, (amp, phase) in enumerate(oscillation_params):
        # For a lying down subject, the vertical direction is simulated as slight offsets.
        delta = amp * np.sin(omega * t + phase)
        new_positions[i, 1] = base_positions[i, 1] + delta

    # Optionally, add a slight horizontal jitter for extra natural motion (very subtle)
    # Uncomment the following two lines to add horizontal jitter:
    # jitter = 0.005 * np.sin(omega * t + 0.5)
    # new_positions[:, 0] += jitter

    scat.set_offsets(new_positions)
    return scat,

anim = FuncAnimation(fig, animate, frames=300, interval=33, blit=True)

# Uncomment the next line to save the animation as a video file (requires ffmpeg)
# anim.save('point_light_biological_motion.mp4', writer='ffmpeg', fps=30)

plt.show()