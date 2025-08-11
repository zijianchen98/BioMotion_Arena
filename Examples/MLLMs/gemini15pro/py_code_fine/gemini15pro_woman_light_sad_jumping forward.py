
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be refined for realistic motion
# Each point is represented by a tuple (x, y)
# Each frame is a list of 15 tuples

num_frames = 30
x_center = 0  # Initial x-coordinate of the center of the figure

point_lights = []
for frame in range(num_frames):
    frame_data = []
    y_offset = np.sin(frame / num_frames * 2 * np.pi) * 20 # Simulate vertical jump motion
    x_offset = frame * 5 # Simulate forward motion
    
    # Head
    frame_data.append((x_center + x_offset, 100 + y_offset))

    # Shoulders
    frame_data.append((x_center - 10 + x_offset, 80 + y_offset))
    frame_data.append((x_center + 10 + x_offset, 80 + y_offset))

    # Elbows
    frame_data.append((x_center - 20 + x_offset, 60 + y_offset))
    frame_data.append((x_center + 20 + x_offset, 60 + y_offset))

    # Hands
    frame_data.append((x_center - 25 + x_offset, 40 + y_offset))
    frame_data.append((x_center + 25 + x_offset, 40 + y_offset))
    
    # Hips
    frame_data.append((x_center - 10 + x_offset, 40 + y_offset))
    frame_data.append((x_center + 10 + x_offset, 40 + y_offset))

    # Knees
    frame_data.append((x_center - 15 + x_offset, 20 + y_offset ))
    frame_data.append((x_center + 15 + x_offset, 20 + y_offset))

    # Feet
    frame_data.append((x_center - 20 + x_offset, 0 + y_offset))
    frame_data.append((x_center + 20 + x_offset, 0 + y_offset))

    # Spine base and mid-spine
    frame_data.append((x_center + x_offset, 60 + y_offset)) # Mid-spine
    frame_data.append((x_center + x_offset, 40 + y_offset))


    point_lights.append(frame_data)



# Create the animation
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(-50, 200) # Adjust limits for full jump visualization
ax.set_ylim(-20, 120)
scatter = ax.scatter([], [], s=20, c='white') # s controls marker size

def animate(i):
    x = [point[0] for point in point_lights[i]]
    y = [point[1] for point in point_lights[i]]
    scatter.set_offsets(np.c_[x, y])
    return scatter,


ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, interval = 100)

plt.show()


