
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = ax.scatter([], [], color='white', s=50)

# Define the key points for a lying down person (simplified)
# Coordinates are relative to the center of the body
def get_body_points(t):
    # Time parameter t is in radians (0 to 2pi for a full cycle)
    # The body is lying horizontally, so y-coordinates are mostly static
    # We'll add some slight movement to simulate breathing
    
    # Main body parts
    head_x = 0.8 * np.sin(t * 0.5)  # slight side-to-side movement
    head_y = 0.1 * np.sin(t * 2)    # slight up-down (breathing)
    
    shoulders_x = 0.5 * np.sin(t * 0.3)
    shoulders_y = 0.05 * np.sin(t * 2)
    
    hips_x = -0.5 * np.sin(t * 0.3)
    hips_y = 0.05 * np.sin(t * 2 + 0.5)
    
    # Limbs will have more movement
    # Arms
    left_arm_angle = math.pi/4 * np.sin(t) - math.pi/4
    right_arm_angle = math.pi/4 * np.sin(t + math.pi) - math.pi/4
    
    left_elbow_x = shoulders_x - 0.3 * np.cos(left_arm_angle)
    left_elbow_y = shoulders_y - 0.3 * np.sin(left_arm_angle)
    
    right_elbow_x = shoulders_x + 0.3 * np.cos(right_arm_angle)
    right_elbow_y = shoulders_y - 0.3 * np.sin(right_arm_angle)
    
    left_hand_x = left_elbow_x - 0.25 * np.cos(left_armangle * 1.5)
    left_hand_y = left_elbow_y - 0.25 * np.sin(left_armangle * 1.5)
    
    right_hand_x = right_elbow_x + 0.25 * np.cos(right_armangle * 1.5)
    right_hand_y = right_elbow_y - 0.25 * np.sin(right_armangle * 1.5)
    
    # Legs
    left_leg_angle = math.pi/6 * np.sin(t + 0.5) - math.pi/6
    right_leg_angle = math.pi/6 * np.sin(t + 0.5 + math.pi) - math.pi/6
    
    left_knee_x = hips_x - 0.35 * np.cos(left_leg_angle)
    left_knee_y = hips_y - 0.35 * np.sin(left_leg_angle)
    
    right_knee_x = hips_x + 0.35 * np.cos(right_leg_angle)
    right_knee_y = hips_y - 0.35 * np.sin(right_leg_angle)
    
    left_foot_x = left_knee_x - 0.4 * np.cos(left_leg_angle * 0.8)
    left_foot_y = left_knee_y - 0.4 * np.sin(left_leg_angle * 0.8)
    
    right_foot_x = right_knee_x + 0.4 * np.cos(right_leg_angle * 0.8)
    right_foot_y = right_knee_y - 0.4 * np.sin(right_leg_angle * 0.8)
    
    # Additional points for more detail
    chest_x = (shoulders_x + hips_x) / 2
    chest_y = (shoulders_y + hips_y) / 2
    
    # Return all 15 points in order
    return np.array([
        [head_x, head_y + 0.1],            # head
        [shoulders_x - 0.1, shoulders_y],  # left shoulder
        [shoulders_x + 0.1, shoulders_y],  # right shoulder
        [left_elbow_x, left_elbow_y],      # left elbow
        [right_elbow_x, right_elbow_y],    # right elbow
        [left_hand_x, left_hand_y],        # left hand
        [right_hand_x, right_hand_y],      # right hand
        [chest_x, chest_y],                # chest
        [hips_x - 0.1, hips_y],            # left hip
        [hips_x + 0.1, hips_y],            # right hip
        [left_knee_x, left_knee_y],        # left knee
        [right_knee_x, right_knee_y],      # right knee
        [left_foot_x, left_foot_y],        # left foot
        [right_foot_x, right_foot_y],      # right foot
        [hips_x, hips_y - 0.05]            # pelvis
    ])

# Animation update function
def update(frame):
    t = frame * 0.1
    body_points = get_body_points(t)
    points.set_offsets(body_points)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.tight_layout()
plt.show()
