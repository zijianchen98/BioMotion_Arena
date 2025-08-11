
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of points
num_points = 15

# Define the points for a lying down person (sadman with heavy weight)
# Points are defined relative to a central point (torso)
# Points order: head, neck, left shoulder, left elbow, left hand, right shoulder, right elbow, right hand,
#               torso, left hip, left knee, left foot, right hip, right knee, right foot

# Initial positions (lying down, slightly curved to show heaviness)
initial_positions = np.array([
    [0.0, 0.6],    # head
    [0.0, 0.4],    # neck
    [-0.3, 0.3],   # left shoulder
    [-0.5, 0.1],   # left elbow
    [-0.6, -0.1],  # left hand
    [0.3, 0.3],    # right shoulder
    [0.5, 0.1],    # right elbow
    [0.6, -0.1],   # right hand
    [0.0, 0.2],    # torso (center)
    [-0.2, -0.2],  # left hip
    [-0.3, -0.5],  # left knee
    [-0.3, -0.8],  # left foot
    [0.2, -0.2],   # right hip
    [0.3, -0.5],   # right knee
    [0.3, -0.8]    # right foot
])

# Create point markers
points = ax.scatter([], [], color='white', s=50)

# Create lines to connect points (optional, for better visualization)
lines = LineCollection([], colors='white', linewidths=1)
ax.add_collection(lines)

# Define connections between points for lines (indices refer to initial_positions)
connections = [
    (0, 1),    # head to neck
    (1, 2),    # neck to left shoulder
    (2, 3),    # left shoulder to left elbow
    (3, 4),    # left elbow to left hand
    (1, 5),    # neck to right shoulder
    (5, 6),    # right shoulder to right elbow
    (6, 7),    # right elbow to right hand
    (1, 8),    # neck to torso
    (8, 9),    # torso to left hip
    (9, 10),   # left hip to left knee
    (10, 11),  # left knee to left foot
    (8, 12),   # torso to right hip
    (12, 13),  # right hip to right knee
    (13, 14)   # right knee to right foot
]

# Animation function to simulate slight movement (breathing/heavy weight)
def update(frame):
    t = frame * 0.1
    # Slight vertical movement for breathing effect
    breathing = 0.02 * np.sin(t * 2)
    # Slight adjustments to limbs to simulate heaviness
    limb_movement = 0.01 * np.sin(t * 3)
    
    # Modify initial positions with breathing and limb movement
    current_positions = initial_positions.copy()
    # Torso and head move slightly up and down
    current_positions[0:2, 1] += breathing  # head and neck
    current_positions[8, 1] += breathing    # torso
    # Arms and legs move slightly
    current_positions[2:8, :] += limb_movement * 0.5  # arms
    current_positions[9:, :] += limb_movement * 0.3   # legs
    
    # Update point positions
    points.set_offsets(current_positions)
    
    # Update lines if needed
    segments = []
    for i, end in connections:
        segments.append([current_positions[i], current_positions[end]])
    lines.set_segments(segments)
    
    return points, lines

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.tight_layout()
plt.show()
