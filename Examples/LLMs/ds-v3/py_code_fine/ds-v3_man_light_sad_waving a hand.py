
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the motion of a waving hand (simplified)
def update(frame):
    t = frame / num_frames * 2 * np.pi  # Normalized time
    
    # Body points (stationary or slight movement)
    body_x = np.zeros(7)
    body_y = np.linspace(-1, 0.5, 7)
    
    # Arm and hand points (waving motion)
    arm_angle = 0.5 * np.sin(t * 2)  # Waving frequency
    
    # Shoulder position (slightly moving)
    shoulder_x = 0.5 * np.sin(t * 0.2)
    shoulder_y = 0.3
    
    # Elbow position (relative to shoulder)
    elbow_rel_x = 0.4 * np.cos(arm_angle)
    elbow_rel_y = -0.4 * np.sin(arm_angle)
    elbow_x = shoulder_x + elbow_rel_x
    elbow_y = shoulder_y + elbow_rel_y
    
    # Wrist position (relative to elbow)
    wrist_rel_x = 0.3 * np.cos(arm_angle + 0.5)
    wrist_rel_y = -0.3 * np.sin(arm_angle + 0.5)
    wrist_x = elbow_x + wrist_rel_x
    wrist_y = elbow_y + wrist_rel_y
    
    # Hand points (fingers, relative to wrist)
    finger_angles = np.linspace(arm_angle - 0.3, arm_angle + 0.3, 5)
    finger_x = wrist_x + 0.1 * np.cos(finger_angles)
    finger_y = wrist_y + 0.1 * np.sin(finger_angles)
    
    # Combine all points
    x = np.concatenate([body_x, [shoulder_x, elbow_x, wrist_x], finger_x])
    y = np.concatenate([body_y, [shoulder_y, elbow_y, wrist_y], finger_y])
    
    # Update point positions
    for i, point in enumerate(points):
        point.center = (x[i], y[i])
    
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
