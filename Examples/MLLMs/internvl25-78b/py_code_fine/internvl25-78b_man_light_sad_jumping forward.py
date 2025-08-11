
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15
bg_color = "black"
pt_color = "white"

# Frame setup
fig, ax = plt.subplots()
ax.set_facecolor(bg_color)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
points = ax.scatter([], [], color=pt_color)

# Point positions
def init_points():
    base = np.array([
        [0.45, 0.8], [0.55, 0.8],  # Head
        [0.35, 0.7], [0.65, 0.7],  # Shoulders
        [0.3, 0.6], [0.4, 0.6], [0.5, 0.6], [0.6, 0.6], [0.7, 0.6],  # Arms
        [0.45, 0.5], [0.55, 0.5],  # Upper body
        [0.45, 0.4], [0.55, 0.4],  # Lower body
        [0.4, 0.3], [0.5, 0.3], [0.6, 0.3]   # Legs
    ])
    return base

# Update function for animation
def update(frame):
    base = init_points()
    t = frame / 100
    x_shift = 0.1 * np.sin(2 * np.pi * t)
    y_shift = 0.1 * np.sin(2 * np.pi * t)

    # Adjusting positions to simulate jumping forward
    positions = base + np.array([x_shift, -y_shift])
    points.set_offsets(positions)
    return points,

# Animation setup
ani = animation.FuncAnimation(
    fig, update, frames=100, interval=50, blit=True
)

plt.axis("off")
plt.show()
