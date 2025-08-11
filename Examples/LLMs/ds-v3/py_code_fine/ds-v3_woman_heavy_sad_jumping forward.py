
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define keyframes for the jumping motion (simplified)
# Each keyframe is a (x, y) position for each of the 15 points
# Here, we'll define positions for a few keyframes and interpolate

# Keyframes: 0 (start), positions1 (mid-jump), positions2 (landing)
# These are rough estimates; for a realistic motion, more keyframes or physics would be needed
def get_keyframe(t):
    # t is a parameter between 0 and 1 for the jump cycle
    # We'll model a sad, heavy jump: slower ascent, faster descent, less height
    
    # Body parts: head, shoulders, elbows, hands, hips, knees, feet
    # Coordinates are relative to the body's center
    
    # Body center movement: parabolic jump
    jump_height = 0.5  # Lower jump for heavy person
    body_y = -jump_height * (t - 0.5)**2 + jump_height/4  # Centered parabola
    
    # Body lean (sad posture: forward lean)
    lean = 0.2 * np.sin(np.pi * t)  # Oscillates forward during jump
    
    # Key points (simplified)
    head_x = 0.0 + lean
    head_y = 0.7 + body_y
    
    shoulder_x = 0.0 + lean
    shoulder_y = 0.5 + body_y
    
    elbow_left_x = -0.2 + lean
    elbow_right_x = 0.2 + lean
    elbow_y = 0.4 + body_y
    
    hand_left_x = -0.3 + lean - 0.1 * np.sin(2 * np.pi * t)
    hand_right_x = 0.3 + lean + 0.1 * np.sin(2 * np.pi * t)
    hand_y = 0.2 + body_y
    
    hip_x = -0.1 + lean
    hip_y = 0.0 + body_y
    
    knee_left_x = -0.1 + lean
    knee_right_x = 0.1 + lean
    knee_y = -0.3 + body_y
    
    foot_left_x = -0.1 + lean - 0.05 * np.sin(2 * np.pi * t)
    foot_right_x = 0.1 + lean + 0.05 * np.sin(2 * np.pi * t)
    foot_y = -0.6 + body_y
    
    # Combine all points
    x = np.array([
        head_x, 
        shoulder_x, 
        elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x,
        hip_x,
        knee_left_x, knee_right_x,
        foot_left_x, foot_right_x,
        # Additional points for more detail (e.g., mid-spine, etc.)
        shoulder_x - 0.05, shoulder_x + 0.05,
        hip_x - 0.05, hip_x + 0.05
    ])
    
    y = np.array([
        head_y,
        shoulder_y,
        elbow_y, elbow_y,
        hand_y, hand_y,
        hip_y,
        knee_y, knee_y,
        foot_y, foot_y,
        shoulder_y - 0.1, shoulder_y - 0.1,
        hip_y + 0.1, hip_y + 0.1
    ])
    
    return x, y

# Animation update
def update(frame):
    t = (frame % 30) / 30  # Loop every 30 frames
    x, y = get_keyframe(t)
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=50, blit=True)

plt.tight_layout()
plt.show()
