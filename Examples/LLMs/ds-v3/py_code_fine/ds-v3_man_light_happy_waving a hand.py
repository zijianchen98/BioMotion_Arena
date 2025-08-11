
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define the motion parameters for a waving hand
def update(frame):
    t = frame * 0.1  # Time parameter
    
    # Body points (relative to torso)
    torso_x = 0
    torso_y = 0
    
    # Head
    head_x = torso_x
    head_y = torso_y + 0.8
    
    # Shoulders
    shoulder_left_x = torso_x - 0.3
    shoulder_right_x = torso_x + 0.3
    shoulder_y = torso_y + 0.5
    
    # Elbows
    elbow_left_x = shoulder_left_x - 0.2
    elbow_right_x = shoulder_right_x + 0.2
    elbow_left_y = shoulder_y - 0.3
    elbow_right_y = shoulder_y - 0.3
    
    # Hands - right hand is waving
    hand_left_x = elbow_left_x - 0.2
    hand_left_y = elbow_left_y - 0.2
    
    # Waving motion for right hand
    wave_amplitude = 0.3
    wave_frequency = 0.5
    hand_right_x = elbow_right_x + 0.2 + wave_amplitude * np.sin(t * wave_frequency * 2 * np.pi)
    hand_right_y = elbow_right_y - 0.2 + wave_amplitude * np.sin(t * wave_frequency * np.pi)
    
    # Hips
    hip_left_x = torso_x - 0.2
    hip_right_x = torso_x + 0.2
    hip_y = torso_y - 0.2
    
    # Knees
    knee_left_x = hip_left_x
    knee_right_x = hip_right_x
    knee_left_y = hip_y - 0.5
    knee_right_y = hip_y - 0.5
    
    # Feet
    foot_left_x = knee_left_x - 0.1
    foot_right_x = knee_right_x + 0.1
    foot_left_y = knee_left_y - 0.3
    foot_right_y = knee_right_y - 0.3
    
    # Additional points for more natural motion (e.g., fingers, toes)
    # Right hand fingers (3 points)
    finger1_right_x = hand_right_x + 0.1 * np.sin(t * wave_frequency * 2 * np.pi + np.pi/4)
    finger1_right_y = hand_right_y + 0.1 * np.cos(t * wave_frequency * 2 * np.pi + np.pi/4)
    finger2_right_x = hand_right_x + 0.1 * np.sin(t * wave_frequency * 2 * np.pi)
    finger2_right_y = hand_right_y + 0.1 * np.cos(t * wave_frequency * 2 * np.pi)
    finger3_right_x = hand_right_x + 0.1 * np.sin(t * wave_frequency * 2 * np.pi - np.pi/4)
    finger3_right_y = hand_right_y + 0.1 * np.cos(t * wave_frequency * 2 * np.pi - np.pi/4)
    
    # Left hand fingers (static)
    finger1_left_x = hand_left_x - 0.1
    finger1_left_y = hand_left_y - 0.1
    finger2_left_x = hand_left_x - 0.15
    finger2_left_y = hand_left_y
    finger3_left_x = hand_left_x - 0.1
    finger3_left_y = hand_left_y + 0.1
    
    # Assemble all points
    x_points = [
        head_x,
        shoulder_left_x, shoulder_right_x,
        elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x,
        hip_left_x, hip_right_x,
        knee_left_x, knee_right_x,
        foot_left_x, foot_right_x,
        finger1_right_x, finger2_right_x, finger3_right_x
    ]
    
    y_points = [
        head_y,
        shoulder_y, shoulder_y,
        elbow_left_y, elbow_right_y,
        hand_left_y, hand_right_y,
        hip_y, hip_y,
        knee_left_y, knee_right_y,
        foot_left_y, foot_right_y,
        finger1_right_y, finger2_right_y, finger3_right_y
    ]
    
    points.set_data(x_points, y_points)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.title('Point-Light Biological Motion: Waving Hand', color='white')
plt.tight_layout()
plt.show()
