
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Define 15 point-light positions (initial stick figure pose)
points = np.array([
    [0, 2],    # Head
    [0, 1.7],  # Neck
    [0, 1.2],  # Chest
    [-0.3, 0.7], [0.3, 0.7],  # Shoulders
    [-0.5, 0], [0.5, 0],      # Elbows
    [-0.7, -0.3], [0.7, -0.3], # Wrists
    [0, 1],    # Spine
    [-0.2, 0.3], [0.2, 0.3],  # Hips
    [-0.4, -0.5], [0.4, -0.5], # Knees
    [-0.6, -1.2], [0.6, -1.2]  # Ankles
])

scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Animation function
def update(frame):
    t = frame * 0.1  # Time parameter for smooth motion
    
    # Jumping forward motion parameters
    height = 1.2 + 0.5 * np.sin(t)  # Vertical jump
    forward = 0.1 * t  # Forward movement
    leg_angle = 0.3 * np.sin(t)  # Leg swing
    arm_angle = 0.2 * np.cos(t)  # Arm swing
    
    # Update positions for realistic motion
    new_points = points.copy()
    
    # Head and torso
    new_points[0] = [forward, height + 0.3]  # Head
    new_points[1] = [forward, height + 0.1]  # Neck
    new_points[2] = [forward, height - 0.2]  # Chest
    new_points[8] = [forward, height - 0.4]  # Spine
    
    # Shoulders
    new_points[3] = [forward - 0.3, height - 0.3]  # Left shoulder
    new_points[4] = [forward + 0.3, height - 0.3]  # Right shoulder
    
    # Arms
    new_points[5] = [forward - 0.5 + arm_angle, height - 0.8]  # Left elbow
    new_points[6] = [forward + 0.5 - arm_angle, height - 0.8]  # Right elbow
    new_points[7] = [forward - 0.7 + 1.5 * arm_angle, height - 1.2]  # Left wrist
    new_points[9] = [forward + 0.7 - 1.5 * arm_angle, height - 1.2]  # Right wrist
    
    # Hips
    new_points[9] = [forward - 0.2, height - 0.7]  # Left hip
    new_points[10] = [forward + 0.2, height - 0.7]  # Right hip
    
    # Legs
    new_points[11] = [forward - 0.4 + leg_angle, height - 1.2]  # Left knee
    new_points[12] = [forward + 0.4 - leg_angle, height - 1.2]  # Right knee
    new_points[13] = [forward - 0.6 + 2 * leg_angle, height - 1.7]  # Left ankle
    new_points[14] = [forward + 0.6 - 2 * leg_angle, height - 1.7]  # Right ankle
    
    scatter.set_offsets(new_points)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
