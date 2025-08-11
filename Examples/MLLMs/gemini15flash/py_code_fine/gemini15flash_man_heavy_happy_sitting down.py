
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
num_points = 15
points, = ax.plot([], [], 'wo', markersize=10)

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [1, 4],
    [-2, 3],
    [0, 3],
    [2, 3],
    [-3, 2],
    [-1, 2],
    [1, 2],
    [3, 2],
    [-1, 1],
    [1, 1],
    [-1, -1],
    [1, -1],
    [0, -2]

])

# Define the animation function
def animate(i):
    # Calculate the new positions of the point-lights based on the frame number
    # This part requires careful design to create realistic biological motion
    # Adjust these values for finer control over the animation

    #Example of the movement.  You will have to adapt it to the sit down action.
    new_positions = initial_positions.copy()
    new_positions[:,1] -= i*0.1 #all points go down

    #Check if any point reached the bottom of the figure.
    points_at_bottom = np.where(new_positions[:,1]<-5)[0]
    if len(points_at_bottom)>0:
      new_positions[points_at_bottom,1] = -5 #stop points from going under the frame


    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

