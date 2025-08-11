
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

# Parameters
num_points = 15
fps = 30
duration = 5  # seconds
total_frames = fps * duration

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_points)]

# Define the motion of a lying down person (simplified)
def get_positions(frame):
    t = frame / fps  # time in seconds
    
    # Main body points (lying horizontally)
    body_x = np.linspace(-1.5, 1.5, 7)
    body_y = np.zeros(7) + 0.1 * np.sin(2 * np.pi * t)  # slight breathing motion
    
    # Head (ellipse)
    head_x = -1.6 + 0.1 * np.sin(2 * np.pi * t * 0.5)
    head_y = 0.1 * np.sin(2 * np.pi * t)
    
    # Arms (simplified)
    left_arm_x = np.array([-1.5, -1.8])
    left_arm_y = np.array([0.1, 0.3 + 0.1 * np.sin(2 * np.pi * t * 1.2)])
    
    right_arm_x = np.array([1.5, 1.8])
    right_arm_y = np.array([0.1, 0.3 + 0.1 * np.sin(2 * np.pi * t * 1.2 + np.pi)])
    
    # Legs (simplified)
    left_leg_x = np.array([-0.5, -0.7])
    left_leg_y = np.array([0.0, -0.4 + 0.1 * np.sin(2 * np.pi * t * 0.8)])
    
    right_leg_x = np.array([0.5, 0.7])
    right_leg_y = np.array([0.0, -0.4 + 0.1 * np.sin(2 * np.pi * t * 0.8 + np.pi)])
    
    # Combine all points
    x = np.concatenate([
        [head_x],
        body_x,
        left_arm_x,
        right_arm_x,
        left_leg_x,
        right_leg_x
    ])
    y = np.concatenate([
        [head_y],
        body_y,
        left_arm_y,
        right_arm_y,
        left_leg_y,
        right_leg_y
    ])
    
    return x, y

# Animation update function
def update(frame):
    x, y = get_positions(frame)
    for i in range(num_points):
        points[i].set_data(x[i], y[i])
    return points

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=total_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
