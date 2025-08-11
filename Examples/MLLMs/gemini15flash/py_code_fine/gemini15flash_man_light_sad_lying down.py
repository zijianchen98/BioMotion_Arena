
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_facecolor('black')
ax.axis('off')

# Initialize the point-lights
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)
points, = ax.plot(x, y, 'wo', markersize=10)

# Define the animation function
def animate(i):
    # Define the movement of the point-lights for a sadman lying down
    # Adjust these values to fine-tune the animation
    global x, y
    
    #Example motion, replace with more realistic biomechanical motion
    x[0] = 0 + np.sin(i/10)
    y[0] = 5 + np.cos(i/10)
    x[1] = 1 + np.sin(i/10 + 0.5)
    y[1] = 4 + np.cos(i/10 + 0.5)
    x[2] = -1 + np.sin(i/10 + 1)
    y[2] = 4 + np.cos(i/10 + 1)
    x[3] = 2 + np.sin(i/10 + 1.5)
    y[3] = 3 + np.cos(i/10 + 1.5)
    x[4] = -2 + np.sin(i/10 + 2)
    y[4] = 3 + np.cos(i/10 + 2)
    x[5] = 0 + np.sin(i/10 + 2.5)
    y[5] = 2 + np.cos(i/10 + 2.5)
    x[6] = 1 + np.sin(i/10 + 3)
    y[6] = 1 + np.cos(i/10 + 3)
    x[7] = -1 + np.sin(i/10 + 3.5)
    y[7] = 1 + np.cos(i/10 + 3.5)
    x[8] = 2 + np.sin(i/10 + 4)
    y[8] = 0 + np.cos(i/10 + 4)
    x[9] = -2 + np.sin(i/10 + 4.5)
    y[9] = 0 + np.cos(i/10 + 4.5)
    x[10] = 0 + np.sin(i/10 + 5)
    y[10] = -1 + np.cos(i/10 + 5)
    x[11] = 1 + np.sin(i/10 + 5.5)
    y[11] = -2 + np.cos(i/10 + 5.5)
    x[12] = -1 + np.sin(i/10 + 6)
    y[12] = -2 + np.cos(i/10 + 6)
    x[13] = 0 + np.sin(i/10 + 6.5)
    y[13] = -3 + np.cos(i/10 + 6.5)
    x[14] = 0 + np.sin(i/10 + 7)
    y[14] = -4 + np.cos(i/10 + 7)



    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(500), interval=20, blit=True)

# Show the animation
plt.show()

