
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the 15 keypoints of a human skeleton in an upright position
# Order: head, neck, L-shoulder, R-shoulder, L-elbow, R-elbow, L-hand, R-hand,
#        torso, L-hip, R-hip, L-knee, R-knee, L-foot, R-foot
upright_points = np.array([
    [ 0.0,  1.8],   # head
    [ 0.0,  1.6],   # neck / upper torso
    [-0.2,  1.5],   # left shoulder
    [ 0.2,  1.5],   # right shoulder
    [-0.5,  1.2],   # left elbow
    [ 0.5,  1.2],   # right elbow
    [-0.7,  0.9],   # left hand
    [ 0.7,  0.9],   # right hand
    [ 0.0,  1.1],   # mid torso (sternum)
    [-0.2,  0.8],   # left hip
    [ 0.2,  0.8],   # right hip
    [-0.2,  0.3],   # left knee
    [ 0.2,  0.3],   # right knee
    [-0.2, -0.2],   # left foot
    [ 0.2, -0.2],   # right foot
])

# Rotate the upright skeleton by -90° to get a lying-down posture
theta = -np.pi / 2
rot_mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])
lying_points = upright_points.dot(rot_mat.T)

# We'll animate slow breathing: the neck (1) and torso (8) move up/down
breath_amplitude = 0.03  # small movement
breath_freq = 0.25       # Hz

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_facecolor('black')
scat = ax.scatter(lying_points[:, 0],
                  lying_points[:, 1],
                  s=100,
                  c='white')

# Hide axes
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(lying_points[:, 0].min() - 0.5, lying_points[:, 0].max() + 0.5)
ax.set_ylim(lying_points[:, 1].min() - 0.5, lying_points[:, 1].max() + 0.5)
ax.set_aspect('equal')

# Animation update function
def update(frame):
    t = frame / 30.0  # assume 30 fps
    offset = breath_amplitude * np.sin(2 * np.pi * breath_freq * t)
    pts = lying_points.copy()
    # apply breathing offset to neck and sternum
    pts[1, 1] += offset
    pts[8, 1] += offset
    scat.set_offsets(pts)
    return scat,

# Create the animation
ani = FuncAnimation(fig,
                    update,
                    frames=300,
                    interval=1000/30,
                    blit=True)

plt.show()
