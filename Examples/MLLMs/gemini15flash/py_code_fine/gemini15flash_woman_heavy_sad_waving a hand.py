
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point lights
num_lights = 15
x = np.zeros(num_lights)
y = np.zeros(num_lights)
points, = ax.plot(x, y, 'wo', markersize=8)


# Define the animation function
def animate(i):
    # Define the positions of the point lights for each frame
    # This is where you define the biological motion
    # Adjust these coordinates to create the desired waving hand motion
    # Note: These coordinates are example values, and may need to be changed.
    # You may also need to adjust the number of points to match your data


    global x,y
    x = [0, 1, 2, 1, 0,-1,-2,-1, 0, 1, 2, 1, 0, -1,-2]
    y = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1]
    
    # Example of adding some movement

    #Add movement to the hand (points 0-3)
    x[0] += 0.1*np.sin(i/10)
    y[0] += 0.1*np.cos(i/10)
    x[1] += 0.1*np.sin(i/10 + np.pi/2)
    y[1] += 0.1*np.cos(i/10 + np.pi/2)
    x[2] += 0.1*np.sin(i/10 + np.pi)
    y[2] += 0.1*np.cos(i/10 + np.pi)
    x[3] += 0.1*np.sin(i/10 + 3*np.pi/2)
    y[3] += 0.1*np.cos(i/10 + 3*np.pi/2)
    


    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

