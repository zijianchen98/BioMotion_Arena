
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need more frames and precise data for realistic motion
# Data would ideally come from motion capture or similar techniques
num_frames = 60

x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example: Head swaying slightly
x[0, :] = 0 + np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 2  # Head top
y[0, :] = 100 + np.cos(np.linspace(0, 2 * np.pi, num_frames)) * 1

# Example: Shoulders moving with a weight 
x[1, :] = -10 + np.sin(np.linspace(0, np.pi, num_frames)) * 5   # Left shoulder
y[1, :] = 80  - np.abs(np.sin(np.linspace(0, 2*np.pi, num_frames))) * 15

x[2, :] = 10 + np.sin(np.linspace(0, np.pi, num_frames)) * 5    # Right shoulder
y[2, :] = 80 - np.abs(np.cos(np.linspace(0, 2*np.pi, num_frames))) * 15


# ... (Similarly define motion for all other 12 points)
# Elbows, wrists, hips, knees, ankles




# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)
ax.set_ylim(0, 120)  # Adjust limits as needed
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background to black
scatter = ax.scatter([], [], s=20, c='white') # Initialize scatter plot


# Animation update function
def animate(i):
    scatter.set_offsets(np.c_[x[:, i], y[:, i]])
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=30, blit=True)


# For saving, uncomment below:  Requires appropriate writer, e.g., imagemagick
# writer = animation.ImageMagickWriter(fps=30)  # Or use other writers like PillowWriter, ffmpeg
# ani.save('sad_walking.gif', writer=writer) 

plt.show()
