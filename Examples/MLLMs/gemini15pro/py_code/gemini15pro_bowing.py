
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions over time (example - replace with your actual data)
# This example simulates a simple bowing motion
num_frames = 60  # Number of frames in the animation
t = np.linspace(0, 1, num_frames)

head = np.array([0, 100]) + 10 * np.sin(2 * np.pi * t)[:, np.newaxis]  # Head moves up and down slightly
shoulders = np.array([-15, 80]), np.array([15, 80])
elbows = np.array([-25, 60]) + 5 * np.sin(2 * np.pi * t + 1)[:, np.newaxis], np.array([25, 60]) + 5 * np.sin(2 * np.pi * t + 1)[:, np.newaxis]
hands = np.array([-20, 40]) + 10 * np.sin(2 * np.pi * t)[:, np.newaxis], np.array([20, 40]) + 10 * np.sin(2 * np.pi * t)[:, np.newaxis]
hips = np.array([-10, 40]), np.array([10, 40])
knees = np.array([-10, 20]), np.array([10, 20])
feet = np.array([-10, 0]), np.array([10, 0])

# Combine joint positions into a single list of lists for each frame
joint_positions = []
for i in range(num_frames):
    frame_positions = [
        head[i], shoulders[0], shoulders[1], elbows[0][i], elbows[1][i],
        hands[0][i], hands[1][i], hips[0], hips[1], knees[0], knees[1],
        feet[0], feet[1]
    ]
    joint_positions.append(frame_positions)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-50, 50])
ax.set_ylim([-10, 120])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-light scatter plot
scatter = ax.scatter([], [], s=20, c='white')

# Update function for the animation
def update(frame):
    x = [pos[0] for pos in joint_positions[frame]]
    y = [pos[1] for pos in joint_positions[frame]]
    scatter.set_offsets(np.c_[x, y])
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)

plt.show()
