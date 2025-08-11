
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define points for the happyman's body
body_points = np.array([
    [-100, -100],
    [0, -100],
    [100, -100],
    [0, 100],
    [-100, 100],
    [0, 100],
    [100, 100],
    [-100, 100]
])

# Define points for the happyman's face
face_points = np.array([
    [-50, -50],
    [0, -50],
    [50, -50],
    [0, 50],
    [-50, 50],
    [0, 50],
    [50, 50],
    [-50, 50]
])

# Define points for the happyman's arms
arm_points = np.array([
    [0, -100],
    [0, 100],
    [100, 100],
    [100, -100]
])

# Define points for the happyman's legs
leg_points = np.array([
    [0, 0],
    [100, 0],
    [100, 100],
    [0, 100]
])

# Function to generate the point-light stimulus
def generate_stimulus():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set axis limits
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)

    # Plot the happyman's body
    for i, point in enumerate(body_points):
        ax.plot(point[0], point[1], 'o-', color=WHITE)

    # Plot the happyman's face
    for i, point in enumerate(face_points):
        ax.plot(point[0], point[1], 'o-', color=WHITE)

    # Plot the happyman's arms
    for i, point in enumerate(arm_points):
        ax.plot(point[0], point[1], 'o-', color=WHITE)

    # Plot the happyman's legs
    for i, point in enumerate(leg_points):
        ax.plot(point[0], point[1], 'o-', color=WHITE)

    # Set axis limits
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)

    # Plot the point-lights
    for i in range(15):
        angle = np.linspace(0, 2*np.pi, 100)
        x = 100 + 50 * np.cos(angle)
        y = 100 + 50 * np.sin(angle)
        ax.plot(x, y, 'k-')

    # Set axis limits
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)

    # Set aspect ratio to be equal
    ax.set_aspect('equal')

    return ax

# Function to animate the stimulus
def animate(frame):
    ax.clear()
    generate_stimulus()
    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)
    return ax

# Create the figure and axis
fig, ax = plt.subplots()

# Animate the stimulus
ani = animation.FuncAnimation(fig, animate, frames=range(15), interval=10)

# Show the animation
plt.show()
