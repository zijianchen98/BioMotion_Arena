
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of point-lights
num_lights = 15

# Initialize positions of the point-lights
positions = np.zeros((num_frames, num_lights, 2))

# Define the keyframes for the running motion
keyframes = {
    0: [(0.5, 0.8), (0.4, 0.7), (0.6, 0.7), (0.3, 0.6), (0.7, 0.6), (0.2, 0.5), (0.8, 0.5),
        (0.3, 0.4), (0.7, 0.4), (0.4, 0.3), (0.6, 0.3), (0.4, 0.2), (0.6, 0.2), (0.5, 0.1), (0.5, 0.9)],
    25: [(0.5, 0.9), (0.4, 0.8), (0.6, 0.8), (0.3, 0.7), (0.7, 0.7), (0.2, 0.6), (0.8, 0.6),
         (0.3, 0.5), (0.7, 0.5), (0.4, 0.4), (0.6, 0.4), (0.4, 0.3), (0.6, 0.3), (0.5, 0.2), (0.5, 0.8)],
    50: [(0.5, 0.8), (0.4, 0.9), (0.6, 0.9), (0.3, 0.8), (0.7, 0.8), (0.2, 0.7), (0.8, 0.7),
         (0.3, 0.6), (0.7, 0.6), (0.4, 0.5), (0.6, 0.5), (0.4, 0.4), (0.6, 0.4), (0.5, 0.3), (0.5, 0.7)],
    75: [(0.5, 0.7), (0.4, 0.8), (0.6, 0.8), (0.3, 0.7), (0.7, 0.7), (0.2, 0.6), (0.8, 0.6),
         (0.3, 0.5), (0.7, 0.5), (0.4, 0.4), (0.6, 0.4), (0.4, 0.3), (0.6, 0.3), (0.5, 0.2), (0.5, 0.6)]
}

# Interpolate positions between keyframes
for i in range(num_frames):
    t = i / (num_frames - 1)
    for j in range(num_lights):
        keys = sorted(keyframes.keys())
        k0, k1 = keys[int(t * (len(keys) - 1))], keys[int(t * (len(keys) - 1)) + 1]
        t_local = (t - k0 / (num_frames - 1)) / ((k1 - k0) / (num_frames - 1))
        pos0, pos1 = keyframes[k0][j], keyframes[k1][j]
        positions[i, j] = (1 - t_local) * np.array(pos0) + t_local * np.array(pos1)

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter(positions[0, :, 0], positions[0, :, 1], s=100, c='white')

def update(frame):
    scatter.set_offsets(positions[frame])

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)
plt.show()
