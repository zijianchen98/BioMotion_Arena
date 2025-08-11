
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15
# Time steps
num_frames = 200
# Position arrays
x = np.zeros((num_frames, num_points))
y = np.zeros((num_frames, num_points))

# Initial positions of points to represent a happy woman waving
x[0] = [0.2, 0.4, 0.6, 0.8, 0.6, 0.8, 1.0, 0.2, 0.4, 0.6, 0.8, 0.6, 0.8, 1.0, 0.5]
y[0] = [0.1, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.1]

# Wave motion for one arm
def wave_motion(t, freq=0.03, amp=0.3):
    return amp * np.sin(2 * np.pi * freq * t)

# Populate positions over time
for t in range(1, num_frames):
    for i in range(num_points):
        if i < 5:
            x[t, i] = x[0, i]
            y[t, i] = y[0, i]
        elif i < 10:
            x[t, i] = x[0, i] + wave_motion(t)
            y[t, i] = y[0, i]
        else:
            x[t, i] = x[0, i]
            y[t, i] = y[0, i]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.axis('off')  # Turn off the axis

# Scatter plot for points
scat = ax.scatter(x[0], y[0], c='white', s=50)

def update(frame):
    scat.set_offsets(np.c_[x[frame], y[frame]])
    return scat,

# Create animation
 ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()
