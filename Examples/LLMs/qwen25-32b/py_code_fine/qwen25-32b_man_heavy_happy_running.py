
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
FPS = 30
DURATION_SECONDS = 10
FRAMES = FPS * DURATION_SECONDS
BODY_POINTS = {
    'left_ankle': [1, 1],
    'right_ankle': [1, -1],
    'left_knee': [0.5, 1.5],
    'right_knee': [0.5, -1.5],
    'left_hip': [0, 2],
    'right_hip': [0, -2],
    'waist': [-0.5, 0],
    'chest': [-1, 0],
    'left_shoulder': [-1.5, 1],
    'right_shoulder': [-1.5, -1],
    'left_elbow': [-2, 1.5],
    'right_elbow': [-2, -1.5],
    'left_wrist': [-2.5, 2],
    'right_wrist': [-2.5, -2],
    'head': [-3, 0]
}

def update(frame):
    global BODY_POINTS
    angle = frame / FRAMES * 4 * np.pi
    amplitude = 0.5
    phase_shift = 0.5 * np.pi
    
    # Update positions based on sine waves for running motion
    for key in ['left_ankle', 'right_ankle', 'left_knee', 'right_knee', 'left_hip', 'right_hip']:
        if 'left' in key:
            BODY_POINTS[key][0] = 1 + amplitude * np.sin(angle + phase_shift)
        else:
            BODY_POINTS[key][0] = 1 + amplitude * np.sin(angle - phase_shift)
    
    # Plot the points
    x_points = [BODY_POINTS[k][0] for k in BODY_POINTS.keys()]
    y_points = [BODY_POINTS[k][1] for k in BODY_POINTS.keys()]
    
    scat.set_offsets(np.c_[x_points, y_points])

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')  # Hide axes for cleaner look
scat = ax.scatter([], [], s=50, c='white')

ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS)

plt.show()
