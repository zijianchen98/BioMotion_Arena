
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need adjustments for realistic motion
# Each point is represented by a tuple (x, y)
# Each frame is a list of tuples
frames = [
    [(1, 5), (2, 4), (3, 4), (1, 3), (3, 3), (1, 2), (2, 2), (3, 2), (2, 1), (4, 1), (2, 0), (3, 0), (1, -1), (2, -2), (3, -2)],  # Initial frame
    [(2, 5), (3, 4), (4, 4), (2, 3), (4, 3), (2, 2), (3, 2), (4, 2), (3, 1), (5, 1), (3, 0), (4, 0), (2, -1), (3, -2), (4, -2)],  # Frame 2 -  Slight shift to the right (forward jump)
    [(3, 5), (4, 4), (5, 4), (3, 3), (5, 3), (3, 2), (4, 2), (5, 2), (4, 1), (6, 1), (4, 0), (5, 0), (3, -1), (4, -2), (5, -2)],  # Frame 3 - Further shift to the right
     # ... more frames showing upward then downward movement ...
     # Landing frames:
    [(6, 5), (7, 4), (8, 4), (6, 3), (8, 3), (6, 2), (7, 2), (8, 2), (7, 1), (9, 1), (7, 0), (8, 0), (6, -1), (7, -2), (8, -2)], #... 
    [(7, 5), (8, 4), (9, 4), (7, 3), (9, 3), (7, 2), (8, 2), (9, 2), (8, 1), (10, 1), (8, 0), (9, 0), (7, -1), (8, -2), (9, -2)],
    [(8, 5), (9, 4), (10, 4), (8, 3), (10, 3), (8, 2), (9, 2), (10, 2), (9, 1), (11, 1), (9, 0), (10, 0), (8, -1), (9, -2), (10, -2)],
]

# Create figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')  # Important for proper point display
ax.set_xlim(0, 12)    # Set limits according to your data range
ax.set_ylim(-3, 6) 
ax.set_facecolor('black') # Set black background

# Initialize scatter plot
scatter = ax.scatter([], [], s=20, c='white') # s controls marker size


# Animation update function
def update(frame_num):
    x = [point[0] for point in frames[frame_num]]
    y = [point[1] for point in frames[frame_num]]
    scatter.set_offsets(np.c_[x, y]) # Update point coordinates
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=100, blit=True) # Adjust interval (ms) for speed

# For displaying in a Jupyter Notebook
#from IPython.display import HTML
#HTML(ani.to_jshtml())

# Or, save as a GIF or MP4
#ani.save('jumping_animation.gif', writer='imagemagick') # Requires imagemagick
#ani.save('jumping_animation.mp4', writer='ffmpeg') # Requires ffmpeg

plt.show() # Show the animation in a separate window




