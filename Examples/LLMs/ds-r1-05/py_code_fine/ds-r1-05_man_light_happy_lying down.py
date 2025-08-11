
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial positions of the 15 points: [x, y]
initial_positions = [
    [-0.8, 0.0],   # head
    [-0.7, 0.0],   # neck
    [-0.7, -0.1],  # right shoulder
    [-0.5, -0.1],  # right elbow
    [-0.2, -0.1],  # right wrist
    [-0.7, 0.1],   # left shoulder
    [-0.5, 0.1],   # left elbow
    [-0.2, 0.1],   # left wrist
    [0.0, -0.1],   # right hip
    [0.3, -0.1],   # right knee
    [0.6, -0.1],   # right ankle
    [0.0, 0.1],    # left hip
    [0.3, 0.1],    # left knee
    [0.6, 0.1],    # left ankle
    [0.0, 0.0]     # pelvis
]

# Factors for breathing motion amplitude (0 = no motion, 1 = max motion)
factors = [
    0.25,  # head
    1.0,   # neck
    1.0,   # right shoulder
    0.1,   # right elbow
    0.0,   # right wrist
    1.0,   # left shoulder
    0.1,   # left elbow
    0.0,   # left wrist
    0.33,  # right hip
    0.0,   # right knee
    0.0,   # right ankle
    0.33,  # left hip
    0.0,   # left knee
    0.0,   # left ankle
    0.33   # pelvis
]

# Animation parameters
A = 0.02    # Maximum amplitude of motion
f = 1       # Frequency in Hz
fps = 40    # Frames per second
duration = 5  # Duration in seconds
total_frames = fps * duration

fig = plt.figure(figsize=(8, 4), facecolor='black')
ax = plt.axes(xlim=(-0.9, 0.7), ylim=(-0.2, 0.2))
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
scat = ax.scatter([], [], s=50, color='white')

def init():
    scat.set_offsets(initial_positions)
    return scat,

def update(frame):
    t = frame / fps
    new_positions = np.array(initial_positions)
    # Apply vertical movement: y = y0 + factor * A * sin(2*pi*f*t)
    for i in range(len(initial_positions)):
        new_positions[i, 1] += factors[i] * A * np.sin(2 * np.pi * f * t)
    scat.set_offsets(new_positions)
    return scat,

ani = animation.FuncAnimation(
    fig, 
    update, 
    frames=total_frames,
    init_func=init,
    blit=True,
    interval=1000/fps
)

plt.show()
