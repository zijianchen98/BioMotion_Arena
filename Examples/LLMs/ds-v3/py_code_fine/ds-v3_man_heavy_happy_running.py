
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize point lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define the motion paths for each point (simplified running motion)
def get_point_positions(frame):
    t = frame / num_frames * 2 * np.pi  # Time parameter
    
    # Body motion (torso)
    body_x = 0.5 * np.sin(t * 2)
    body_y = 0.1 * np.sin(t * 4)
    
    # Head
    head_x = body_x
    head_y = body_y + 0.3
    
    # Arms (left and right)
    arm_phase = np.sin(t * 4)
    left_arm_x = body_x - 0.2 - 0.1 * arm_phase
    left_arm_y = body_y + 0.2 + 0.1 * np.abs(arm_phase)
    right_arm_x = body_x + 0.2 + 0.1 * arm_phase
    right_arm_y = body_y + 0.2 + 0.1 * np.abs(arm_phase)
    
    # Hands
    left_hand_x = left_arm_x - 0.1 * np.sin(t * 4)
    left_hand_y = left_arm_y - 0.1
    right_hand_x = right_arm_x + 0.1 * np.sin(t * 4)
    right_hand_y = right_arm_y - 0.1
    
    # Legs (left and right)
    leg_phase = np.sin(t * 4)
    left_leg_x = body_x - 0.15
    left_leg_y = body_y - 0.2 - 0.2 * np.abs(leg_phase)
    right_leg_x = body_x + 0.15
    right_leg_y = body_y - 0.2 + 0.2 * np.abs(leg_phase)
    
    # Feet
    left_foot_x = left_leg_x - 0.05 * np.sin(t * 4)
    left_foot_y = left_leg_y - 0.2
    right_foot_x = right_leg_x + 0.05 * np.sin(t * 4)
    right_foot_y = right_leg_y - 0.2
    
    # Additional points for more detail (e.g., knees, elbows)
    left_knee_x = left_leg_x
    left_knee_y = (left_leg_y + body_y) / 2
    right_knee_x = right_leg_x
    right_knee_y = (right_leg_y + body_y) / 2
    
    left_elbow_x = (left_arm_x + left_hand_x) / 2
    left_elbow_y = (left_arm_y + left_hand_y) / 2
    right_elbow_x = (right_arm_x + right_hand_x) / 2
    right_elbow_y = (right_arm_y + right_hand_y) / 2
    
    # Combine all points
    x = np.array([
        head_x,
        left_arm_x, right_arm_x,
        left_hand_x, right_hand_x,
        left_elbow_x, right_elbow_x,
        body_x,
        left_leg_x, right_leg_x,
        left_knee_x, right_knee_x,
        left_foot_x, right_foot_x,
        (left_leg_x + right_leg_x) / 2  # Pelvis
    ])
    
    y = np.array([
        head_y,
        left_arm_y, right_arm_y,
        left_hand_y, right_hand_y,
        left_elbow_y, right_elbow_y,
        body_y,
        left_leg_y, right_leg_y,
        left_knee_y, right_knee_y,
        left_foot_y, right_foot_y,
        (left_leg_y + right_leg_y) / 2  # Pelvis
    ])
    
    return x, y

# Animation update function
def update(frame):
    x, y = get_point_positions(frame)
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.title('Biological Motion: Running', color='white')
plt.tight_layout()
plt.show()
