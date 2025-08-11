
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
# Each point is represented by a list of [x, y] coordinates for each frame
num_frames = 60
dots = []

# Example data for the head
head_x = np.linspace(200, 200, num_frames)
head_y = np.linspace(400, 350, num_frames)
dots.append([head_x, head_y])


# Example data for shoulders
shoulder_left_x = np.linspace(175, 175, num_frames)
shoulder_left_y = np.linspace(350, 320, num_frames)

shoulder_right_x = np.linspace(225, 225, num_frames)
shoulder_right_y = np.linspace(350, 320, num_frames)

dots.append([shoulder_left_x, shoulder_left_y])
dots.append([shoulder_right_x, shoulder_right_y])

# Example data for elbows
elbow_left_x = np.linspace(150, 150, num_frames)
elbow_left_y = np.linspace(300, 300, num_frames)

elbow_right_x = np.linspace(250, 250, num_frames)
elbow_right_y = np.linspace(300, 300, num_frames)


dots.append([elbow_left_x, elbow_left_y])
dots.append([elbow_right_x, elbow_right_y])




# Example data for the hips
hip_left_x = np.linspace(175, 175, num_frames)
hip_left_y = np.linspace(250, 230, num_frames)

hip_right_x = np.linspace(225, 225, num_frames)
hip_right_y = np.linspace(250, 230, num_frames)
dots.append([hip_left_x, hip_left_y])

dots.append([hip_right_x, hip_right_y])



# Example data for the knees
knee_left_x = np.linspace(175, 175, num_frames)
knee_left_y = np.linspace(175, 150, num_frames)


knee_right_x = np.linspace(225, 225, num_frames)
knee_right_y = np.linspace(175, 150, num_frames)

dots.append([knee_left_x, knee_left_y])

dots.append([knee_right_x, knee_right_y])



# Example data for the feet
feet_left_x = np.linspace(175, 175, num_frames)
feet_left_y = np.linspace(100, 75, num_frames)
feet_right_x = np.linspace(225, 225, num_frames)

feet_right_y = np.linspace(100, 75, num_frames)
dots.append([feet_left_x, feet_left_y])
dots.append([feet_right_x, feet_right_y])


wrists_left_x=np.linspace(150,160,num_frames)
wrists_left_y = np.linspace(250,240, num_frames)

wrists_right_x= np.linspace(250,240, num_frames)
wrists_right_y=np.linspace(250,240,num_frames)

dots.append([wrists_left_x, wrists_left_y])
dots.append([wrists_right_x, wrists_right_y])



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(50,350)
ax.set_ylim(0, 450)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-light scatter plot
scat = ax.scatter([], [], s=30, c='white')

# Update function for the animation
def update(frame):
    x = [dots[i][0][frame] for i in range(len(dots))]
    y = [dots[i][1][frame] for i in range(len(dots))]
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)


plt.show()

