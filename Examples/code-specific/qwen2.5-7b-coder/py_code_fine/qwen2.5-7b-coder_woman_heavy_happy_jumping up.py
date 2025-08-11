
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2) * 8 - 4  # Random positions between -4 and 4 on both axes

# Define the target positions for the jumping motion
target_positions = np.array([
    [-2, 0], [0, 0], [2, 0],
    [-2, 1], [0, 1], [2, 1],
    [-2, 2], [0, 2], [2, 2],
    [-2, 3], [0, 3], [2, 3]
])

# Define the animation function
def animate(frame):
    global initial_positions
    
    # Calculate the step size based on the frame number
    step_size = frame / 60.0
    
    # Update the positions of the point-lights towards the target positions
    for i in range(num_lights):
        initial_positions[i] += (target_positions[i] - initial_positions[i]) * step_size
    
    # Clear the previous plot
    plt.clf()
    
    # Plot the updated positions of the point-lights
    plt.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')
    
    # Set the limits of the plot
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    
    # Remove the axis ticks
    plt.xticks([])
    plt.yticks([])

# Create the animation
fig = plt.figure(figsize=(6, 6))
ani = FuncAnimation(fig, animate, frames=300, interval=20, repeat=False)

# Show the animation
plt.show()
