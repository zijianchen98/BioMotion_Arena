
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = ax.scatter([], [], color='white', s=50)

# Define the key points of the body (approximate positions for a forward roll)
# These are relative to the center of mass which will move in a rolling motion
body_points_relative = {
    'head': (0, 0.6),
    'shoulder_left': (-0.3, 0.3),
    'shoulder_right': (0.3, 0.3),
    'elbow_left': (-0.5, 0.2),
    'elbow_right': (0.5, 0.2),
    'hand_left': (-0.6, 0.0),
    'hand_right': (0.6, 0.0),
    'hip_left': (-0.2, -0.3),
    'hip_right': (0.2, -0.3),
    'knee_left': (-0.3, -0.6),
    'knee_right': (0.3, -0.6),
    'ankle_left': (-0.2, -0.9),
    'ankle_right': (0.2, -0.9),
    'toe_left': (-0.3, -1.0),
    'toe_right': (0.3, -1.0)
}

# Convert to a list for easier manipulation
point_names = list(body_points_relative.keys())
initial_relative_positions = np.array([body_points_relative[name] for name in point_names])

# Animation parameters
duration = 5  # seconds
fps = 30
total_frames = duration * fps
roll_radius = 0.5  # Approximate radius of the body's roll

def update(frame):
    # Calculate the progress through the roll (0 to 2*pi for a full roll)
    progress = (frame / total_frames) * 2 * math.pi
    
    # Center of mass moves in a circular path (rolling forward)
    com_x = progress * roll_radius - roll_radius
    com_y = roll_radius  # The y-coordinate remains constant for a simple roll
    
    # Rotate the body points around the center of mass to simulate the roll
    rotation_angle = -progress  # Negative because the body rolls forward
    
    # Rotation matrix
    cos_theta = math.cos(rotation_angle)
    sin_theta = math.sin(rotation_angle)
    
    rotated_positions = np.zeros_like(initial_relative_positions)
    for i, (x, y) in enumerate(initial_relative_positions):
        rotated_x = x * cos_theta - y * sin_theta
        rotated_y = x * sin_theta + y * cos_theta
        rotated_positions[i] = [rotated_x, rotated_y]
    
    # Translate to the center of mass position
    positions = rotated_positions + np.array([com_x, com_y])
    
    # Update the scatter plot data
    points.set_offsets(positions)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
