
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
# Each point is represented by a tuple (x, y)
# Each frame is a list of 15 tuples


def animate(i):
    ax.clear()
    ax.set_xlim(-100,100)
    ax.set_ylim(-150, 50)
    ax.set_aspect('equal')  # Important for correct aspect ratio of points
    ax.set_facecolor('black') # Black background

    x = [0] * 15
    y = [0] * 15


    # Head
    x[0] = 0
    y[0] = 40


    # Shoulders
    x[1] = -20
    y[1] = 20

    x[2] = 20
    y[2] = 20

    # Elbows
    x[3] = -30 + 10*np.sin(i*0.1)
    y[3] = 0

    x[4] = 30
    y[4] = 0

    # Hands

    x[5] = -40 + 15*np.sin(i*0.1)
    y[5] = -20

    x[6] = 30
    y[6] = -20



    # Hip

    x[7] = -10
    y[7] = -40

    x[8] = 10
    y[8] = -40

    # Knee

    x[9] = -15
    y[9] = -90


    x[10] = 15
    y[10] = -90

    # Feet
    x[11] = -20
    y[11] = -130

    x[12] = 20
    y[12] = -130

    # Extra points for better visualisation

    x[13] = 0
    y[13] = -65

    x[14] = 0
    y[14] = 15

    ax.scatter(x, y, s=30, c='white')  # Large white points



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-100,100)
ax.set_ylim(-150, 50)
ax.set_aspect('equal')
ax.set_facecolor('black')



# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)



plt.show()
