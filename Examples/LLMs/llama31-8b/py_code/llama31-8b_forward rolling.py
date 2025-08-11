
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the figure and axis
fig, ax = plt.subplots()

# Define the point lights' initial positions
lights = np.array([[0.5, 0.2, 0.1], [0.6, 0.3, 0.1], [0.7, 0.4, 0.1],
                   [0.5, 0.2, 0.2], [0.6, 0.3, 0.2], [0.7, 0.4, 0.2],
                   [0.5, 0.2, 0.3], [0.6, 0.3, 0.3], [0.7, 0.4, 0.3],
                   [0.5, 0.2, 0.4], [0.6, 0.3, 0.4], [0.7, 0.4, 0.4],
                   [0.5, 0.2, 0.5], [0.6, 0.3, 0.5], [0.7, 0.4, 0.5]])

# Define the point lights' initial velocities
velocities = np.array([[0, 0, 0.5], [0.1, 0, 0.5], [0.2, 0, 0.5],
                       [0, 0.1, 0.5], [0.1, 0.1, 0.5], [0.2, 0.1, 0.5],
                       [0, 0.2, 0.5], [0.1, 0.2, 0.5], [0.2, 0.2, 0.5],
                       [0, 0.3, 0.5], [0.1, 0.3, 0.5], [0.2, 0.3, 0.5],
                       [0, 0.4, 0.5], [0.1, 0.4, 0.5], [0.2, 0.4, 0.5]])

# Set the axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Set the axis aspect ratio to be equal
ax.set_aspect('equal')

# Initialize the plot
for i, light in enumerate(lights):
    ax.scatter(light[0], light[1], light[2], c='w')

# Function to update the plot
def update(frame):
    global lights
    # Update the point lights' positions
    for i in range(len(lights)):
        lights[i] += velocities[i]
        
        # Keep the point lights inside the axis limits
        if lights[i][0] < 0:
            lights[i][0] = 0
        elif lights[i][0] > 1:
            lights[i][0] = 1
            
        if lights[i][1] < 0:
            lights[i][1] = 0
        elif lights[i][1] > 1:
            lights[i][1] = 1
            
        if lights[i][2] < 0:
            lights[i][2] = 0
        elif lights[i][2] > 1:
            lights[i][2] = 1
            
    # Clear the previous plot
    ax.clear()
    
    # Set the axis limits
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    
    # Set the axis aspect ratio to be equal
    ax.set_aspect('equal')
    
    # Plot the updated point lights
    for light in lights:
        ax.scatter(light[0], light[1], light[2], c='w')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=20)

plt.show()
