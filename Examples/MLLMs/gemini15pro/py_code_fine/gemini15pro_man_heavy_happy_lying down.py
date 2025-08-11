
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
num_frames = 60
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example: Head (point 0) moves slightly
x[0,:] = 10 + np.sin(np.linspace(0, 2*np.pi, num_frames)) * 2
y[0,:] = 40 + np.cos(np.linspace(0, 2*np.pi, num_frames)) * 2

# Example: Shoulders (points 1 and 2)
x[1,:] = 5 + np.sin(np.linspace(0, 2*np.pi, num_frames))
y[1,:] = 35
x[2,:] = 15 + np.sin(np.linspace(0, 2*np.pi, num_frames))
y[2,:] = 35

# ... define similar movements for the other 12 points ...
# Make sure they move accordingly to represent "happyman lying down"
# This might involve rotations, translations, etc.

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 20)  # Adjust limits as needed
ax.set_ylim(0, 50)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points, = ax.plot([], [], 'wo', markersize=5)

# Animation function
def animate(i):
  points.set_data(x[:, i], y[:, i])
  return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=20, blit=True)

# For saving the animation, uncomment the following
# writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
# ani.save('lying_down.mp4', writer=writer)


plt.show()

