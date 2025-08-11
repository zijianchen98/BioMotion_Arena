
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint positions over time (replace with your actual motion data)
# This is a simplified example, you'll need more frames and realistic motion
num_frames = 60  # Example number of frames

joint_positions = np.zeros((15, 2, num_frames)) # 15 joints, 2D coordinates, over time


# Example Motion - bowing with a heavy weight (adjust as needed)
def bowing_motion(t):
    center_x = 250
    center_y = 250

    head_x = center_x
    head_y = center_y + 70 + 20 * np.sin(t * 0.15) 
    joint_positions[0, :, t] = [head_x, head_y]

    shoulder_x = center_x
    shoulder_y = center_y + 40 + 15 * np.sin(t * 0.15)
    joint_positions[1, :, t] = [shoulder_x - 20, shoulder_y]
    joint_positions[2, :, t] = [shoulder_x + 20, shoulder_y]

    elbow_x = center_x
    elbow_y = center_y + 10 + 10 * np.sin(t * 0.15 + 0.5)
    joint_positions[3, :, t] = [elbow_x - 40, elbow_y]
    joint_positions[4, :, t] = [elbow_x + 40 , elbow_y ]

    hand_x = center_x
    hand_y = center_y -20 + 5 * np.sin(t*0.15 + 1)
    joint_positions[5, :, t] = [hand_x - 60 + 10 * np.sin(t * 0.15 + 1), hand_y]
    joint_positions[6, :, t] = [hand_x + 60 + 10* np.sin(t * 0.15+1), hand_y]


    hip_x = center_x 
    hip_y = center_y + 5 + 5* np.sin(t * 0.1)
    joint_positions[7, :, t] = [hip_x-20, hip_y]
    joint_positions[8, :, t] = [hip_x + 20, hip_y]

    knee_x = center_x
    knee_y = center_y - 30
    joint_positions[9, :, t] = [knee_x - 20, knee_y]
    joint_positions[10, :, t] = [knee_x + 20, knee_y]


    ankle_x = center_x
    ankle_y = center_y - 60
    joint_positions[11, :, t] = [ankle_x - 20, ankle_y]
    joint_positions[12, :, t] = [ankle_x + 20, ankle_y]

    foot_x = center_x 
    foot_y = center_y - 70
    joint_positions[13,:,t] = [foot_x - 30, foot_y]
    joint_positions[14,:,t] = [foot_x + 30, foot_y]




for t in range(num_frames):
    bowing_motion(t)





# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 500) # Adjust window size
ax.set_ylim(0, 500)
ax.set_aspect('equal')  # Important for proper display of body proportions
ax.set_facecolor('black') # Set background color

# Create the point-light scatter plot
scatter = ax.scatter([], [], s=20, c='white')  # s controls marker size

# Animation update function
def update(frame):
    x = joint_positions[:, 0, frame]
    y = joint_positions[:, 1, frame]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=40, blit=True) # adjust interval for speed


plt.show()


