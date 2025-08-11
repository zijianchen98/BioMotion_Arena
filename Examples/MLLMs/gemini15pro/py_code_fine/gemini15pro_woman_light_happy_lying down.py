
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
num_frames = 60  # Number of frames in the animation
dots_x = []
dots_y = []

for frame in range(num_frames):

    head_x = 2.5 + np.sin(frame/15) * .2
    head_y = 7 + np.cos(frame/30) * 0.15

    shoulder_left_x = 2 + np.sin(frame / 15) * .1
    shoulder_left_y = 6

    shoulder_right_x = 3 + np.sin(frame / 15) * .1
    shoulder_right_y = 6


    elbow_left_x = 1 + np.sin(frame / 15) * .1
    elbow_left_y = 5

    elbow_right_x = 4 + np.sin(frame / 15) * .1
    elbow_right_y = 5



    hand_left_x = 1 + np.sin(frame/15) *.1
    hand_left_y = 4


    hand_right_x = 4 + np.sin(frame/15) *.1
    hand_right_y = 4


    hip_left_x = 2
    hip_left_y = 3


    hip_right_x = 3
    hip_right_y = 3

    knee_left_x = 2
    knee_left_y = 2
    knee_right_x = 3
    knee_right_y = 2

    foot_left_x = 2
    foot_left_y = 1
    foot_right_x = 3
    foot_right_y = 1



    dots_x.append([head_x, shoulder_left_x, shoulder_right_x, elbow_left_x, elbow_right_x,hand_left_x, hand_right_x, hip_left_x, hip_right_x,knee_left_x, knee_right_x, foot_left_x,foot_right_x ])
    dots_y.append([head_y, shoulder_left_y,shoulder_right_y, elbow_left_y, elbow_right_y, hand_left_y, hand_right_y, hip_left_y, hip_right_y, knee_left_y,knee_right_y, foot_left_x,foot_right_y])



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0,5])
ax.set_ylim([0, 8])
ax.set_aspect('equal')
ax.set_facecolor('black')
scatter = ax.scatter([], [], s=30, c='white')



# Animation update function
def update(frame):
    x = dots_x[frame]
    y = dots_y[frame]
    scatter.set_offsets(np.c_[x, y])
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(num_frames), interval=40, blit=True)



plt.show()

