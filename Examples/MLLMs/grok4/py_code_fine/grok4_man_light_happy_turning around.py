
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Generate initial positions of the points
# Positions can be defined based on a simple 2D skeleton representation
# Here we define a basic skeleton for the happy man
skeleton = np.array([
    #  Head
    [0, 2],  
    #  Shoulders
    [-0.5, 1], [0.5, 1],  
    #  Elbows
    [-1, 0.5], [1, 0.5],  
    #  Hands
    [-1.5, 0], [1.5, 0],  
    #  Body
    [0, 0],  
    #  Legs
    [-0.5, -1], [0.5, -1],  
    #  Feet
    [-0.8, -2], [0.8, -2],
    #  Extra points for more realism
    [-0.3, -0.5], [0.3, -0.5], [-0.3, 1], [0.3, 1]
])

# Function to animate the points
def update(frame):
    plt.cla()
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.axis('off')
    
    # Calculate new positions for rotating 
    angle = np.radians(frame * 5)  # Rotation speed
    rot_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                           [np.sin(angle),  np.cos(angle)]])
    
    # Apply rotation to skeleton points
    rotated_points = skeleton @ rot_matrix
    plt.scatter(rotated_points[:, 0], rotated_points[:, 1], color='white')

# Create the figure and animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

# Set the background color to black
fig.patch.set_facecolor('black')

# Show the animation
plt.show()
