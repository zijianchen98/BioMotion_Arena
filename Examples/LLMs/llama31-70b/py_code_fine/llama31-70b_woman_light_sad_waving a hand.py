
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are based on a simplified human body model
lights = np.array([
    [0, 0],  # Head
    [-0.2, 0.2], [0.2, 0.2],  # Shoulders
    [-0.4, 0.4], [0.4, 0.4],  # Elbows
    [-0.6, 0.6], [0.6, 0.6],  # Hands
    [-0.2, -0.2], [0.2, -0.2],  # Hips
    [-0.4, -0.4], [0.4, -0.4],  # Knees
    [-0.6, -0.6], [0.6, -0.6],  # Ankles
    [-0.2, 0.1], [0.2, 0.1],  # Torso
    [-0.2, -0.1], [0.2, -0.1]  # Torso
])

# Define the animation function
def animate(frame):
    global lights
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    # Update the positions of the point-lights
    # Simulate the waving motion by moving the right hand and arm
    lights[4, 0] = 0.6 + 0.1 * np.sin(frame / 10.0)
    lights[4, 1] = 0.6 + 0.1 * np.cos(frame / 10.0)
    lights[3, 0] = 0.4 + 0.1 * np.sin(frame / 10.0)
    lights[3, 1] = 0.4 + 0.1 * np.cos(frame / 10.0)
    lights[2, 0] = 0.2 + 0.05 * np.sin(frame / 10.0)
    lights[2, 1] = 0.2 + 0.05 * np.cos(frame / 10.0)
    
    # Plot the point-lights
    ax.scatter(lights[:, 0], lights[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
