
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions over time (replace with your actual motion data)
# This is a simplified example and would need more frames and accurate data for realistic motion
num_frames = 60
joint_positions = np.zeros((15, 2, num_frames))

# Example data (replace with actual joint positions): a simple jump
for i in range(num_frames):
    # Head
    joint_positions[0, :, i] = [0.5 + i / 20, 0.9 + 0.1 * np.sin(i * 0.2)]
    # Shoulders
    joint_positions[1, :, i] = [0.3 + i / 20, 0.7 + 0.05 * np.sin(i * 0.2)]
    joint_positions[2, :, i] = [0.7 + i / 20, 0.7 + 0.05 * np.sin(i * 0.2)]
    # Elbows
    joint_positions[3, :, i] = [0.2 + i / 20, 0.5 + 0.1 * np.sin(i * 0.2)]
    joint_positions[4, :, i] = [0.8 + i / 20, 0.5 + 0.1 * np.sin(i * 0.2)]
    # Hands
    joint_positions[5, :, i] = [0.1 + i / 20, 0.3 + 0.1 * np.sin(i * 0.2 + 1)]
    joint_positions[6, :, i] = [0.9 + i / 20, 0.3 + 0.1 * np.sin(i * 0.2 + 1)]
    # Hips
    joint_positions[7, :, i] = [0.4 + i / 20, 0.4 + 0.1 * np.sin(i * 0.2)]
    joint_positions[8, :, i] = [0.6 + i / 20, 0.4 + 0.1 * np.sin(i * 0.2)]
    # Knees
    joint_positions[9, :, i] = [0.35 + i / 20, 0.2 + 0.2 * np.abs(np.sin(i * 0.2))] # knees bend more while jumping forward
    joint_positions[10, :, i] = [0.65 + i / 20, 0.2 + 0.2 * np.abs(np.sin(i * 0.2))]
    # Ankles
    joint_positions[11, :, i] = [0.35 + i / 20, 0.05 + 0.05 * np.abs(np.sin(i * 0.2+1))] 
    joint_positions[12, :, i] = [0.65 + i / 20, 0.05 + 0.05 * np.abs(np.sin(i * 0.2+1))]
    # Feet (added for a total of 15 points)
    joint_positions[13, :, i] = [0.3 + i / 20, 0 + 0.05 * np.abs(np.sin(i * 0.2 + 2))]
    joint_positions[14, :, i] = [0.7 + i / 20, 0 + 0.05 * np.abs(np.sin(i * 0.2 + 2))]

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 1) # set the x and y axis so that the figure won't change size
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black') #set background color to black
scat = ax.scatter([], [], s=20, c='white')


# Animation update function
def update(frame):
    x = joint_positions[:, 0, frame]
    y = joint_positions[:, 1, frame]
    scat.set_offsets(np.c_[x, y])
    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)


plt.show()


