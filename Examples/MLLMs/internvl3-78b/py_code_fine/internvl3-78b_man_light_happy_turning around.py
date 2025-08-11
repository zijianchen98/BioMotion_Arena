
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect('equal')
ax.axis('off')

# Define the initial positions of the point-lights
points = np.array([[50, 20], [45, 30], [55, 30], 
                   [50, 10], [45, 25], [55, 25], 
                   [40, 40], [50, 40], [60, 40], 
                   [40, 55], [50, 55], [60, 55], 
                   [45, 70], [55, 70], [50, 80]])

# Create the scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Initialize the turning angle
angle = 0
turning_speed = 0.1

def update(frame):
    global angle
    # Clear the previous scatter plot
    ax.collections.clear()
    
    # Update the points' positions
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    rotated_points = np.dot(points - [50, 50], rotation_matrix) + [50, 50]
    
    # Update the scatter plot
    scat.set_offsets(rotated_points)
    
    # Add the scatter plot back to the axes
    ax.add_collection(scat)
    
    # Increment the angle for the next frame
    angle += turning_speed

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

# Show the plot
plt.show()
