
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_points = 15
frame_rate = 30
total_frames = 60
weight_factor = 0.5

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'o', markersize=10, color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Clear previous points
    points.set_data([], [])

    # Calculate new positions for the points
    if frame < total_frames // 2:
        x = np.linspace(-2 + weight_factor * np.sin(2 * np.pi * frame / total_frames),
                        2 - weight_factor * np.sin(2 * np.pi * frame / total_frames),
                        num_points)
        y = np.linspace(-1 + weight_factor * np.cos(2 * np.pi * frame / total_frames),
                        1 - weight_factor * np.cos(2 * np.pi * frame / total_frames),
                        num_points)
    else:
        x = np.linspace(-2 + weight_factor * np.sin(2 * np.pi * (frame - total_frames // 2) / total_frames),
                        2 - weight_factor * np.sin(2 * np.pi * (frame - total_frames // 2) / total_frames),
                        num_points)
        y = np.linspace(-1 + weight_factor * np.cos(2 * pi * (frame - total_frames // 2) / total_frames),
                        1 - weight_factor * np.cos(2 * pi * (frame - total_frames // 2) / total_frames),
                        num_points)

    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, update, frames=range(total_frames), init_func=init, blit=True, interval=int(1000 / frame_rate))

plt.show()
