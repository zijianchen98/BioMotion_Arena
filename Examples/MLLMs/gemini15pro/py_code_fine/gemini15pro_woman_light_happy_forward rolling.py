
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions for each frame (replace with your actual data)
# This is a simplified example, you'll need more frames and precise coordinates
joint_positions = np.array([
    [[10, 50], [15, 45], [20, 40], [12, 35], [18, 35], [10, 30], [15, 30], [20, 30], [12, 25], [18, 25], [15, 20], [15, 15], [13, 10], [17, 10], [15, 5]],  # Frame 1
    [[12, 52], [17, 47], [22, 42], [14, 37], [20, 37], [12, 32], [17, 32], [22, 32], [14, 27], [20, 27], [17, 22], [17, 17], [15, 12], [19, 12], [17, 7]],  # Frame 2
    # ... more frames ...
])


num_frames = len(joint_positions)
num_joints = joint_positions.shape[1]

fig, ax = plt.subplots()
ax.set_xlim(0, 30)  # Set appropriate limits for your data
ax.set_ylim(0, 60)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=5)


def animate(i):
    x = joint_positions[i, :, 0]
    y = joint_positions[i, :, 1]
    points.set_data(x, y)
    return points,


ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

plt.show()


