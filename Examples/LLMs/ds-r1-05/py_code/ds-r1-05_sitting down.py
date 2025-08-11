
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the standing pose coordinates (x, y) for 15 points
standing = [
    (0.0, 1.8),     # 0: head top
    (0.0, 1.65),    # 1: head base
    (0.0, 1.5),     # 2: shoulder center
    (-0.2, 1.5),    # 3: left shoulder
    (0.2, 1.5),     # 4: right shoulder
    (-0.4, 1.5),    # 5: left elbow (relaxed)
    (0.4, 1.5),     # 6: right elbow (relaxed)
    (-0.5, 1.0),    # 7: left hand
    (0.5, 1.0),     # 8: right hand
    (0.0, 1.2),     # 9: spine center
    (-0.2, 1.0),    # 10: left hip
    (0.2, 1.0),     # 11: right hip
    (-0.2, 0.3),    # 12: left ankle
    (0.2, 0.3),     # 13: right ankle
    (0.0, 0.9)      # 14: pelvis center
]

# Define the sitting pose coordinates (x, y) for 15 points
sitting = [
    (0.0, 1.3),     # 0: head top
    (0.0, 1.15),    # 1: head base
    (0.0, 1.0),     # 2: shoulder center
    (-0.15, 1.0),   # 3: left shoulder
    (0.15, 1.0),    # 4: right shoulder
    (-0.3, 0.9),    # 5: left elbow (bent while sitting)
    (0.3, 0.9),     # 6: right elbow (bent while sitting)
    (-0.35, 0.7),   # 7: left hand
    (0.35, 0.7),    # 8: right hand
    (0.0, 0.8),     # 9: spine center (leaning forward)
    (-0.15, 0.4),   # 10: left hip (lowered)
    (0.15, 0.4),    # 11: right hip (lowered)
    (-0.15, 0.1),   # 12: left ankle (slightly forward)
    (0.15, 0.1),    # 13: right ankle (slightly forward)
    (0.0, 0.5)      # 14: pelvis center
]

def ease_in_out(t):
    return 0.5 * (1 - np.cos(t * np.pi))

def update(frame, scat, num_frames):
    t = frame / (num_frames - 1)
    t_smooth = ease_in_out(t)
    current = []
    for i in range(len(standing)):
        x_s, y_s = standing[i]
        x_e, y_e = sitting[i]
        x = x_s + (x_e - x_s) * t_smooth
        y = y_s + (y_e - y_s) * t_smooth
        current.append([x, y])
    scat.set_offsets(current)
    return [scat]

fig = plt.figure(figsize=(7, 10), facecolor='black')
ax = fig.add_subplot(111, facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

scat = ax.scatter([], [], s=80, color='white')

num_frames = 100
ani = animation.FuncAnimation(
    fig, update, fargs=(scat, num_frames),
    frames=num_frames, interval=30, blit=True
)

plt.tight_layout()
plt.show()
