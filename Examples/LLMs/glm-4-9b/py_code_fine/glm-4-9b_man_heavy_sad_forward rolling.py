
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
duration = 300  # frames
fps = 30
滚动_period = 10  # seconds
滚动_amplitude = 0.8
time_step = 1 / fps

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize point-lights
points = [Circle((0, 0), radius=0.02, facecolor='white', edgecolor='none') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Function to simulate the rolling motion
def rolling_motion(t, amplitude, period):
    omega = 2 * np.pi / period
    x = amplitude * np.sin(omega * t)
    y = -amplitude * np.cos(omega * t)
    return x, y

# Animation update function
def update(frame):
    t = frame * time_step
    for i, point in enumerate(points):
        angle = 2 * np.pi * (i / num_points) + 2 * np.pi * t
        x, y = rolling_motion(t, rolling_amplitude,滚动_period)
        x += 0.2 * np.cos(angle)
        y += 0.2 * np.sin(angle)
        point.center = (x, y)
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=duration, blit=True, interval=time_step*1000)

plt.show()
