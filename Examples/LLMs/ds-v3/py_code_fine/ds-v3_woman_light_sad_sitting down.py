
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 100
fps = 30

# Generate motion data for a sitting down action
def generate_sitting_motion():
    # Time array
    t = np.linspace(0, 2 * np.pi, num_frames)
    
    # Key points for the sitting motion (simplified)
    # Head (circular motion)
    head_x = 0.5 * np.cos(t * 0.5) + 0.5
    head_y = 0.5 * np.sin(t * 0.5) + 0.7
    
    # Shoulders (slight movement)
    shoulder_x = np.zeros(num_frames) + 0.5
    shoulder_y = 0.6 - 0.1 * np.sin(t * 0.5)
    
    # Elbows (moving down and slightly back)
    elbow_left_x = -0.2 * np.ones(num_frames) + 0.5
    elbow_left_y = 0.5 - 0.2 * np.sin(t * 0.5)
    elbow_right_x = 0.2 * np.ones(num_frames) + 0.5
    elbow_right_y = 0.5 - 0.2 * np.sin(t * 0.5)
    
    # Hands (following elbows)
    hand_left_x = -0.3 * np.ones(num_frames) + 0.5
    hand_left_y = 0.4 - 0.1 * np.sin(t * 0.5)
    hand_right_x = 0.3 * np.ones(num_frames) + 0.5
    hand_right_y = 0.4 - 0.1 * np.sin(t * 0.5)
    
    # Torso (slight bend)
    torso_x = np.zeros(num_frames) + 0.5
    torso_y = np.linspace(0.5, 0.3, num_frames)
    
    # Hips (moving down)
    hip_x = np.zeros(num_frames) + 0.5
    hip_y = np.linspace(0.3, 0.1, num_frames)
    
    # Knees (bending)
    knee_left_x = -0.15 * np.ones(num_frames) + 0.5
    knee_left_y = 0.1 - 0.1 * np.sin(t * 0.5)
    knee_right_x = 0.15 * np.ones(num_frames) + 0.5
    knee_right_y = 0.1 - 0.1 * np.sin(t * 0.5)
    
    # Feet (moving slightly)
    foot_left_x = -0.2 * np.ones(num_frames) + 0.5
    foot_left_y = 0.0 - 0.05 * np.sin(t * 0.5)
    foot_right_x = 0.2 * np.ones(num_frames) + 0.5
    foot_right_y = 0.0 - 0.05 * np.sin(t * 0.5)
    
    # Combine all points
    points_x = np.vstack([
        head_x, shoulder_x, elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x, torso_x, hip_x,
        knee_left_x, knee_right_x, foot_left_x, foot_right_x,
        # Additional points for more detail (e.g., mid-torso, etc.)
        np.zeros(num_frames) + 0.5,  # mid-torso
        np.linspace(-0.1, 0.1, num_frames) + 0.5,  # mid-hip
        np.linspace(-0.05, 0.05, num_frames) + 0.5  # mid-knee
    ])
    
    points_y = np.vstack([
        head_y, shoulder_y, elbow_left_y, elbow_right_y,
        hand_left_y, hand_right_y, torso_y, hip_y,
        knee_left_y, knee_right_y, foot_left_y, foot_right_y,
        # Additional points
        np.linspace(0.4, 0.2, num_frames),
        np.linspace(0.2, 0.1, num_frames),
        np.linspace(0.05, 0.0, num_frames)
    ])
    
    return points_x, points_y

# Generate the motion data
points_x, points_y = generate_sitting_motion()

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Create point-light markers
points = [ax.plot([], [], 'wo', markersize=10)[0] for _ in range(num_points)]

# Initialization function
def init():
    for point in points:
        point.set_data([], [])
    return points

# Animation update function
def update(frame):
    for i, point in enumerate(points):
        point.set_data(points_x[i, frame], points_y[i, frame])
    return points

# Create the animation
ani = FuncAnimation(
    fig, update, frames=num_frames, init_func=init,
    blit=True, interval=1000/fps
)

plt.title('Point-Light Animation: Sitting Down', color='white')
plt.show()
