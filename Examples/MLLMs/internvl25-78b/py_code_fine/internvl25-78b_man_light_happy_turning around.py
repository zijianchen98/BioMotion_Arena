
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

points, = ax.plot([], [], 'o', color='white', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    angle = np.radians(frame)
    
    center_x = 0.5
    center_y = 0.5

    radius = 0.1

    # Define the positions of the points
    positions = [
        (center_x, center_y),  # head
        (center_x - 0.1, center_y - 0.1),  # left shoulder
        (center_x + 0.1, center_y - 0.1),  # right shoulder
        (center_x - 0.15, center_y - 0.2),  # left elbow
        (center_x + 0.15, center_y - 0.2),  # right elbow
        (center_x - 0.25, center_y - 0.3),  # left hand
        (center_x + 0.25, center_y - 0.3),  # right hand
        (center_x - 0.05, center_y - 0.2),  # left hip
        (center_x + 0.05, center_y - 0.2),  # right hip
        (center_x - 0.15, center_y - 0.3),  # left knee
        (center_x + 0.15, center_y - 0.3),  # right knee
        (center_x - 0.25, center_y - 0.4),  # left foot
        (center_x + 0.25, center_y - 0.4),  # right foot
        (center_x - 0.1, center_y - 0.1),  # chest
        (center_x, center_y - 0.1)  # stomach
    ]
    
    # Rotate points around center
    rotated_positions = []
    for (x, y) in positions:
        x_new = center_x + (x - center_x) * np.cos(angle) - (y - center_y) * np.sin(angle)
        y_new = center_y + (x - center_x) * np.sin(angle) + (y - center_y) * np.cos(angle)
        rotated_positions.append((x_new, y_new))

    xs, ys = zip(*rotated_positions)
    points.set_data(xs, ys)
    return points,

ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 360, 10), init_func=init, blit=True)

plt.axis('off')
plt.show()
