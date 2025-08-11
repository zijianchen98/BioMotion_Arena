
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified representation for a lying down posture.
# Replace with actual motion capture data or more detailed keyframes for realistic motion.
key_frames = [
    # Frame 0
    [[1, 5], [2, 4], [3, 4], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3],
     [1, 2], [2, 2], [3, 2], [1.5, 1], [2.5, 1], [1, 0], [3, 0]],

    #Frame 1 (very minor shift to simluate lying down, can be expanded further)
    [[1.1, 5], [2, 4.1], [3, 4], [0, 3.1], [1, 3], [2, 3], [3, 3.1], [4, 3],
     [1, 2], [2, 2.1], [3, 2], [1.5, 1.1], [2.5, 1], [1, 0], [3, 0.1]]
]



# Create figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_xlim([0, 5])  # Set x-axis limits
ax.set_ylim([-1, 6])  # Set y-axis limits
ax.set_facecolor('black')
scatter = ax.scatter([], [], s=20, c='white')


def animate(i):
    frame = key_frames[i % len(key_frames)] # Loop through Keyframes
    scatter.set_offsets(frame) # Set Offsets to current Keyframe coordinates
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(key_frames), interval=200, blit=True, repeat=True)


plt.show()
