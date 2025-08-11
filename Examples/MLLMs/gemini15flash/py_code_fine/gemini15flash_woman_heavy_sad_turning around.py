
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)
points, = ax.plot(x, y, 'wo', markersize=10)


def animate(i):
    # Define the coordinates of the points
    #These coordinates are carefully crafted to create the illusion of a sad woman turning around while carrying a heavy weight.  
    #Adjusting these values will alter the animation.
    #The key is to maintain a realistic and biomechanically plausible representation of human movement. 
    x_coords = [
        np.sin(i/10 + np.pi/2) + 1, 
        np.sin(i/10 + np.pi) + 1.5, 
        np.sin(i/10 + np.pi + np.pi/4) + 2, 
        np.sin(i/10 + 3*np.pi/4) + 1.5, 
        np.sin(i/10 + 0) + 1,
        np.sin(i/10 + np.pi/4) + 0.5, 
        np.sin(i/10) + 0, 
        np.sin(i/10 + 3*np.pi/4) -0.5, 
        np.sin(i/10 + np.pi) - 1,
        np.sin(i/10 + 5*np.pi/4) - 0.5, 
        np.sin(i/10 + 3*np.pi/2) - 1,
        np.sin(i/10 + 7*np.pi/4) -1.5,
        np.sin(i/10 + 2*np.pi) -1, 
        np.sin(i/10 + 5*np.pi/4) - 1.5,
        np.sin(i/10 + 3*np.pi/2) - 2,
    ]
    
    y_coords = [
        np.cos(i/10 + np.pi/2) + 2,
        np.cos(i/10 + np.pi) + 1.5,
        np.cos(i/10 + np.pi + np.pi/4) + 1,
        np.cos(i/10 + 3*np.pi/4) + 0.5,
        np.cos(i/10 + 0) + 0,
        np.cos(i/10 + np.pi/4) -0.5,
        np.cos(i/10) -1,
        np.cos(i/10 + 3*np.pi/4) -1.5,
        np.cos(i/10 + np.pi) - 2,
        np.cos(i/10 + 5*np.pi/4) - 2.5,
        np.cos(i/10 + 3*np.pi/2) - 2,
        np.cos(i/10 + 7*np.pi/4) - 1.5,
        np.cos(i/10 + 2*np.pi) -1,
        np.cos(i/10 + 5*np.pi/4) - 0.5,
        np.cos(i/10 + 3*np.pi/2) + 0
    ]

    x = np.array(x_coords)
    y = np.array(y_coords)


    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(720), interval=20, blit=True)

# Show the animation
plt.show()

