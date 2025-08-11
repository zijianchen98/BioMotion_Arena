
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the points for the animation
n_points = 15
x = np.linspace(-1, 1, n_points)
y = np.linspace(-1, 1, n_points)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# Define the figure and axis
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Define the point lights
point_lights = []
for i in range(n_points):
    # Define the color and intensity of the light
    color = (i / n_points, i / n_points, i / n_points)
    intensity = 1.0
    
    # Define the position of the light
    angle = np.radians(i * 10)
    x = X[i] + np.cos(angle) * 0.1
    y = Y[i] + np.sin(angle) * 0.1
    z = Z[i] + np.sin(angle) * 0.1
    
    # Create the point light
    light = plt.Line2D([0, x], [0, y], [0, z], color=color, lw=1, alpha=intensity)
    point_lights.append(light)

# Define the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# Define the initial position of the light
light = plt.Line2D([0, 0], [0, 0], color='black', lw=2, alpha=0.5)
ax.add_artist(light)

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    
    # Move the point lights
    for light in point_lights:
        light.set_xdata(X[i] + np.cos(i * 10))
        light.set_ydata(Y[i] + np.sin(i * 10))
        light.set_zdata(Z[i] + np.sin(i * 10))
        
    # Add the point light
    light = plt.Line2D([0, 0], [0, 0], color='black', lw=2, alpha=0.5)
    ax.add_artist(light)
    
    # Show the animation
    plt.pause(0.01)

# Animate the light
ani = animation.FuncAnimation(fig, animate, frames=range(n_points), interval=50)

# Show the animation
plt.show()
