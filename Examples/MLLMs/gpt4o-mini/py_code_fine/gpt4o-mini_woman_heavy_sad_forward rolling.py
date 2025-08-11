
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')  # Turn off the axis

# Define the point-light position based on a simple rolling motion
num_lights = 15  # Number of point-lights
lights = np.zeros((num_lights, 2))

# Initial positions of the point-lights (y-axis)
# Top to bottom (human silhouette based on given example)
initial_positions = np.array([
    [0, 4], [1, 5], [-1, 5],
    [0, 3], [1, 4], [-1, 4],
    [0, 2], [1, 3], [-1, 3],
    [0, 1], [1, 2], [-1, 2],
    [0, 0], [1, 1], [-1, 1],
    [0, -1], [1, 0], [-1, 0],
])

lights = initial_positions

def update(frame):
    global lights
    
    # Simulate forward rolling by adjusting the positions
    # Basic rolling motion in a cycle (y goes down, x swings slightly)
    lights[:, 1] -= 0.1  # Move down
    if frame % 10 < 5:  # Swing motion
        lights[:, 0] += 0.05
    else:
        lights[:, 0] -= 0.05
    
    # Reset position to create looping effect when it rolls off screen
    if lights[0, 1] < -5:
        lights[:, 1] = initial_positions[:, 1]
    
    # Clear the plot and redraw lights
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis('off')
    
    # Draw point-lights
    ax.scatter(lights[:, 0], lights[:, 1], color='white')

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Show the animation
plt.show()
