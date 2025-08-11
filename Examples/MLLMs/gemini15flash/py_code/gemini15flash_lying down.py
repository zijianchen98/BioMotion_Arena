
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initial positions of the point lights
num_points = 15
points_x = np.array([0, 2, 2, 2, 1, 1, 1, 0, 0, 0, -1, -1, -1, -2, -2])
points_y = np.array([5, 4, 3, 2, 1, 0, -1, -2, -3, -4,-3,-2,-1, 0, 1])


# Create the point light scatter plot
scat = ax.scatter(points_x, points_y, s=50, color='white')

# Function to update the animation
def animate(i):
    global points_x, points_y

    #Simulate lying down motion. Adjust parameters for different motions. 
    #This is a simplified example and more sophisticated animation would require advanced techniques.
    
    #Example motion: slight up and down movement of the body 
    amplitude = 0.5
    frequency = 0.1
    points_y += amplitude * np.sin(2*np.pi * frequency * i/30)
    
    #Example motion: slight rotation of the upper body
    angle = 0.05 * i
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                               [np.sin(angle), np.cos(angle)]])
    rotated_points = np.dot(np.vstack((points_x,points_y)), rotation_matrix)
    points_x = rotated_points[0,:]
    points_y = rotated_points[1,:]
    
    
    scat.set_offsets(np.c_[points_x, points_y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

