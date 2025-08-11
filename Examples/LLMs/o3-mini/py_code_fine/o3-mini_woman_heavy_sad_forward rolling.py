
"""
This program creates a point‐light animation in which 15 white dots – arranged like
a “sad” female figure – perform a forward roll (a full 360° rotation) across a black background.
The figure is defined by 15 fixed offsets (in a “neutral pose”) that capture the head,
shoulders, arms, torso, hips, knees and feet. Over the course of the animation these 15 points are:
  • rotated by a continuously changing angle (to simulate a forward roll),
  • translated across the screen (to simulate forward motion).

The resulting animation is smooth, biomechanically plausible in its overall movement,
and depicts the heavy, sad posture of the woman as she rolls forward.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the 15 “body marker” offsets in a neutral pose.
# (x,y) coordinates relative to the figure's center.
# These values are chosen to resemble a sad posture:
# Slumped head, low shoulders, down arms, and heavy legs.
body_markers = np.array([
    [ 0.0,   2.0],    # 1. Head
    [-0.5,   1.5],    # 2. Left shoulder
    [ 0.5,   1.5],    # 3. Right shoulder
    [-0.75,  1.0],    # 4. Left elbow
    [ 0.75,  1.0],    # 5. Right elbow
    [-1.0,   0.75],   # 6. Left hand
    [ 1.0,   0.75],   # 7. Right hand
    [ 0.0,   1.2],    # 8. Upper torso
    [ 0.0,   0.5],    # 9. Lower torso
    [-0.3,   0.0],    # 10. Left hip
    [ 0.3,   0.0],    # 11. Right hip
    [-0.3,  -1.0],    # 12. Left knee
    [ 0.3,  -1.0],    # 13. Right knee
    [-0.3,  -1.5],    # 14. Left foot
    [ 0.3,  -1.5]     # 15. Right foot
])

# Animation parameters
fps = 30
duration = 5           # seconds, one forward roll
frames = fps * duration

# Set up figure and axis.
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
# axis limits chosen to show the entire motion
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Scatter plot for the 15 white point-lights.
scatter = ax.scatter([], [], c='white', s=50)

def transform_markers(offsets, angle, center):
    """
    Rotate the offsets by 'angle' radians and then translate by 'center'.
    offsets: array of shape (15,2)
    angle: rotation angle in radians.
    center: translation vector (x,y)
    Returns an array of shape (15,2) with transformed positions.
    """
    # Rotation matrix (counter-clockwise)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    # Rotate each point and then add center offset
    transformed = (R @ offsets.T).T + center
    return transformed

def animate(frame):
    # time variable normalized to animation duration in [0,1]
    t = frame / frames

    # For a forward roll, we simulate a full 360 degrees rotation.
    roll_angle = 2 * np.pi * t  # full rotation over duration

    # Simulate forward translation.
    # Let the center move linearly from left to right (from x=-3 to x=3).
    # For a heavy body, use a slight vertical bounce to reflect the rolling dynamics.
    center_x = -3 + 6 * t
    # A small cosine “bounce” (rolling has slight vertical modulation)
    center_y = -1 + 0.5 * np.cos(2 * np.pi * t)
    center = np.array([center_x, center_y])

    # Transform markers
    points = transform_markers(body_markers, roll_angle, center)
    scatter.set_offsets(points)
    return scatter,

# Create the animation
anim = FuncAnimation(fig, animate, frames=frames, interval=1000/fps, blit=True)

# To show the animation, uncomment the following line:
plt.show()

# Uncomment the following lines to save the animation to a file (requires ffmpeg or imagemagick).
# anim.save('forward_roll_pointlight.mp4', writer='ffmpeg', fps=fps)
