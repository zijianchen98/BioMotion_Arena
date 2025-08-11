
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions over time (example data - replace with your actual motion capture data)
# Each frame contains the (x, y) coordinates of 15 joints
frames = [
    # Frame 1
    np.array([[10, 50], [15, 45], [20, 50], [5, 40], [25, 40], [10, 35], [15, 30], [20, 35], [5, 25], [25, 25], [12, 15], [18, 15], [10, 5], [15, 0], [20, 5]]),
    # Frame 2 (slightly moved)
    np.array([[11, 52], [16, 47], [21, 52], [6, 42], [26, 42], [11, 37], [16, 32], [21, 37], [6, 27], [26, 27], [13, 17], [19, 17], [11, 7], [16, 2], [21, 7]]),

      # more frames with varied positions, simulating jumping motion

      np.array([[30, 50], [35, 45], [40, 50], [25, 40], [45, 40], [30, 35], [35, 30], [40, 35], [25, 25], [45, 25], [32, 15], [38, 15], [30, 5], [35, 0], [40, 5]]) #Final frame
]


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 50])  # Set x-axis limits
ax.set_ylim([-5, 55])  # Set y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_facecolor('black')  # Set background color to black
scatter = ax.scatter([], [], s=20, c='white') # Initialize scatter plot


# Animation update function
def animate(i):
    x = frames[i][:, 0] #extract x coordinates
    y = frames[i][:, 1] #extract y coordinates
    scatter.set_offsets(np.c_[x,y])
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=50, blit=True)


# Display the animation (or save as a video file)
plt.show()



# To save as video (uncomment the following lines):
# writer = animation.writers['ffmpeg'](fps=20) # Adjust fps as needed
# ani.save('jumping_animation.mp4', writer=writer)

