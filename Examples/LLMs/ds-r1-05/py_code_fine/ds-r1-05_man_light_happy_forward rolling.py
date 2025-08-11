
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial standing pose
standing = np.array([
    [0.0, 1.6],   # head
    [0.0, 1.4],   # neck
    [-0.2, 1.3], [0.2, 1.3],   # shoulders (left, right)
    [-0.2, 1.1], [0.2, 1.1],   # elbows
    [-0.2, 0.9], [0.2, 0.9],   # hands
    [0.0, 1.0],   # torso
    [-0.2, 0.8], [0.2, 0.8],   # hips
    [-0.2, 0.5], [0.2, 0.5],   # knees
    [-0.2, 0.1], [0.2, 0.1]    # feet
])

# Poses at key times
key_times = [0.0, 0.5, 1.5, 1.7, 2.3, 3.0]
keyframes = {
    0.0: standing,
    0.5: np.array([
        [0.6, 1.0],    # head
        [0.6, 0.9],    # neck
        [0.4, 0.8], [0.8, 0.8],    # shoulders
        [0.3, 0.5], [0.7, 0.5],    # elbows
        [0.3, 0.2], [0.7, 0.2],    # hands
        [0.6, 0.7],    # torso
        [0.5, 0.6], [0.7, 0.6],    # hips
        [0.5, 0.5], [0.7, 0.5],    # knees
        [0.5, 0.1], [0.7, 0.1]     # feet
    ]),
    1.5: np.array([
        [1.4, 0.4],    # head
        [1.4, 0.3],    # neck
        [1.3, 0.5], [1.5, 0.5],    # shoulders
        [1.2, 0.7], [1.4, 0.7],    # elbows
        [1.1, 0.9], [1.3, 0.9],    # hands
        [1.4, 0.6],    # torso
        [1.3, 0.8], [1.5, 0.8],    # hips
        [1.2, 1.0], [1.4, 1.0],    # knees
        [1.1, 1.2], [1.3, 1.2]     # feet
    ]),
    1.7: np.array([
        [1.8, 0.3],    # head
        [1.8, 0.4],    # neck
        [1.7, 0.5], [1.9, 0.5],    # shoulders
        [1.6, 0.2], [1.8, 0.2],    # elbows
        [1.5, 0.0], [1.7, 0.0],    # hands
        [1.8, 0.6],    # torso
        [1.7, 0.7], [1.9, 0.7],    # hips
        [1.6, 0.9], [1.8, 0.9],    # knees
        [1.5, 1.1], [1.7, 1.1]     # feet
    ]),
    2.3: np.array([
        [3.0, 0.8],    # head
        [3.0, 0.7],    # neck
        [2.9, 0.6], [3.1, 0.6],    # shoulders
        [2.9, 0.4], [3.1, 0.4],    # elbows
        [2.9, 0.2], [3.1, 0.2],    # hands
        [3.0, 0.5],    # torso
        [2.9, 0.5], [3.1, 0.5],    # hips
        [2.9, 0.3], [3.1, 0.3],    # knees
        [2.9, 0.1], [3.1, 0.1]     # feet
    ]),
    3.0: np.array([
        [4.0, 1.6],    # head
        [4.0, 1.4],    # neck
        [3.8, 1.3], [4.2, 1.3],    # shoulders
        [3.8, 1.1], [4.2, 1.1],    # elbows
        [3.8, 0.9], [4.2, 0.9],    # hands
        [4.0, 1.0],    # torso
        [3.8, 0.8], [4.2, 0.8],    # hips
        [3.8, 0.5], [4.2, 0.5],    # knees
        [3.8, 0.1], [4.2, 0.1]     # feet
    ])
}

# Function to interpolate positions between keyframes
def interpolate_points(t):
    global key_times, keyframes
    
    if t <= key_times[0]:
        return keyframes[key_times[0]]
    elif t >= key_times[-1]:
        return keyframes[key_times[-1]]
    else:
        for i in range(1, len(key_times)):
            if t < key_times[i]:
                t_prev = key_times[i-1]
                t_next = key_times[i]
                frac = (t - t_prev) / (t_next - t_prev)
                points_prev = keyframes[t_prev]
                points_next = keyframes[t_next]
                interp_points = points_prev + frac * (points_next - points_prev)
                return interp_points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 5)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
scat = ax.scatter([], [], s=100, c='white', marker='o')
ax.set_axis_off()

# Animation function
def animate(frame):
    t = frame * 0.1  # Time in seconds at 10 frames per second
    points = interpolate_points(t)
    scat.set_offsets(points)
    return scat,

# Create animation
fps = 10
total_frames = int(3 * fps)  # 3 seconds
anim = FuncAnimation(fig, animate, frames=total_frames, interval=1000//fps, blit=True)

plt.tight_layout()
plt.show()
