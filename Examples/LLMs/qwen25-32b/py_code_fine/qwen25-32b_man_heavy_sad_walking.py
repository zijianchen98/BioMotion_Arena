
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the coordinates of the point-lights for each frame
def get_coordinates(frame):
    # Simplified model for walking motion with heavy weight
    angle = 2 * np.pi * frame / num_frames
    x = [np.sin(angle), np.cos(angle), 0, 0, -np.sin(angle), -np.cos(angle)]
    y = [0.5 * np.cos(angle), 0.5 * np.sin(angle), 0, 0, 0.5 * np.cos(angle), 0.5 * np.sin(angle)]
    z = [0] * 6
    
    # Adding more points to make it 15
    x.extend([0.2 * np.sin(angle + i * np.pi / 3) for i in range(9)])
    y.extend([0.2 * np.cos(angle + i * np.pi / 3) for i in range(9)])
    z.extend([0] * 9)
    
    return x, y, z

# Set up the figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide the axis

# Create a scatter plot for the point-lights
scat = ax.scatter([], [], s=100, c='white')

# Animation function
def animate(frame):
    x, y, _ = get_coordinates(frame)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

plt.show()
