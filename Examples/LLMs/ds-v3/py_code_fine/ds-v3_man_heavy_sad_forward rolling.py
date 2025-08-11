
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')

# Number of points
num_points = 15

# Initialize point positions (x, y)
points = np.zeros((num_points, 2))
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Parameters for the rolling motion
radius = 0.5  # Radius of the body's rolling motion
body_length = 1.5  # Length of the body (head to feet)
arm_length = 0.6  # Length of the arms
leg_length = 0.7  # Length of the legs
time_step = 0.05  # Time step for animation frame

# Points layout:
# 0: Head
# 1-2: Shoulders
# 3-4: Elbows
# 5-6: Hands
# 7: Torso
# 8-9: Hips
# 10-11: Knees
# 12-13: Feet
# 14: Mid-body (for rolling effect)

def update(frame):
    t = frame * time_step
    # The body rolls forward in a circular path
    angle = t * np.pi  # Angle for rolling motion
    
    # Center of the rolling body
    center_x = np.sin(angle) * radius
    center_y = 1.5 - np.cos(angle) * radius
    
    # Head (point 0)
    head_x = center_x
    head_y = center_y + 0.2 * np.cos(angle)
    
    # Torso (point 7)
    torso_x = center_x
    torso_y = center_y - 0.3 * np.cos(angle)
    
    # Shoulders (points 1-2)
    shoulder_width = 0.4
    shoulder1_x = center_x - shoulder_width * np.cos(angle)
    shoulder1_y = center_y + 0.1 * np.cos(angle)
    shoulder2_x = center_x + shoulder_width * np.cos(angle)
    shoulder2_y = center_y + 0.1 * np.cos(angle)
    
    # Elbows (points 3-4)
    elbow_offset = 0.3
    elbow1_x = shoulder1_x - elbow_offset * np.cos(angle + np.pi/4)
    elbow1_y = shoulder1_y - elbow_offset * np.sin(angle + np.pi/4)
    elbow2_x = shoulder2_x + elbow_offset * np.cos(angle + np.pi/4)
    elbow2_y = shoulder2_y - elbow_offset * np.sin(angle + np.pi/4)
    
    # Hands (points 5-6)
    hand_offset = 0.3
    hand1_x = elbow1_x - hand_offset * np.cos(angle + np.pi/3)
    hand1_y = elbow1_y - hand_offset * np.sin(angle + np.pi/3)
    hand2_x = elbow2_x + hand_offset * np.cos(angle + np.pi/3)
    hand2_y = elbow2_y - hand_offset * np.sin(angle + np.pi/3)
    
    # Hips (points 8-9)
    hip_width = 0.3
    hip1_x = center_x - hip_width * np.cos(angle)
    hip1_y = center_y - 0.5 * np.cos(angle)
    hip2_x = center_x + hip_width * np.cos(angle)
    hip2_y = center_y - 0.5 * np.cos(angle)
    
    # Knees (points 10-11)
    knee_offset = 0.3
    knee1_x = hip1_x - knee_offset * np.cos(angle - np.pi/6)
    knee1_y = hip1_y - knee_offset * np.sin(angle - np.pi/6)
    knee2_x = hip2_x + knee_offset * np.cos(angle - np.pi/6)
    knee2_y = hip2_y - knee_offset * np.sin(angle - np.pi/6)
    
    # Feet (points 12-13)
    foot_offset = 0.3
    foot1_x = knee1_x - foot_offset * np.cos(angle - np.pi/4)
    foot1_y = knee1_y - foot_offset * np.sin(angle - np.pi/4)
    foot2_x = knee2_x + foot_offset * np.cos(angle - np.pi/4)
    foot2_y = knee2_y - foot_offset * np.sin(angle - np.pi/4)
    
    # Mid-body point (point 14)
    mid_x = center_x
    mid_y = center_y - 0.1 * np.cos(angle)
    
    # Update all points
    points[0] = [head_x, head_y]  # Head
    points[1] = [shoulder1_x, shoulder1_y]  # Shoulder 1
    points[2] = [shoulder2_x, shoulder2_y]  # Shoulder 2
    points[3] = [elbow1_x, elbow1_y]  # Elbow 1
    points[4] = [elbow2_x, elbow2_y]  # Elbow 2
    points[5] = [hand1_x, hand1_y]  # Hand 1
    points[6] = [hand2_x, hand2_y]  # Hand 2
    points[7] = [torso_x, torso_y]  # Torso
    points[8] = [hip1_x, hip1_y]  # Hip 1
    points[9] = [hip2_x, hip2_y]  # Hip 2
    points[10] = [knee1_x, knee1_y]  # Knee 1
    points[11] = [knee2_x, knee2_y]  # Knee 2
    points[12] = [foot1_x, foot1_y]  # Foot 1
    points[13] = [foot2_x, foot2_y]  # Foot 2
    points[14] = [mid_x, mid_y]  # Mid-body
    
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.tight_layout()
plt.show()
