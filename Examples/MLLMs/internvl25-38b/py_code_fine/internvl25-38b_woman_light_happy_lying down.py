
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to update the position of the lights
def update_position(i, dots, scat):
    # Define the movement for a happy woman lying down with light movements
    for j in range(15):
        angle = i / 10.0 + j * np.pi / 2
        rad = 10 + np.sin(angle) * 3
        x = np.cos(angle) * rad
        y = np.sin(angle) * rad
        dots[j] = (x, y)
    scat.set_offsets(dots)
    return scat,

# Initialize the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
dots = np.random.rand(15, 2) * 0
scat = ax.scatter(dots[:, 0], dots[:, 1], s=200, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_position, frames=300, fargs=(dots, scat), interval=50, blit=True)

plt.show()
