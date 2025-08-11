
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the positions of the points
num_frames = 100
positions = np.zeros((num_frames, 15, 2))

# Walking pattern
pattern = np.array([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

# Generate walking pattern
for i in range(num_frames):
    for j in range(15):
        if i % 10 == 0:
            pattern[0][j] = (i // 10) % 15
        if i % 10 == 5:
            pattern[1][j] = (i // 10) % 15
        if i % 10 == 1:
            pattern[2][j] = (i // 10) % 15
        if i % 10 == 6:
            pattern[3][j] = (i // 10) % 15
        if i % 10 == 2:
            pattern[4][j] = (i // 10) % 15
        if i % 10 == 7:
            pattern[5][j] = (i // 10) % 15
        if i % 10 == 3:
            pattern[6][j] = (i // 10) % 15
        if i % 10 == 8:
            pattern[7][j] = (i // 10) % 15
        if i % 10 == 4:
            pattern[8][j] = (i // 10) % 15
        if i % 10 == 9:
            pattern[9][j] = (i // 10) % 15

    positions[i] = pattern[i % 10]

# Set up plot
fig, ax = plt.subplots()
ax.set_xlim([0, 15])
ax.set_ylim([0, 15])
ax.set_facecolor('black')

# Create scatter plot
scat = ax.scatter(positions[0, :, 0], positions[0, :, 1], c='white')

# Animation function
def animate(i):
    scat.set_offsets(positions[i])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show animation
plt.show()
