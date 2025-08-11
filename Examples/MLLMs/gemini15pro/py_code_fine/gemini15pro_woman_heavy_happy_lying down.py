
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be fleshed out for realistic motion
# Each point is represented by a tuple: (x, y)
# Each frame is a list of these tuples

num_frames = 60  # Number of frames in the animation

data = []
for i in range(num_frames):
    frame_data = []
    # Head
    head_x = 0.5 + 0.05 * np.sin(i * 2 * np.pi / num_frames) # Example head movement
    head_y = 0.9 + 0.02 * np.cos(i * 2 * np.pi / num_frames)
    frame_data.append((head_x, head_y))

    # Shoulders
    shoulder_width = 0.2
    frame_data.append((head_x - shoulder_width/2, head_y - 0.1 ))
    frame_data.append((head_x + shoulder_width/2, head_y - 0.1 ))


    # Elbows
    elbow_offset = 0.15
    frame_data.append((head_x - shoulder_width/2 - elbow_offset/2 * np.cos(i * 2 * np.pi / num_frames), head_y - 0.25)) # Example elbow movement
    frame_data.append((head_x + shoulder_width/2 + elbow_offset/2*np.cos(i*2*np.pi/num_frames) , head_y - 0.25))

    # Hips
    hip_width = 0.15
    frame_data.append((head_x - hip_width/2, head_y - 0.4))
    frame_data.append((head_x + hip_width/2, head_y - 0.4))


    # Knees
    knee_offset = 0.2
    frame_data.append((head_x - hip_width/2 + knee_offset/4 * np.cos(i * 2 * np.pi / num_frames), head_y - 0.65))
    frame_data.append((head_x + hip_width/2 - knee_offset/4* np.cos(i*2*np.pi/num_frames), head_y - 0.65))


    # Hands
    frame_data.append((frame_data[3][0] + elbow_offset/2 * np.sin(i * 2 * np.pi / num_frames), frame_data[3][1] - 0.1))
    frame_data.append((frame_data[4][0] - elbow_offset/2 * np.sin(i * 2 * np.pi / num_frames), frame_data[4][1] - 0.1))


    # Feet
    frame_data.append((frame_data[7][0] + knee_offset / 2 * np.cos(i * 2 * np.pi / num_frames), frame_data[7][1] - 0.1))
    frame_data.append((frame_data[8][0] - knee_offset / 2 * np.cos(i * 2 * np.pi / num_frames), frame_data[8][1] - 0.1 ))

    # Torso 
    frame_data.append((head_x, head_y-0.2))
    frame_data.append((head_x, head_y-0.3))
    frame_data.append((head_x, head_y-0.45))


    data.append(frame_data)



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 1)  # x and y from 0 to 1 makes normalized units useful
ax.set_ylim(0, 1)  # x and y from 0 to 1 makes normalized units useful

ax.set_aspect('equal')  # Important for proper point-light display
ax.set_facecolor('black')


# Initialize the points
points, = ax.plot([], [], 'wo')


# Update function for the animation
def update(frame):
    x = [point[0] for point in data[frame]]
    y = [point[1] for point in data[frame]]
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# If you want to save it to a .mp4 file.
# ani.save('point_light_animation.mp4')


plt.show()

