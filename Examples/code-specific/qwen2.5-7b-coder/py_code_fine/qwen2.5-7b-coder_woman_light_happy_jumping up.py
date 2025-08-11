
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2) * 2 - 1  # Random positions between -1 and 1

# Define the target position for jumping
target_position = np.array([0, 1])

# Define the animation function
def update(frame):
    global initial_positions
    
    # Update each point light's position towards the target
    for i in range(num_lights):
        if np.linalg.norm(initial_positions[i] - target_position) > 0.01:
            direction = (target_position - initial_positions[i]) / np.linalg.norm(target_position - initial_positions[i])
            initial_positions[i] += direction * 0.05
    
    # Clear the previous frame
    plt.clf()
    
    # Plot the point lights
    plt.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')
    
    # Set the background to black
    plt.gca().set_facecolor('black')
    
    # Set the limits of the plot
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    
    # Remove the axes
    plt.axis('off')

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the animation
plt.show()
