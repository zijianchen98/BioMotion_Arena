
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 200

# Define the number of point lights
num_lights = 15

# Initialize positions for the point lights
positions = np.zeros((num_lights, 2, num_frames))

# Define the keyframes for the forward rolling motion
keyframes = {
    0: [(0, 0), (0, 0.1), (0, 0.2), (0, 0.3), (0, 0.4), (0, 0.5), (0, 0.6), (0, 0.7), (0, 0.8), (0, 0.9), (-0.1, 0.9), (-0.2, 0.9), (-0.3, 0.9), (-0.4, 0.9), (-0.5, 0.9)],
    50: [(-0.5, 0.8), (-0.4, 0.7), (-0.3, 0.6), (-0.2, 0.5), (-0.1, 0.4), (0, 0.3), (0, 0.2), (0, 0.1), (0, 0), (0, -0.1), (-0.1, -0.1), (-0.2, -0.1), (-0.3, -0.1), (-0.4, -0.1), (-0.5, -0.1)],
    100: [(-0.5, -0.2), (-0.4, -0.3), (-0.3, -0.4), (-0.2, -0.5), (-0.1, -0.6), (0, -0.7), (0, -0.8), (0, -0.9), (0, -1), (0, -1.1), (-0.1, -1.1), (-0.2, -1.1), (-0.3, -1.1), (-0.4, -1.1), (-0.5, -1.1)],
    150: [(-0.5, -1), (-0.4, -0.9), (-0.3, -0.8), (-0.2, -0.7), (-0.1, -0.6), (0, -0.5), (0, -0.4), (0, -0.3), (0, -0.2), (0, -0.1), (-0.1, -0.1), (-0.2, -0.1), (-0.3, -0.1), (-0.4, -0.1), (-0.5, -0.1)],
    200: [(-0.5, 0), (-0.4, 0.1), (-0.3, 0.2), (-0.2, 0.3), (-0.1, 0.4), (0, 0.5), (0, 0.6), (0, 0.7), (0, 0.8), (0, 0.9), (-0.1, 0.9), (-0.2, 0.9), (-0.3, 0.9), (-0.4, 0.9), (-0.5, 0.9)]
}

# Interpolate between keyframes
for t in range(num_frames):
    for i in range(num_lights):
        for k1, k2 in zip(sorted(keyframes.keys()), sorted(keyframes.keys())[1:]):
            if k1 <= t < k2:
                t_norm = (t - k1) / (k2 - k1)
                positions[i, :, t] = (1 - t_norm) * np.array(keyframes[k1][i]) + t_norm * np.array(keyframes[k2][i])

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')
scat = ax.scatter(positions[:, 0, 0], positions[:, 1, 0], color='white', s=100)

def update(frame):
    scat.set_offsets(np.c_[positions[:, 0, frame], positions[:, 1, frame]])

ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)
plt.show()
