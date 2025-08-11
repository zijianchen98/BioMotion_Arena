
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define the initial positions of the points
positions = np.array([
    [5, 4], [4.8, 4.5], [5.2, 4.5],  # head
    [4, 5], [5, 5], [6, 5],  # shoulders
    [4, 6], [5, 6], [6, 6],  # hips
    [3, 7], [4, 7], [6, 7], [7, 7],  # legs
    [4.5, 7.5], [5.5, 7.5]  # feet
])

# Create point objects
points, = ax.plot(positions[:, 0], positions[:, 1], 'wo')

def update(frame):
    # Update positions based on the walking motion
    if frame % 20 < 10:
        positions[6:10, 0] += 0.1  # right leg forward
        positions[10:14, 0] -= 0.1  # left leg backward
    else:
        positions[6:10, 0] -= 0.1  # right leg backward
        positions[10:14, 0] += 0.1  # left leg forward

    positions[3:6, 0] += 0.05 * np.sin(frame / 10)  # shoulders swing
    positions[9:11, 1] += 0.05 * np.sin(frame / 10)  # body up and down

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
