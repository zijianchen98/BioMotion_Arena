
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define 15 point-light positions for a walking human figure (initial pose)
# Based on biomechanical plausibility: head, shoulders, elbows, wrists, hips, knees, ankles
points = np.array([
    [0, 0.8],  # head
    [-0.2, 0.6], [0.2, 0.6],  # shoulders
    [-0.4, 0.4], [0.4, 0.4],  # elbows
    [-0.6, 0.2], [0.6, 0.2],  # wrists
    [-0.1, 0.0], [0.1, 0.0],  # hips
    [-0.2, -0.4], [0.2, -0.4],  # knees
    [-0.3, -0.8], [0.3, -0.8]  # ankles
])

# Scatter plot for point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Animation function
def update(frame):
    # Simulate walking motion with biomechanical plausibility
    # Phase for walking cycle (0 to 2π)
    t = frame * 0.1
    leg_phase = np.sin(t)
    arm_phase = np.cos(t)
    
    # Update positions for natural walking
    new_points = points.copy()
    
    # Head and torso slight vertical movement
    new_points[0, 1] += 0.05 * np.sin(t * 0.5)  # head bobbing
    
    # Arms swinging
    new_points[2, 0] = -0.4 + 0.2 * arm_phase  # left elbow
    new_points[3, 0] = 0.4 - 0.2 * arm_phase   # right elbow
    new_points[4, 0] = -0.6 + 0.3 * arm_phase  # left wrist
    new_points[5, 0] = 0.6 - 0.3 * arm_phase   # right wrist
    
    # Legs moving (exaggerated for heavy weight)
    new_points[6, 0] = -0.2 + 0.3 * leg_phase  # left knee
    new_points[7, 0] = 0.2 - 0.3 * leg_phase   # right knee
    new_points[8, 0] = -0.3 + 0.4 * leg_phase  # left ankle
    new_points[9, 0] = 0.3 - 0.4 * leg_phase   # right ankle
    
    # Update scatter points
    scatter.set_offsets(new_points)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
