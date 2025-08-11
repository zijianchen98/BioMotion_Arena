
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Function to initialize the figure and axis
def init():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1280)
    ax.set_ylim(0, 720)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    return fig, ax

# Function to create a single frame of the animation
def update(i, x):
    x[0] = np.mod(i, 160)
    x[1] = (720 - np.mod(i%8*60, 1440))/4/10
    pts = ax.plot(x, color='white')
    return pts,

# Initialize the figure and axis
fig, ax = init()

# Generate the index for animation
frame = np.arange(0, 640, 2)

# Define the x and Y coordinates of the points
x = np.ones(15) * -1

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(x,), frames=frame, interval=40, blit=True)

# Save the animation
ani.save('sadwoman_jumping_forward.gif', writer='pillow', fps=30)

# Show the animation
# plt.show()
