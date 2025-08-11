
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define point light positions for a bowing motion
def get_bowing_frames():
    frames = []
    offset = 0.0

    # Initial upright position
    positions = np.array([
        [0, 1], [0.2, 1], [0.4, 1], [0.6, 1], [0.8, 1],
        [0.1, 0.7], [0.3, 0.7], [0.5, 0.7], [0.7, 0.7], [0.9, 0.7],
        [0, 0.5], [0.2, 0.5], [0.4, 0.5], [0.6, 0.5], [0.8, 0.5]
    ])
    frames.append(positions)

    for i in range(15):
        # Create bowing motion by gradually changing y-coordinates
        positions[:, 1] -= 0.02
        frames.append(positions.copy())

    # Return to upright position
    for i in range(15):
        positions[:, 1] += 0.02
        frames.append(positions.copy())

    return frames

# Create the animation
fig, ax = plt.subplots()
ax.set facecolor('black')
ax.set_xlim(-1, 1.5)
ax.set_ylim(0, 1.2)

frames = get_bowing_frames()
scat = ax.scatter(frames[0][:, 0], frames[0][:, 1], c='white', s=50)

def update(frame):
    scat.set_offsets(frames[frame])
    return scat,

ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=50)

plt.axis('off')
plt.show()
