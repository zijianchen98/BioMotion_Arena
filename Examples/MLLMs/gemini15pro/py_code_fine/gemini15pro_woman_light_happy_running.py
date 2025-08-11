
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need more frames and adjustments for realistic motion
# You'll likely need motion capture data or advanced animation techniques for proper biomechanical plausibility
key_frames = 5  # Number of keyframes in the animation
data = np.array([
    [[1, 5], [2, 4], [3, 5], [1, 3], [2, 2], [3, 3], [1, 1], [2, 0], [3, 1], [1.5, -1], [2.5, -1], [1, -3], [3, -3], [1.5, -5], [2.5, -5]],  # Frame 1
    [[2, 5], [3, 4], [4, 5], [2, 3], [3, 2], [4, 3], [2, 1], [3, 0], [4, 1], [2.5, -1], [3.5, -1], [2, -3], [4, -3], [2.5, -5], [3.5, -5]],  # Frame 2
    [[3, 5], [4, 4], [5, 5], [3, 3], [4, 2], [5, 3], [3, 1], [4, 0], [5, 1], [3.5, -1], [4.5, -1], [3, -3], [5, -3], [3.5, -5], [4.5, -5]],  # Frame 3
    [[4, 5], [5, 4], [6, 5], [4, 3], [5, 2], [6, 3], [4, 1], [5, 0], [6, 1], [4.5, -1], [5.5, -1], [4, -3], [6, -3], [4.5, -5], [5.5, -5]],  # Frame 4
    [[5, 5], [6, 4], [7, 5], [5, 3], [6, 2], [7, 3], [5, 1], [6, 0], [7, 1], [5.5, -1], [6.5, -1], [5, -3], [7, -3], [5.5, -5], [6.5, -5]]   # Frame 5
])

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 8]) # adjust limits as needed based on animation range
ax.set_ylim([-6, 6])
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=5)


# Animation update function
def update(frame):
    x = data[frame % key_frames, :, 0]
    y = data[frame % key_frames, :, 1]
    points.set_data(x, y)
    return points,


# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(20), interval=100, blit=True)  # Adjust frames and interval for desired duration

# For saving the animation (optional)
# ani.save('running_animation.gif', writer='imagemagick') 

plt.show()

