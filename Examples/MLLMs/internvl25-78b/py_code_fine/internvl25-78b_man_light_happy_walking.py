
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the walking motion frames
def generate_frames():
    frames = []
    x = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3]
    y = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2]

    for i in range(10):
        frame = []
        offsets = [0, 0.2, 0.4, 0.6, 0.8, -0.2, -0.4, -0.6, -0.8, 0.1, 0.3, 0.5, 0.7, -0.1, -0.3]
        for j in range(15):
            frame.append([x[j] + offsets[j] * np.sin(np.pi * i / 5), y[j] + offsets[j] * np.cos(np.pi * i / 5)])
        frames.append(frame)
    return frames

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 6)
ax.set_ylim(1, 6)
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot([], [], 'wo', ms=10)

# Animation update function
def update(frame):
    points.set_data([p[0] for p in frame], [p[1] for p in frame])
    return points,

# Generate frames
frames = generate_frames()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=100, blit=True)

plt.axis('off')
plt.show()
