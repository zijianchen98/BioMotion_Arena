
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set constants for the number of points and background color
num_points = 15
background_color = (0, 0, 0)

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

def update(frame):
    global x, y

    x = np.sin(frame / 40) * 0.5 + 0.5
    y = np.sin((frame / 30) - np.pi / 2) * 0.5 + 0.5

    line.set_data(x, y)
    return line,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(background_color)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Turn off axis

# Initialize the points
x = np.zeros(num_points)
y = np.zeros(num_points)
line, = ax.plot(x, y, 'o', color='white', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 180), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
