
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point-lights and frames
num_points = 15
num_frames = 60  # Adjust for smoother animation

# Create a simple biomechanically plausible sitting motion
def generate_motion(frames):
    # Simulate key points for a sitting motion (simplified)
    # Points: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2), torso (1)
    motion = np.zeros((frames, num_points, 2))
    
    # Initial positions (standing)
    for i in range(frames):
        t = i / frames
        # Head (sinusoidal for slight movement)
        motion[i, 0, 0] = 0.5
        motion[i, 0, 1] = 1.8 - 0.2 * np.sin(t * np.pi)
        
        # Shoulders
        motion[i, 1, 0] = 0.3
        motion[i, 1, 1] = 1.5 - 0.1 * t
        motion[i, 2, 0] = 0.7
        motion[i, 2, 1] = 1.5 - 0.1 * t
        
        # Elbows (move down and slightly forward)
        motion[i, 3, 0] = 0.2 + 0.1 * t
        motion[i, 3, 1] = 1.3 - 0.3 * t
        motion[i, 4, 0] = 0.8 - 0.1 * t
        motion[i, 4, 1] = 1.3 - 0.3 * t
        
        # Hands (follow elbows with more movement)
        motion[i, 5, 0] = 0.1 + 0.2 * t
        motion[i, 5, 1] = 1.1 - 0.4 * t
        motion[i, 6, 0] = 0.9 - 0.2 * t
        motion[i, 6, 1] = 1.1 - 0.4 * t
        
        # Hips (move down and back slightly)
        motion[i, 7, 0] = 0.4 - 0.05 * t
        motion[i, 7, 1] = 1.0 - 0.5 * t
        motion[i, 8, 0] = 0.6 + 0.05 * t
        motion[i, 8, 1] = 1.0 - 0.5 * t
        
        # Knees (bend as sitting)
        motion[i, 9, 0] = 0.3
        motion[i, 9, 1] = 0.6 - 0.3 * t
        motion[i, 10, 0] = 0.7
        motion[i, 10, 1] = 0.6 - 0.3 * t
        
        # Feet (stay on ground, slight movement)
        motion[i, 11, 0] = 0.2
        motion[i, 11, 1] = 0.1
        motion[i, 12, 0] = 0.8
        motion[i, 12, 1] = 0.1
        
        # Torso (midpoint between shoulders and hips)
        motion[i, 13, 0] = 0.5
        motion[i, 13, 1] = (motion[i, 1, 1] + motion[i, 7, 1]) / 2
        
        # Additional point for spine or balance
        motion[i, 14, 0] = 0.5
        motion[i, 14, 1] = (motion[i, 0, 1] + motion[i, 13, 1]) / 2
    
    return motion

# Generate motion data
motion_data = generate_motion(num_frames)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Create point-light artists
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_points)]

# Initialization function
def init():
    for point in points:
        point.set_data([], [])
    return points

# Animation update function
def update(frame):
    for i, point in enumerate(points):
        x, y = motion_data[frame, i, 0], motion_data[frame, i, 1]
        point.set_data(x, y)
    return points

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=50
)

plt.tight_layout()
plt.show()
