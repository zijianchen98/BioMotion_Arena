
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the frames for the sadman waving action
# Simplified representation as a series of xy coordinates
# Data should be based on actual motion capture data or a coherent biomechanical model
frames = [
    np.array([(1, 1), (2, 1), (3, 2), (2, 3), (1, 2), (2, 2), 
              (3, 1), (4, 1), (5, 2), (4, 3), (3, 2), (4, 2), 
              (5, 1), (6, 1), (7, 2)]),
    # ... more frames here ...
    np.array([(1, 1), (2, 1), (3, 3), (2, 2), (1, 2), (2, 2),
              (3, 1), (4, 1), (5, 3), (4, 2), (3, 2), (4, 2),
              (5, 1), (6, 1), (7, 3)])
]

# Create new frames using interpolation for smooth animation if needed
num_intermediate_frames = 5
all_frames = []

for i in range(len(frames) - 1):
    start_frame = frames[i]
    end_frame = frames[i + 1]
    for t in np.linspace(0, 1, num_intermediate_frames, endpoint=False):
        interpolated_frame = (1 - t) * start_frame + t * end_frame
        all_frames.append(interpolated_frame)

# Final frame
all_frames.append(frames[-1])

# Create the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_aspect('equal')

scatter = ax.scatter([], [])

def init():
    scatter.set_offsets([])
    return scatter,

def animate(i):
    data = all_frames[i]
    scatter.set_offsets(data)
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=len(all_frames), init_func=init, blit=True, repeat=True)

plt.show()
