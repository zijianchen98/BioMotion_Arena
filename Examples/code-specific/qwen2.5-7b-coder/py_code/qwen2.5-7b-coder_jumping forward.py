
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
frame_rate = 30
jump_duration = 1.0  # seconds
total_frames = int(frame_rate * jump_duration)

# Initial positions
initial_positions = np.linspace(0, 1, num_points)
positions = initial_positions.copy()

# Time array
time = np.linspace(0, jump_duration, total_frames)

# Jump parameters
amplitude = 0.1
frequency = 2 * np.pi / jump_duration

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(-amplitude, amplitude)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', markersize=10, color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = time[frame]
    positions = initial_positions + amplitude * np.sin(frequency * t - 2 * np.pi * frame / total_frames)
    points.set_data(positions, [0] * num_points)
    return points,

ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, interval=1000 / frame_rate)

plt.show()
