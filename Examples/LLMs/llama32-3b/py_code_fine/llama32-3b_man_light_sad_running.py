
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import matplotlib.colors as mcolors

# Define the figure and axis
fig, ax = plt.subplots()

# Define the figure size
fig.set_size_inches(10, 10)

# Define the colors
colors = [mcolors.ColorConverter().to_rgb(1.0) for _ in range(15)]

# Define the radius of the circles
radius = 0.1

# Define the initial positions of the circles
x = np.linspace(-1, 1, 15)
y = np.linspace(-1, 1, 15)
X, Y = np.meshgrid(x, y)
X = X.flatten()
Y = Y.flatten()

# Initialize the circles
circles = []
for i in range(15):
    circle = Circle((X[i], Y[i]), radius, edgecolor='white', facecolor='white', color=colors[i])
    circles.append(circle)
    ax.add_patch(circle)

# Set the limits of the axes
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Set the aspect ratio of the axes to be equal
ax.set_aspect('equal')

# Define the function to update the circles
def update(i):
    # Calculate the angle of the current circle
    angle = 2 * np.pi * i / 15

    # Update the position of the current circle
    x = 1 + np.cos(angle) * 0.5
    y = 1 + np.sin(angle) * 0.5
    circles[i].center = (x, y)

    # Update the position of the other circles
    for j in range(15):
        if j!= i:
            angle = 2 * np.pi * j / 15
            x = 1 + np.cos(angle) * 0.5
            y = 1 + np.sin(angle) * 0.5
            circles[j].center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Display the animation
plt.show()
