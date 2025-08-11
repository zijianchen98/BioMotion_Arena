
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
FRAME_RATE = 30
DURATION = 5
FRAMES = FRAME_RATE * DURATION
AMPLITUDE = 50
FREQUENCY = 1 / 2  # Frequency of jump cycle in seconds

# Body points defined relative to the center of mass (COM)
body_points = {
    'left_ankle': (-20, -40),
    'right_ankle': (20, -40),
    'left_knee': (-10, -20),
    'right_knee': (10, -20),
    'left_hip': (-5, -10),
    'right_hip': (5, -10),
    'waist': (0, 0),
    'chest': (0, 15),
    'left_shoulder': (-10, 30),
    'right_shoulder': (10, 30),
    'left_elbow': (-20, 45),
    'right_elbow': (20, 45),
    'left_wrist': (-30, 60),
    'right_wrist': (30, 60),
}

def update(frame):
    t = frame / FRAME_RATE
    angle = np.sin(2 * np.pi * t / FREQUENCY) * AMPLITUDE
    
    for name, point in body_points.items():
        x, y = point
        if 'ankle' in name or 'knee' in name or 'hip' in name:
            y += angle
        elif 'waist' in name:
            y += angle / 2
        elif 'chest' in name:
            y += angle / 4
        else:
            y -= angle / 8
        
        x_positions[name] = x
        y_positions[name] = y
    
    scatter.set_offsets(np.c_[x_positions.values(), y_positions.values()])

fig, ax = plt.subplots()
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.axis('off')

x_positions = {name: x for name, (x, _) in body_points.items()}
y_positions = {name: y for name, (_, y) in body_points.items()}

scatter = ax.scatter(x_positions.values(), y_positions.values(), color='white', s=50)

ani = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FREEZE_RATE, blit=False)
plt.show()
