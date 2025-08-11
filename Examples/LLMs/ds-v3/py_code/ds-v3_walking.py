
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches

# Define the number of points and frames
num_points = 15
num_frames = 30

# Define the positions of the points for a walking motion
def generate_walking_motion(frames, points):
    # Key points: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2)
    # The motion is a simple sinusoidal movement for demonstration
    # Each point's position is a function of time (frame)
    t = np.linspace(0, 2 * np.pi, frames)
    
    # Head position (stationary in x, slight vertical movement)
    head_x = np.zeros(frames)
    head_y = 1.5 + 0.1 * np.sin(t * 2)
    
    # Shoulders (move side to side)
    shoulder_y = 1.3 + 0.05 * np.sin(t)
    left_shoulder_x = -0.2 + 0.1 * np.sin(t)
    right_shoulder_x = 0.2 + 0.1 * np.sin(t + np.pi)
    
    # Elbows (move opposite to shoulders)
    left_elbow_x = left_shoulder_x - 0.2 + 0.1 * np.sin(t + np.pi/2)
    left_elbow_y = shoulder_y - 0.2 + 0.1 * np.sin(t * 2)
    right_elbow_x = right_shoulder_x + 0.2 + 0.1 * np.sin(t + np.pi/2 + np.pi)
    right_elbow_y = shoulder_y - 0.2 + 0.1 * np.sin(t * 2 + np.pi)
    
    # Hands (follow elbows with more movement)
    left_hand_x = left_elbow_x - 0.2 + 0.1 * np.sin(t * 2)
    left_hand_y = left_elbow_y - 0.2 + 0.1 * np.sin(t * 3)
    right_hand_x = right_elbow_x + 0.2 + 0.1 * np.sin(t * 2 + np.pi)
    right_hand_y = right_elbow_y - 0.2 + 0.1 * np.sin(t * 3 + np.pi)
    
    # Hips (stationary in x, slight vertical movement)
    hip_y = 0.8 + 0.05 * np.sin(t)
    left_hip_x = -0.1 + 0.05 * np.sin(t + np.pi/2)
    right_hip_x = 0.1 + 0.05 * np.sin(t + np.pi/2 + np.pi)
    
    # Knees (move opposite to hips)
    left_knee_x = left_hip_x - 0.1 + 0.1 * np.sin(t * 2)
    left_knee_y = hip_y - 0.3 + 0.1 * np.sin(t * 3)
    right_knee_x = right_hip_x + 0.1 + 0.1 * np.sin(t * 2 + np.pi)
    right_knee_y = hip_y - 0.3 + 0.1 * np.sin(t * 3 + np.pi)
    
    # Feet (follow knees with more movement)
    left_foot_x = left_knee_x - 0.1 + 0.1 * np.sin(t * 3)
    left_foot_y = left_knee_y - 0.2 + 0.1 * np.sin(t * 4)
    right_foot_x = right_knee_x + 0.1 + 0.1 * np.sin(t * 3 + np.pi)
    right_foot_y = right_knee_y - 0.2 + 0.1 * np.sin(t * 4 + np.pi)
    
    # Combine all points
    points_x = np.array([
        head_x,
        left_shoulder_x, right_shoulder_x,
        left_elbow_x, right_elbow_x,
        left_hand_x, right_hand_x,
        left_hip_x, right_hip_x,
        left_knee_x, right_knee_x,
        left_foot_x, right_foot_x
    ])
    
    points_y = np.array([
        head_y,
        shoulder_y, shoulder_y,
        left_elbow_y, right_elbow_y,
        left_hand_y, right_hand_y,
        hip_y, hip_y,
        left_knee_y, right_knee_y,
        left_foot_y, right_foot_y
    ])
    
    # Ensure we have exactly 15 points (duplicate some if necessary)
    if points_x.shape[0] < points:
        # Duplicate some points to reach 15
        extra = points - points_x.shape[0]
        points_x = np.vstack([points_x, np.tile(points_x[-1], (extra, 1))])
        points_y = np.vstack([points_y, np.tile(points_y[-1], (extra, 1))])
    
    return points_x, points_y

# Generate the motion data
points_x, points_y = generate_walking_motion(num_frames, num_points)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize the points
points = ax.plot([], [], 'wo', markersize=10)[0]

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    x = points_x[:, frame]
    y = points_y[:, frame]
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=100)

plt.title('Biological Motion: Walking', color='white')
plt.show()
