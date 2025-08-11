
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
n_points = 15
radius = 1.5
offsets = np.linspace(0, 2 * np.pi, n_points)
frame_duration = 50  # duration in ms for each frame
frames_per_second = 15
frames = frame_duration / 1000 * frames_per_second

# Create animation function
def animation(update):
    # Set up plot
    plt.cla()  # clear current instance
    ax = plt.gca()
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.set_aspect('equal')
    ax.set_axis_off()
    background = plt.fill_between(range(-radius, radius), range(-radius, radius), color='black')

    # Generate points
    points = []
    for offset in offsets:
        point = []
        for i in range(n_points):
            x = radius * np.cos(offset + i * 2 * np.pi / n_points)
            y = radius * np.sin(offset + i * 2 * np.pi / n_points)
            point.append(x)
        points.append(point)
    
    # Plot points
    for point in points:
        plt.plot([0] * len(point), [0] * len(point), 'o', color='white')

# Animation object
fig = plt.figure(figsize=(6.25, 6.25))
ani = FuncAnimation(fig, animation, blit=True, frames=np.arange(0, 360, 10), interval=frame_duration)

# Show plot
plt.show()
