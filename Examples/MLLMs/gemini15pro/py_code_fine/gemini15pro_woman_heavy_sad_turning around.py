
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be replaced with real motion capture data
# for accurate and biomechanically plausible movement.  This example just "wobbles" the points.


def animate(i):
    ax.clear()
    ax.set_xlim(-100, 100)  # Set limits to keep the points visible as they move.
    ax.set_ylim(-150, 150)
    x = np.array([20, -20, 0, 30, -30, 25, -25, 15, -15, 40+5*np.sin(i/5), -40+5*np.cos(i/5), 45+5*np.cos(i/4), -45+5*np.sin(i/4), 55+5*np.cos(i/2),-55+5*np.sin(i/2) ])
    y = np.array([120, 120, 100, 50, 50, 30, 30, 0, 0, -50+20*np.sin(i/10), -50+20*np.cos(i/10), -80+20*np.sin(i/6), -80+20*np.cos(i/6), -120, -120])


    ax.scatter(x, y, s=30, c='white') # s controls the size of the dots
    ax.set_facecolor('black')


    return []

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xticks([]) # remove x ticks
ax.set_yticks([]) # remove y ticks



# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=30, blit=True)  # frames, interval control animation length and speed


plt.show()




