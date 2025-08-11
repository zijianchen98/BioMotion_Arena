
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be replaced with actual motion capture data or similar for realistic movement
num_frames = 60  # Number of frames in the animation
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example movement: simple oscillation (replace with realistic walking motion)
for i in range(15):
    x[i, :] = i * 10 + 5 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
    y[i, :] = i * 10 + 2 * np.cos(np.linspace(0, 2 * np.pi, num_frames))


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 150)
ax.set_ylim(0, 150)
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background color to black

# Create the point-light scatter plot
scatter = ax.scatter(x[:, 0], y[:, 0], s=30, c='white')  # s controls marker size


# Update function for the animation
def update(frame):
    scatter.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, interval=30)  # interval controls speed

# Display the animation (optional, can save to file instead)
plt.show()


# To save the animation as a GIF or MP4 (requires imagemagick or ffmpeg):
# writer = animation.PillowWriter(fps=30) # For GIF
# ani.save("walking_animation.gif", writer=writer)
# writer = animation.FFMpegWriter(fps=30) # For MP4
# ani.save("walking_animation.mp4", writer=writer)

