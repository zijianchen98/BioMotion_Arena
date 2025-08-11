
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint positions over time (replace with your actual motion data)
# This is a simplified example, you'll need more frames and accurate data
joint_positions = np.array([
    [[10, 50], [15, 60], [20, 70], [10, 60], [20, 60], [12, 50], [18, 50], [15, 40], [15, 30], [12, 20], [18, 20], [10, 10], [20, 10], [13, 5], [17, 5]],
    [[10, 55], [15, 65], [20, 75], [10, 65], [20, 65], [12, 55], [18, 55], [15, 45], [15, 35], [12, 25], [18, 25], [10, 15], [20, 15], [13, 10], [17, 10]],
    [[10, 60], [15, 70], [20, 80], [10, 70], [20, 70], [12, 60], [18, 60], [15, 50], [15, 40], [12, 30], [18, 30], [10, 20], [20, 20], [13, 15], [17, 15]],
    # ... more frames
])


# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 30)  # Adjust limits as needed
ax.set_ylim(0, 80)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], s=20, c='white')


# Update function for animation
def update(frame):
    x = joint_positions[frame, :, 0]
    y = joint_positions[frame, :, 1]
    scat.set_offsets(np.c_[x, y])
    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(joint_positions), interval=50, blit=True)  # Adjust interval as needed

plt.show()


# To save as a gif (requires imagemagick):
# ani.save('jumping_up.gif', writer='imagemagick', fps=20) # adjust fps as needed




