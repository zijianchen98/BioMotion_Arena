
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
num_frames = 60  # Number of frames in the animation
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example motion: Head (point 0) moving down slightly
x[0, :] = 0
y[0, :] = np.linspace(0, -0.2, num_frames)

# Example motion: Shoulders (points 1 and 2) moving down and slightly inward
x[1, :] = np.linspace(0.2, 0.1, num_frames)
y[1, :] = np.linspace(0, -0.3, num_frames)
x[2, :] = np.linspace(-0.2, -0.1, num_frames)
y[2, :] = np.linspace(0, -0.3, num_frames)


# Example motion: Elbows (points 3 and 4) moving down and forward 
x[3, :] = np.linspace(0.3, 0.4, num_frames)
y[3, :] = np.linspace(-0.2, -0.5, num_frames)

x[4, :] = np.linspace(-0.3, -0.4, num_frames)
y[4, :] = np.linspace(-0.2, -0.5, num_frames)

# Example motion: Hands (points 5 and 6) moving towards the knees
x[5, :] = np.linspace(0.3, 0.2, num_frames)
y[5, :] = np.linspace(-0.5, -0.8, num_frames)
x[6, :] = np.linspace(-0.3, -0.2, num_frames)
y[6, :] = np.linspace(-0.5, -0.8, num_frames)

# Example motion: Hips (points 7 and 8) moving down and spreading slightly
x[7, :] = np.linspace(0.1, 0.15, num_frames)
y[7, :] = np.linspace(-0.6, -0.9, num_frames)
x[8, :] = np.linspace(-0.1, -0.15, num_frames)
y[8, :] = np.linspace(-0.6, -0.9, num_frames)


# Example motion: Knees (points 9 and 10) moving down and spreading slightly
x[9, :] = np.linspace(0.2, 0.25, num_frames)
y[9, :] = np.linspace(-1, -1.4, num_frames)
x[10, :] = np.linspace(-0.2, -0.25, num_frames)
y[10, :] = np.linspace(-1, -1.4, num_frames)

# Example motion: Feet (points 11 and 12) staying relatively still


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-1, 1])  # Set x-axis limits
ax.set_ylim([-1.5, 0.5])  # Set y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_facecolor('black')  # Set background color to black
scatter = ax.scatter([], [], s=20, c='white')  # Create scatter plot for points

# Animation update function
def update(frame):
    scatter.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=40, blit=True)


plt.show()
