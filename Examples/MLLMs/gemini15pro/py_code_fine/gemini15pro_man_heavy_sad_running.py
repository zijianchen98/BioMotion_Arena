
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
# Each point is represented by a tuple (x, y)
# Each frame is a list of 15 such tuples
frames = []
for i in range(20): # 20 frames of animation
    frame = []
    # Head
    frame.append((100 + i*2, 350))
    # Shoulders
    frame.append((80 + i*2, 320))
    frame.append((120 + i*2, 320))
    # Elbows
    frame.append((70 + i*2 + 10*np.sin(i*0.5), 280))
    frame.append((130 + i*2 + 10*np.sin(i*0.5), 280))
    # Wrists 
    frame.append((70 + i*2 + 15 *np.sin(i*0.7), 240))
    frame.append((130 + i*2 + 15 *np.sin(i*0.7), 240))


    # Hips
    frame.append((90+ i*2, 200))
    frame.append((110 + i*2, 200 ))
    # Knees
    frame.append((80 + i*2 + 20*np.sin(i), 150))
    frame.append((120 + i*2 + 20*np.sin(i + 1), 150))
    # Ankles
    frame.append((90 + i*2+ 10*np.sin(i*1.2), 100 ))
    frame.append((110 + i*2+ 10*np.sin(i*1.2+1), 100))
    # Feet
    frame.append((85 + i*2 + 15*np.sin(i*1.5), 70))
    frame.append((115+ i*2 + 15*np.sin(i*1.5 +1), 70))

    frames.append(frame)



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 200)  # Adjust limits as needed
ax.set_ylim(0, 400)
ax.set_aspect('equal')  # Ensure points are circular
ax.set_facecolor('black')  # Set background to black

# Create the point-light scatter plot
scatter = ax.scatter([], [], s=20, c='white')

# Animation update function
def update(frame_num):
    x = [point[0] for point in frames[frame_num]]
    y = [point[1] for point in frames[frame_num]]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=50, blit=True) # interval controls speed

# Save the animation as a GIF (optional)
# ani.save('running_man.gif', writer='imagemagick', fps=20)


# Display the animation 
plt.show()
