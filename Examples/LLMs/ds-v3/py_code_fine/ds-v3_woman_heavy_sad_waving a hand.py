
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

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
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the motion of a sad woman with heavy weight waving a hand
def update(frame):
    t = frame / num_frames * 2 * np.pi  # Time parameter
    
    # Body points (torso, head, legs)
    # Torso and head
    body_x = np.zeros(5)
    body_y = np.linspace(-1, 0.5, 5)
    
    # Legs (slightly apart, heavy weight)
    legs_x = np.array([-0.2, 0.2, -0.3, 0.3])
    legs_y = np.array([-1.5, -1.5, -1.8, -1.8])
    
    # Arms (one arm waving)
    # Right arm (waving)
    arm_angle = np.pi/4 * np.sin(t * 2)  # Waving motion
    arm_length = 0.7
    upper_arm_x = 0.5 * np.cos(arm_angle + np.pi/2)
    upper_arm_y = 0.2 + 0.5 * np.sin(arm_angle + np.pi/2)
    lower_arm_x = upper_arm_x + 0.4 * np.cos(arm_angle * 1.5 - np.pi/4)
    lower_arm_y = upper_arm_y + 0.4 * np.sin(arm_angle * 1.5 - np.pi/4)
    
    # Left arm (hanging, slightly bent due to heavy weight)
    left_upper_arm_x = -0.5
    left_upper_arm_y = 0.2
    left_lower_arm_x = -0.5
    left_lower_arm_y = -0.3
    
    # Combine all points
    x_coords = np.concatenate([
        [0],  # head
        body_x,
        legs_x,
        [0.5, upper_arm_x, lower_arm_x],  # right arm
        [-0.5, left_upper_arm_x, left_lower_arm_x]  # left arm
    ])
    y_coords = np.concatenate([
        [0.7],  # head
        body_y,
        legs_y,
        [0.2, upper_arm_y, lower_arm_y],  # right arm
        [0.2, left_upper_arm_y, left_lower_arm_y]  # left arm
    ])
    
    # Ensure we have exactly 15 points
    x_coords = x_coords[:num_points]
    y_coords = y_coords[:num_points]
    
    # Update point positions
    for i, point in enumerate(points):
        point.center = (x_coords[i], y_coords[i])
    
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
