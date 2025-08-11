
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the keyframes for the bowing motion
def get_keyframes():
    # Keyframes for each point (x, y) over time
    # The points are roughly representing head, shoulders, elbows, hands, hips, knees, feet
    # The motion is simplified for a bowing action
    
    # Time steps
    t = np.linspace(0, 2 * np.pi, 100)
    
    # Head
    head_x = 0.0 * np.ones_like(t)
    head_y = 1.5 + 0.3 * np.sin(t)
    
    # Shoulders (left and right)
    shoulder_l_x = -0.3 * np.ones_like(t)
    shoulder_r_x = 0.3 * np.ones_like(t)
    shoulder_y = 1.2 + 0.2 * np.sin(t)
    
    # Elbows (left and right)
    elbow_l_x = -0.4 + 0.1 * np.sin(t)
    elbow_r_x = 0.4 - 0.1 * np.sin(t)
    elbow_y = 1.0 + 0.3 * np.sin(t)
    
    # Hands (left and right)
    hand_l_x = -0.5 + 0.1 * np.sin(t)
    hand_r_x = 0.5 - 0.1 * np.sin(t)
    hand_y = 0.8 + 0.4 * np.sin(t)
    
    # Hips (left and right)
    hip_l_x = -0.2 * np.ones_like(t)
    hip_r_x = 0.2 * np.ones_like(t)
    hip_y = 0.7 - 0.1 * np.sin(t)
    
    # Knees (left and right)
    knee_l_x = -0.2 * np.sin(t) * 0.1
    knee_r_x = 0.2 * np.sin(t) * 0.1
    knee_y = 0.3 - 0.2 * np.sin(t)
    
    # Feet (left and right)
    foot_l_x = -0.2 * np.ones_like(t)
    foot_r_x = 0.2 * np.ones_like(t)
    foot_y = 0.0 * np.ones_like(t)
    
    # Spine points (additional points for smoothness)
    spine1_x = 0.0 * np.ones_like(t)
    spine1_y = 1.0 + 0.25 * np.sin(t)
    
    spine2_x = 0.0 * np.ones_like(t)
    spine2_y = 0.5 - 0.15 * np.sin(t)
    
    # Combine all points' trajectories
    trajectories = np.array([
        [head_x, head_y],  # 0: head
        [shoulder_l_x, shoulder_y],  # 1: left shoulder
        [shoulder_r_x, shoulder_y],  # 2: right shoulder
        [elbow_l_x, elbow_y],  # 3: left elbow
        [elbow_r_x, elbow_y],  # 4: right elbow
        [hand_l_x, hand_y],  # 5: left hand
        [hand_r_x, hand_y],  # 6: right hand
        [hip_l_x, hip_y],  # 7: left hip
        [hip_r_x, hip_y],  # 8: right hip
        [knee_l_x, knee_y],  # 9: left knee
        [knee_r_x, knee_y],  # 10: right knee
        [foot_l_x, foot_y],  # 11: left foot
        [foot_r_x, foot_y],  # 12: right foot
        [spine1_x, spine1_y],  # 13: spine1
        [spine2_x, spine2_y],  # 14: spine2
    ])
    
    return trajectories

trajectories = get_keyframes()

# Animation update function
def update(frame):
    for i, point in enumerate(points):
        point.set_center((trajectories[i, 0, frame], trajectories[i, 1, frame]))
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=len(trajectories[0, 0]), interval=50, blit=True)

plt.title('Biological Motion: Bowing', color='white')
plt.show()
