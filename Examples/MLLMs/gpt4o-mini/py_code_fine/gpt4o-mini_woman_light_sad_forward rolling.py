
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Initial positions of point lights representing a sad woman in a forward rolling action
# Points are represented in 2D space (x, y)
initial_positions = np.array([
    [0, 5], [1, 4], [-1, 4], [2, 3], [-2, 3],  # Upper points
    [0, 2], [1, 1], [-1, 1], [0, 0],           # Middle points
    [0, -1], [1, -2], [-1, -2], [0, -3],      # Lower points (rolling)
    [1, -4], [-1, -4], [0, -5]                 # End points
])

# Function to update the position of point lights
def update(frame):
    plt.clf()
    plt.xlim(-5, 5)
    plt.ylim(-6, 6)
    plt.gca().set_facecolor('black')
    plt.axis('off')

    # Simulate forward rolling by updating y positions in a cyclic manner
    phase = frame % 30
    y_offset = phase / 2.0 - 5  # Adjust y_position for rolling motion
    
    # Update points
    updated_positions = np.copy(initial_positions)
    updated_positions[:, 1] += y_offset

    # Draw points
    plt.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white', s=100)

# Create the animation
fig = plt.figure(figsize=(5, 10))
ani = animation.FuncAnimation(fig, update, frames=60, interval=100)

# Show the animation
plt.show()
