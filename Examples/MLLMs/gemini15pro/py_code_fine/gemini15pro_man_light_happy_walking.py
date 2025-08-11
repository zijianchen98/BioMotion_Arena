
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point lights over time
# This is a simplified example and would need more frames for a smooth animation
# and realistic walking motion.  You would likely load this data from a motion capture file.

# Example coordinates for one frame (replace with your actual data)
x = np.array([10, 12, 14, 10, 14, 11, 13, 10, 14, 20, 22, 20, 22, 21, 23 ])
y = np.array([50, 60, 50, 40, 40, 30, 30, 20, 20, 20, 20, 10, 10, 0,0 ])

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 30])  # Adjust limits based on your data
ax.set_ylim([0, 70])
ax.set_aspect('equal') # Ensure correct aspect ratio
ax.set_facecolor('black') # Set background to black
scat = ax.scatter(x, y, s=20, c='white') # Initialize scatter plot with white dots

def animate(i):
    # Update the coordinates for each frame
    # Here, we just make a simple oscillatory motion, replace this with your real data
    x_new = x # + np.sin(i * 0.1)  # Example oscillation, replace with your data
    y_new = y #+ np.cos(i * 0.1)
   
    scat.set_offsets(np.c_[x_new, y_new])  # Update the scatter plot data
    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True) # Increase frames for smoothness

plt.show()


