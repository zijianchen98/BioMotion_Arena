
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent a person in a jumping position
lights = np.array([
    [0, 0],  # Head
    [-0.1, 0.2], [0.1, 0.2],  # Shoulders
    [-0.2, 0.4], [0.2, 0.4],  # Elbows
    [-0.3, 0.6], [0.3, 0.6],  # Hands
    [0, -0.2],  # Hips
    [-0.1, -0.4], [0.1, -0.4],  # Knees
    [-0.2, -0.6], [0.2, -0.6],  # Ankles
    [-0.2, -0.8], [0.2, -0.8],  # Toes
    [0, -0.4]  # Center of mass
])

# Define the movement of each point-light over time
# These movements are chosen to represent a person jumping forward
def update(frame):
    # Calculate the position of each point-light at the current frame
    positions = np.copy(lights)
    
    # Head
    positions[0, 1] += 0.1 * np.sin(frame / 10.0)
    
    # Shoulders
    positions[1, 1] += 0.1 * np.sin(frame / 10.0 + np.pi / 2)
    positions[2, 1] += 0.1 * np.sin(frame / 10.0 + np.pi / 2)
    
    # Elbows
    positions[3, 1] += 0.2 * np.sin(frame / 10.0 + np.pi)
    positions[4, 1] += 0.2 * np.sin(frame / 10.0 + np.pi)
    
    # Hands
    positions[5, 1] += 0.3 * np.sin(frame / 10.0 + np.pi / 2)
    positions[6, 1] += 0.3 * np.sin(frame / 10.0 + np.pi / 2)
    
    # Hips
    positions[7, 1] -= 0.1 * np.sin(frame / 10.0)
    
    # Knees
    positions[8, 1] -= 0.2 * np.sin(frame / 10.0 + np.pi / 2)
    positions[9, 1] -= 0.2 * np.sin(frame / 10.0 + np.pi / 2)
    
    # Ankles
    positions[10, 1] -= 0.3 * np.sin(frame / 10.0 + np.pi)
    positions[11, 1] -= 0.3 * np.sin(frame / 10.0 + np.pi)
    
    # Toes
    positions[12, 1] -= 0.4 * np.sin(frame / 10.0 + np.pi / 2)
    positions[13, 1] -= 0.4 * np.sin(frame / 10.0 + np.pi / 2)
    
    # Center of mass
    positions[14, 1] -= 0.2 * np.sin(frame / 10.0)
    
    # Update the positions of the point-lights
    scatter.set_offsets(positions)
    
    return scatter,

# Create a new figure
fig, ax = plt.subplots()

# Create a scatter plot of the point-lights
scatter = ax.scatter(lights[:, 0], lights[:, 1], c='w', s=50)

# Set the background color to black
ax.set_facecolor('k')

# Set the limits of the axes
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Set the aspect ratio of the axes to be equal
ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
