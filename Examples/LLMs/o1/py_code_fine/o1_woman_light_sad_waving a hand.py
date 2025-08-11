import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Base coordinates for 15 points (x, y) in a "sad" posture
# Head, Neck, LShoulder, RShoulder, LElbow, RElbow, LWrist, RWrist,
# Torso, LHip, RHip, LKnee, RKnee, LFoot, RFoot
base_points = np.array([
    [5.0, 9.0],  # Head
    [5.0, 8.0],  # Neck
    [4.2, 8.0],  # LShoulder
    [5.8, 8.0],  # RShoulder
    [4.0, 7.0],  # LElbow
    [6.0, 7.0],  # RElbow
    [3.8, 6.0],  # LWrist
    [6.2, 6.0],  # RWrist
    [5.0, 6.5],  # Torso
    [4.6, 5.5],  # LHip
    [5.4, 5.5],  # RHip
    [4.6, 4.5],  # LKnee
    [5.4, 4.5],  # RKnee
    [4.6, 3.5],  # LFoot
    [5.4, 3.5]   # RFoot
])

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(3, 7)
ax.set_ylim(2.5, 9.5)
ax.set_aspect('equal')
ax.axis('off')

scatter = ax.scatter(base_points[:, 0], base_points[:, 1], c='white', s=50)

def init():
    scatter.set_offsets(base_points)
    return (scatter,)

def update(frame):
    # Create a copy of the base points so we don't overwrite them
    new_points = np.copy(base_points)
    
    # Slight vertical "sad" bounce for the entire body
    body_bounce = 0.1 * np.sin(frame * 0.1)
    new_points[:, 1] += body_bounce
    
    # Right wrist (index 7) wave: sinusoidal motion
    wave_amplitude = 0.3
    wave_speed = 0.2
    new_points[7, 1] += wave_amplitude * np.sin(frame * wave_speed)
    
    # Update scatter plot
    scatter.set_offsets(new_points)
    return (scatter,)

ani = FuncAnimation(fig, update, frames=120, init_func=init, interval=50, blit=True, repeat=True)
plt.show()