
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection

# Parameters
num_points = 15
frames = 100
radius = 1.0
height = 2.0
speed = 0.1

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Initialize point positions (simplified model of a person)
# Points: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2), torso (1), center (1)
points = np.zeros((num_points, 2))
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Lines to connect points (optional for better visualization)
lines = [
    [0, 1], [0, 2],  # head to shoulders
    [1, 3], [2, 4],  # shoulders to elbows
    [3, 5], [4, 6],  # elbows to hands
    [1, 7], [2, 8],  # shoulders to hips
    [7, 9], [8, 10], # hips to knees
    [9, 11], [10, 12], # knees to feet
    [1, 2], [7, 8],  # shoulders and hips connections
    [13, 1], [13, 2], [13, 7], [13, 8]  # torso/center connections
]
line_segments = LineCollection([], colors='white', linewidths=1)
ax.add_collection(line_segments)

def update(frame):
    angle = frame * speed
    
    # Head (0)
    points[0] = [0, height]
    
    # Shoulders (1, 2)
    shoulder_width = 0.5
    points[1] = [-shoulder_width * np.cos(angle), height - 0.2]
    points[2] = [shoulder_width * np.cos(angle), height - 0.2]
    
    # Elbows (3, 4)
    elbow_angle = angle + np.pi/4
    points[3] = points[1] + [ -0.3 * np.cos(elbow_angle), -0.3 * np.sin(elbow_angle) ]
    points[4] = points[2] + [ 0.3 * np.cos(elbow_angle), -0.3 * np.sin(elbow_angle) ]
    
    # Hands (5, 6)
    hand_angle = angle + np.pi/2
    points[5] = points[3] + [ -0.2 * np.cos(hand_angle), -0.2 * np.sin(hand_angle) ]
    points[6] = points[4] + [ 0.2 * np.cos(hand_angle), -0.2 * np.sin(hand_angle) ]
    
    # Hips (7, 8)
    hip_width = 0.6
    points[7] = [-hip_width * np.cos(angle), height - 0.8]
    points[8] = [hip_width * np.cos(angle), height - 0.8]
    
    # Knees (9, 10)
    knee_angle = angle + np.pi/6
    points[9] = points[7] + [ -0.2 * np.cos(knee_angle), -0.5 * np.sin(knee_angle) ]
    points[10] = points[8] + [ 0.2 * np.cos(knee_angle), -0.5 * np.sin(knee_angle) ]
    
    # Feet (11, 12)
    foot_angle = angle + np.pi/3
    points[11] = points[9] + [ -0.1 * np.cos(foot_angle), -0.2 * np.sin(foot_angle) ]
    points[12] = points[10] + [ 0.1 * np.cos(foot_angle), -0.2 * np.sin(foot_angle) ]
    
    # Torso/Center (13)
    points[13] = [0, height - 0.5]
    
    # Update scatter plot
    scatter.set_offsets(points)
    
    # Update lines
    segments = []
    for line in lines:
        segments.append([points[line[0]], points[line[1]]])
    line_segments.set_segments(segments)
    
    return scatter, line_segments

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=False)
plt.tight_layout()
plt.show()
