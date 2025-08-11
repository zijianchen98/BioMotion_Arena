
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Time steps
frames = 100
t = np.linspace(0, 2 * np.pi, frames)

# Define the motion of each point-light
def get_point_positions(t_frame):
    # Main body points (head, shoulders, torso)
    head_x = 0
    head_y = 0.8 + 0.1 * np.sin(t_frame * 2)  # slight bobbing
    
    shoulder_left_x = -0.3
    shoulder_left_y = 0.5 + 0.05 * np.sin(t_frame * 2 + 0.5)
    
    shoulder_right_x = 0.3
    shoulder_right_y = 0.5 + 0.05 * np.sin(t_frame * 2 + 0.5)
    
    torso_x = 0
    torso_y = 0.2 + 0.05 * np.sin(t_frame * 2 + 0.3)
    
    # Arms (elbows and hands)
    elbow_left_x = -0.4 - 0.1 * np.sin(t_frame * 3)
    elbow_left_y = 0.3 - 0.1 * np.sin(t_frame * 2)
    
    elbow_right_x = 0.4 + 0.1 * np.sin(t_frame * 3)
    elbow_right_y = 0.3 - 0.1 * np.sin(t_frame * 2)
    
    hand_left_x = -0.5 - 0.1 * np.sin(t_frame * 3 + 0.5)
    hand_left_y = 0.1 - 0.1 * np.sin(t_frame * 2 + 0.5)
    
    hand_right_x = 0.5 + 0.1 * np.sin(t_frame * 3 + 0.5)
    hand_right_y = 0.1 - 0.1 * np.sin(t_frame * 2 + 0.5)
    
    # Legs (knees and feet)
    hip_left_x = -0.2
    hip_left_y = 0.0 - 0.1 * np.sin(t_frame * 2 + 0.2)
    
    hip_right_x = 0.2
    hip_right_y = 0.0 - 0.1 * np.sin(t_frame * 2 + 0.2)
    
    knee_left_x = -0.2 - 0.1 * np.sin(t_frame * 2 + 0.3)
    knee_left_y = -0.5 - 0.2 * np.sin(t_frame * 2 + 0.3)
    
    knee_right_x = 0.2 + 0.1 * np.sin(t_frame * 2 + 0.3)
    knee_right_y = -0.5 - 0.2 * np.sin(t_frame * 2 + 0.3)
    
    foot_left_x = -0.2 - 0.1 * np.sin(t_frame * 2 + 0.5)
    foot_left_y = -0.8 - 0.1 * np.sin(t_frame * 2 + 0.5)
    
    foot_right_x = 0.2 + 0.1 * np.sin(t_frame * 2 + 0.5)
    foot_right_y = -0.8 - 0.1 * np.sin(t_frame * 2 + 0.5)
    
    # Combine all points
    x = [
        head_x, 
        shoulder_left_x, shoulder_right_x, 
        torso_x, 
        elbow_left_x, elbow_right_x, 
        hand_left_x, hand_right_x, 
        
        hip_left_x, hip_right_x, 
        knee_left_x, knee_right_x, 
        foot_left_x, foot_right_x
    ]
    
    y = [
        head_y, 
        shoulder_left_y, shoulder_right_y, 
        
        torso_y, 
        
        elbow_left_y, elbow_right_y, 
        hand_left_y, hand_right_y, 
        
        hip_left_y, hip_right_y, 
        knee_left_y, knee_right_y, 
        foot_left_y, foot_right_y
    ]
    
    return x, y

# Animation update function
def update(frame):
    t_frame = t[frame]
    x, y = get_point_positions(t_frame)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.tight_layout()
plt.show()
