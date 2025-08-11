
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define keyframes for the jumping motion
def get_keyframe(t):
    # Time is normalized between 0 and 1 for one jump cycle
    t = t % 1.0
    
    # Key positions for the points (simplified jumping motion)
    # Points are ordered as: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2), torso (1)
    
    # Vertical positions (y-coordinates)
    # The jump has a parabolic trajectory for the body's vertical movement
    body_phase = np.sin(t * 2 * np.pi)  # Oscillates between -1 and 1
    body_y = 0.5 * body_phase + 1.0  # Center around 1.0, range [0.5, 1.5]
    
    # Head
    head_x = 0.0
    head_y = body_y + 0.3
    
    # Shoulders
    shoulder_y = body_y + 0.2
    shoulder_left_x = -0.2
    shoulder_right_x = 0.2
    
    # Elbows (arms are moving during jump)
    elbow_left_x = -0.25 - 0.1 * np.sin(t * 4 * np.pi)
    elbow_right_x = 0.25 + 0.1 * np.sin(t * 4 * np.pi)
    elbow_y = body_y + 0.1
    
    # Hands (follow elbows with some lag)
    hand_left_x = elbow_left_x - 0.15 - 0.05 * np.sin(t * 4 * np.pi + np.pi/4)
    hand_right_x = elbow_right_x + 0.15 + 0.05 * np.sin(t * 4 * np.pi + np.pi/4)
    hand_y = body_y - 0.1
    
    # Hips
    hip_left_x = -0.15
    hip_right_x = 0.15
    hip_y = body_y
    
    # Knees (legs bend during jump)
    knee_left_x = -0.15
    knee_right_x = 0.15
    knee_y = body_y - 0.3 - 0.1 * np.sin(t * 2 * np.pi + np.pi/2)
    
    # Feet (follow knees)
    foot_left_x = -0.15
    foot_right_x = 0.15
    foot_y = body_y - 0.6 -  # Feet move more during jump
    if t < 0.5:
        foot_y = body_y - 0.6 + 0.3 * np.sin(t * 2 * np.pi)
    else:
        foot_y = body_y - 0.6
    
    # Torso (midpoint between shoulders and hips)
    torso_x = 0.0
    torso_y = (shoulder_y + hip_y) / 2
    
    # Combine all points
    x_coords = [
        head_x,
        shoulder_left_x, shoulder_right_x,
        elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x,
        hip_left_x, hip_right_x,
        knee_left_x, knee_right_x,
        foot_left_x, foot_right_x,
        torso_x
    ]
    
    y_coords = [
        head_y,
        shoulder_y, shoulder_y,
        elbow_y, elbow_y,
        hand_y, hand_y,
        hip_y, hip_y,
        knee_y, knee_y,
        foot_y, foot_y,
        torso_y
    ]
    
    return x_coords, y_coords

# Animation update function
def update(frame):
    t = frame / 30  # 30 frames per second
    x_coords, y_coords = get_keyframe(t)
    points.set_data(x_coords, y_coords)
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=30, interval=50, blit=True
)

plt.tight_layout()
plt.show()
