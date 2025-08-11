
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
x = np.array([0, -1, 1, -2, 2, -1, 0, 1, -1, 0, 1, 0, -1, 0, 0])  # Initial x-coordinates
y = np.array([5, 3, 3, 1, 1, 0, 0, 0, -2, -2, -2, -4, -4, -6, -8]) # Initial y-coordinates

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])  # Set x-axis limits
ax.set_ylim([-10, 6]) # Set y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_facecolor('black') # Set black background
scat = ax.scatter(x, y, s=50, c='white')  # Scatter plot for point lights

# Animation update function
def update(frame):
    global x, y
    # Wave hand motion
    if frame < 30 : 
      x[3] -=0.1*np.sin(frame/5)
      y[3] +=0.05*np.sin(frame/5)
    elif frame < 60:
      x[3] +=0.2*np.sin((frame-30)/5)
      y[3] -=0.05*np.sin((frame-30)/5)
    elif frame < 90:
      x[3] -=0.25*np.sin((frame-60)/5)
      y[3] +=0.05*np.sin((frame-60)/5)
    elif frame < 120:
      x[3] +=0.3*np.sin((frame-90)/5)
      y[3] -=0.05*np.sin((frame-90)/5)

    scat.set_offsets(np.c_[x, y]) # Update point light positions
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=120, interval=50, blit=True)
plt.show()
