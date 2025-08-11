
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Time steps
frames = 100
t = np.linspace(0, 2 * np.pi, frames)

# Define the motion of each point-light
def get_positions(t_frame):
    # Main body motion (vertical oscillation for jumping)
    body_y = 0.5 * np.sin(t_frame)  # Vertical movement
    body_x = 0.3 * t_frame / (2 * np.pi)  # Slight forward drift
    
    # Head (stationary relative to body)
    head_x = body_x
    head_y = body_y + 0.7
    
    # Shoulders (slightly moving with body)
    shoulder_left_x = body_x - 0.3
    shoulder_left_y = body_y + 0.5
    shoulder_right_x = body_x + 0.3
    shoulder_right_y = body_y + 0.5
    
    # Elbows (moving with arms)
    elbow_left_x = body_x - 0.3 - 0.2 * np.sin(t_frame * 2)
    elbow_left_y = body_y + 0.3 - 0.1 * np.sin(t_frame * 2)
    elbow_right_x = body_x + 0.3 + 0.2 * np.sin(t_frame * 2)
    elbow_right_y = body_y + 0.3 - 0.1 * np.sin(t_frame * 2)
    
    # Hands (moving more than elbows)
    hand_left_x = elbow_left_x - 0.2 * np.sin(t_frame * 2 + 0.5)
    hand_left_y = elbow_left_y - 0.2 * np.cos(t_frame * 2 + 0.5)
    hand_right_x = elbow_right_x + 0.2 * np.sin(t_frame * 2 + 0.5)
    hand_right_y = elbow_right_y - 0.2 * np.cos(t_frame * 2 + 0.5)
    
    # Hips (stationary relative to body)
    hip_left_x = body_x - 0.2
    hip_left_y = body_y
    hip_right_x = body_x + 0.2
    hip_right_y = body_y
    
    # Knees (moving with legs)
    knee_left_x = body_x - 0.2
    knee_left_y = body_y - 0.4 + 0.2 * np.sin(t_frame * 2)
    knee_right_x = body_x + 0.2
    knee_right_y = body_y - 0.4 + 0.2 * np.sin(t_frame * 2)
    
    # Feet (moving more than knees)
    foot_left_x = knee_left_x - 0.1 * np.sin(t_frame * 2 + 0.3)
    foot_left_y = knee_left_y - 0.3 + 0.1 * np.sin(t_frame * 2 + 0.3)
    foot_right_x = knee_right_x + 0.1 * np.sin(t_frame * 2 + 0.3)
    foot_right_y = knee_right_y - 0.3 + 0.1 * np.sin(t_frame * 2 + 0.3)
    
    # Combine all points
    x = np.array([
        head_x,
        shoulder_left_x, shoulder_right_x,
        elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x,
        hip_left_x, hip_right_x,
        knee_left_x, knee_right_x,
        foot_left_x, foot_right_x,
        body_x,  # Additional point for the torso
        body_x + 0.1 * np.sin(t_frame)  # Extra point for variation
    ])
    
    y = np.array([
        head_y,
        shoulder_left_y, shoulder_right_y,
        elbow_left_y, elbow_right_y,
        hand_left_y, hand_right_y,
        hip_left_y, hip_right_y,
        knee_left_y, knee_right_y,
        foot_left_y, foot_right_y,
        body_y - 0.1,
        body_y + 0.1 * np.cos(t_frame)
    ])
    
    return x, y

# Animation function
def update(frame):
    t_frame = t[frame]
    x, y = get_positions(t_frame)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.tight_layout()
plt.show()
