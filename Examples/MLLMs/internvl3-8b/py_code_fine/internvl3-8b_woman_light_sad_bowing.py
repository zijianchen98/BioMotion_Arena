
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def update_points(frame_number, points):
    """Update the points in the animation"""
    # The current frame determines the vertical position of the arrows
    # Assuming the animation follows a simple sinusoidal motion
    t = np.linspace(0, np.pi * frame_number / 360, len(points))
    points.set_data(np.cos(t), np.sin(t))
    return points,

fig, ax = plt.subplots(subplot_kw={'xaxis': 'off', 'yaxis': 'off'})
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], 'bo')  # Blue circles

# Generate initial positions
points_x = np.random.uniform(-1, 1, size=15)
points_y = np.random.uniform(-1, 1, size=15)
points = ax.scatter(points_x, points_y, color='white')

# Animate
ani = animation.FuncAnimation(fig, update_points, fargs=(points,), frames=360, interval=50, blit=True)
plt.show()
