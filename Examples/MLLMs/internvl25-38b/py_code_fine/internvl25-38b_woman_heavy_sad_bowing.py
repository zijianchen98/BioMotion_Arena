
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the bowing animation
num_frames = 120
frame_rate = 30  # Frames per second
num_points = 15

# Position parameters (initial positions for the sad woman with heavy weight)
initial_positions = np.array([
    [0.5, 0.3], [0.4, 0.4], [0.6, 0.4],  # Head and shoulders
    [0.45, 0.5], [0.55, 0.5],              # Shoulders
    [0.4, 0.6], [0.6, 0.6],              # Upper arms
    [0.35, 0.7], [0.65, 0.7],              # Lower arms
    [0.5, 0.8], [0.45, 0.85], [0.55, 0.85],  # Upper body and abdomen
    [0.45, 0.9], [0.55, 0.9],              # Hips
    [0.42, 1.0], [0.58, 1.0]               # Feet
])

# Bowing motion parameters
amplitude = 0.1
frequency = 0.5 * np.pi / (num_frames // 2)

def update_positions(frame):
    angle = amplitude * np.sin(frame * frequency)
    positions = initial_positions.copy()
    positions[:, 1] += angle
    return positions

def update(frame, scat):
    positions = update_positions(frame)
    scat.set_offsets(positions)
    return scat,

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
scat = ax.scatter([], [])

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(num_frames), fargs=(scat,), interval=1000 / frame_rate, blit=True
)

plt.show()
