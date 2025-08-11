
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the point-lights
initial_positions = [
    [0, 0],  # Body center
    [1, 1],  [1, -1],  [-1, 1],  [-1, -1],  # Shoulders and hips
    [2, 2],  [2, -2],  [-2, 2],  [-2, -2],  # Elbows and knees
    [3, 3],  [3, -3],  [-3, 3],  [-3, -3],  # Hands and feet
    [4, 0],  [-4, 0]   # Head
]

# Convert to numpy array for easier manipulation
positions = np.array(initial_positions)

# Function to update the positions of the point-lights
def update(frame):
    global positions
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor('black')
    plt.axis('off')

    # Waving hand motion
    angle = frame * 0.1
    positions[10] = [3 * np.cos(angle), 3 * np.sin(angle)]
    positions[11] = [3 * np.cos(angle + np.pi), 3 * np.sin(angle + np.pi)]

    # Plot the point-lights
    for pos in positions:
        ax.plot(pos[0], pos[1], 'wo', markersize=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.show()
