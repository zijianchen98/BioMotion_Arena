
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define frame rate and duration
fps = 30
duration = 2  # seconds
frame_count = fps * duration

# Create a figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define the initial positions of the point-lights
points = np.array([
    [0.45, 0.85], [0.5, 0.85], [0.55, 0.85],
    [0.3, 0.7], [0.4, 0.7], [0.5, 0.7], [0.6, 0.7], [0.7, 0.7],
    [0.35, 0.6], [0.45, 0.6], [0.5, 0.6], [0.55, 0.6], [0.65, 0.6],
    [0.4, 0.45], [0.5, 0.45], [0.6, 0.45]
])

# Define a scattering of points for the jumping animation
jump_height = 0.15
jump_frames = frame_count // 2
scattering = np.linspace(0, jump_height, jump_frames)

# Create the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def init():
    scat.set_offsets(points)
    return scat,

def animate(frame):
    jump_progress = frame if frame < jump_frames else jump_frames - (frame - jump_frames)
    displacement = scattering[jump_progress]
    
    updated_points = points.copy()
    updated_points[:, 1] += displacement
    
    scat.set_offsets(updated_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frame_count, init_func=init, blit=True, interval=1000/fps)

plt.show()
