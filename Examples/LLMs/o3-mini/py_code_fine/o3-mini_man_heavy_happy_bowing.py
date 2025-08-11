
"""
This program displays an animation of a point‐light stimulus representing a happy heavy man bowing.
It uses matplotlib’s animation module to show 15 white point‐lights on a solid black background.
The 15 points represent key joints of the body (head, shoulders, elbows, hands, chest, hips, knees and feet).
The upper body (head, shoulders, elbows, hands and chest) rotates about the hip center to simulate 
a natural bowing motion.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Define the base coordinates for 15 points of the stick figure.
# Points indices:
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Left Hand
# 6: Right Hand
# 7: Chest (center of upper torso)
# 8: Hip Center (pivot for upper body rotation)
# 9: Left Hip
# 10: Right Hip
# 11: Left Knee
# 12: Right Knee
# 13: Left Foot
# 14: Right Foot
base_points = np.array([
    [0.0, 1.8],      # Head
    [-0.15, 1.4],    # Left Shoulder
    [0.15, 1.4],     # Right Shoulder
    [-0.3, 1.2],     # Left Elbow
    [0.3, 1.2],      # Right Elbow
    [-0.35, 1.0],    # Left Hand
    [0.35, 1.0],     # Right Hand
    [0.0, 1.4],      # Chest (center upper torso)
    [0.0, 1.0],      # Hip Center (also acts as the pivot for upper body rotation)
    [-0.1, 1.0],     # Left Hip
    [0.1, 1.0],      # Right Hip
    [-0.1, 0.6],     # Left Knee
    [0.1, 0.6],      # Right Knee
    [-0.1, 0.2],     # Left Foot
    [0.1, 0.2]       # Right Foot
])

# Indices of the points that belong to the upper body (to be rotated)
upper_body_indices = [0, 1, 2, 3, 4, 5, 6, 7]
# The pivot (hip center) for the upper body rotation is point index 8.
pivot = base_points[8].copy()

# Define animation parameters
frames = 120          # Total frames for the animation
theta_max = math.radians(30)  # Maximum bow angle (30 degrees) in radians.
# We'll animate a bow: the upper body rotates forward (clockwise) and then returns to upright.
# For a clockwise rotation in our coordinate system, we use negative angles.

# Prepare figure and axes with black background.
fig, ax = plt.subplots(figsize=(5,8))
ax.set_facecolor("black")
scat = ax.scatter(base_points[:,0], base_points[:,1], color="white", s=80)  # marker size as needed

# Set axis limits so the figure is comfortably in view.
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2.2)
ax.set_aspect('equal')
ax.axis("off")

# Function to apply a 2D rotation about the pivot.
def rotate_points(points, angle, pivot_point):
    # Rotation matrix for angle (clockwise if angle is negative)
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    R = np.array([[cos_theta, -sin_theta],
                  [sin_theta,  cos_theta]])
    # Shift points so that pivot is the origin, rotate, then shift back.
    return (points - pivot_point) @ R.T + pivot_point

# Animation update function.
def update(frame):
    # Determine the normalized progress p between 0 and 1.
    # For the first half, p increases from 0 to 1 (bowing down).
    # For the second half, p decreases from 1 to 0 (returning to upright).
    if frame <= frames/2:
        p = frame / (frames/2)
    else:
        p = (frames - frame) / (frames/2)
    
    # Compute the angle for this frame (clockwise, so negative).
    angle = - p * theta_max
    
    # Create a copy of the base points so as not to modify the original.
    points = base_points.copy()
    
    # Apply rotation to the upper body points about the pivot.
    points[upper_body_indices] = rotate_points(points[upper_body_indices], angle, pivot)
    
    # Update the scatter object with the new positions.
    scat.set_offsets(points)
    return scat,

# Create the animation.
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# To show the animation window
plt.show()