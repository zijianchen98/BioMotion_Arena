
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60  # Frames per animation cycle
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
plt.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define key points for a waving motion (simplified)
def get_positions(frame):
    t = frame / num_frames * 2 * np.pi  # Normalized time
    # Body points (torso, head, legs)
    body_x = np.zeros(5)
    body_y = np.linspace(-1.5, 0.5, 5)
    
    # Arm waving (right arm)
    arm_angle = 0.5 * np.sin(t * 2) * np.pi/3  # Waving angle
    # Shoulder position (right)
    shoulder_x, shoulder_y = 0.5, 0.3
    # Elbow position (relative to shoulder)
    elbow_rel_x = 0.5 * np.cos(arm_angle)
    elbow_rel_y = 0.5 * np.sin(arm_angle)
    elbow_x = shoulder_x + elbow_rel_x
    elbow_y = shoulder_y + elbow_rel_y
    # Hand position (relative to elbow)
    hand_rel_x = 0.4 * np.cos(arm_angle + np.pi/4)
    hand_rel_y = 0.4 * np.sin(arm_angle + np.pi/4)
    hand_x = elbow_x + hand_rel_x
    hand_y = elbow_y + hand_rel_y
    
    # Left arm (static)
    l_shoulder_x, l_shoulder_y = -0.5, 0.3
    l_elbow_x, l_elbow_y = -0.5, 0.0
    l_hand_x, l_hand_y = -0.5, -0.3
    
    # Legs (static)
    hip_x, hip_y = 0.0, -0.5
    r_knee_x, r_knee_y = 0.2, -1.0
    r_foot_x, r_foot_y = 0.2, -1.5
    l_knee_x, l_knee_y = -0.2, -1.0
    l_foot_x, l_foot_y = -0.2, -1.5
    
    # Combine all points
    x = np.array([
        body_x[0], body_x[1], body_x[2], body_x[3], body_x[4],  # Body/head
        shoulder_x, elbow_x, hand_x,  # Right arm
        l_shoulder_x, l_elbow_x, l_hand_x,  # Left arm
        hip_x, r_knee_x, r_foot_x, l_knee_x, l_foot_x  # Legs
    ])
    y = np.array([
        body_y[0], body_y[1], body_y[2], body_y[3], body_y[4],
        shoulder_y, elbow_y, hand_y,
        l_shoulder_y, l_elbow_y, l_hand_y,
        hip_y, r_knee_y, r_foot_y, l_knee_y, l_foot_y
    ])
    
    return x[:num_points], y[:num_points]  # Ensure only 15 points

def update(frame):
    x, y = get_positions(frame)
    for i, point in enumerate(points):
        point.center = (x[i], y[i])
    return points

ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)
plt.title('Biological Motion: Happy Woman Waving', color='white')
plt.show()
