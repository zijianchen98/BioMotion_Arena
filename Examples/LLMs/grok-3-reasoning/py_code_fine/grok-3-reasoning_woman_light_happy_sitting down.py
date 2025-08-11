
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the points with their standing and sitting positions
points = [
    {'name': 'head', 'standing': (50, 180), 'sitting': (50, 140)},
    {'name': 'neck', 'standing': (50, 170), 'sitting': (50, 130)},
    {'name': 'chest', 'standing': (50, 150), 'sitting': (50, 110)},
    {'name': 'left_shoulder', 'standing': (30, 160), 'sitting': (30, 120)},
    {'name': 'right_shoulder', 'standing': (70, 160), 'sitting': (70, 120)},
    {'name': 'left_elbow', 'standing': (20, 140), 'sitting': (35, 90)},
    {'name': 'right_elbow', 'standing': (80, 140), 'sitting': (65, 90)},
    {'name': 'left_wrist', 'standing': (10, 120), 'sitting': (35, 70)},
    {'name': 'right_wrist', 'standing': (90, 120), 'sitting': (65, 70)},
    {'name': 'left_hip', 'standing': (40, 120), 'sitting': (40, 80)},
    {'name': 'right_hip', 'standing': (60, 120), 'sitting': (60, 80)},
    {'name': 'left_knee', 'standing': (40, 60), 'sitting': (40, 40)},
    {'name': 'right_knee', 'standing': (60, 60), 'sitting': (60, 40)},
    {'name': 'left_ankle', 'standing': (40, 0), 'sitting': (40, 0)},
    {'name': 'right_ankle', 'standing': (60, 0), 'sitting': (60, 0)},
]

# Set up the figure with a black background
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(0, 100)
ax.set_ylim(0, 200)
ax.axis('off')

# Initial positions for the scatter plot
standing_positions = [p['standing'] for p in points]
x_standing = [pos[0] for pos in standing_positions]
y_standing = [pos[1] for pos in standing_positions]
scatter = ax.scatter(x_standing, y_standing, c='white', s=50)

# Update function for the animation
def update(frame):
    t = frame / 29.0  # Assuming 30 frames for the animation
    positions = []
    for p in points:
        standing = p['standing']
        sitting = p['sitting']
        x = (1 - t) * standing[0] + t * sitting[0]
        y = (1 - t) * standing[1] + t * sitting[1]
        positions.append((x, y))
    x = [pos[0] for pos in positions]
    y = [pos[1] for pos in positions]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=30, interval=50, blit=True)

# Display the animation
plt.show()
