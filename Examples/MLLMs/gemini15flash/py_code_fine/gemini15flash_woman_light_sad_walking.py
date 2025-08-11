
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
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [0, 4],
    [1, 4],
    [-2, 3],
    [-1, 3],
    [0, 3],
    [1, 3],
    [2, 3],
    [-1, 2],
    [0, 2],
    [1, 2],
    [0, 1],
    [-0.5, 0],
    [0.5, 0]
])

# Define a function to update the positions of the points
def update(frame):
    global initial_positions
    dt = 0.1
    x_vel = np.random.normal(0,0.5,size=num_points)
    y_vel = np.random.normal(0,0.5, size=num_points)
    
    #Simulate walking motion
    if frame<20:
        initial_positions[:,0]+=x_vel
        initial_positions[:,1]+=y_vel

    elif frame>=20 and frame < 40:
         initial_positions[:,0]+=x_vel
         initial_positions[:,1]-=y_vel
    
    elif frame >=40 and frame < 60:
         initial_positions[:,0]-=x_vel
         initial_positions[:,1]+=y_vel

    else:
         initial_positions[:,0]-=x_vel
         initial_positions[:,1]-=y_vel


    #Keep points in bounds
    initial_positions[:,0] = np.clip(initial_positions[:,0], -8, 8)
    initial_positions[:,1] = np.clip(initial_positions[:,1], -8, 8)
    
    points.set_data(initial_positions[:, 0], initial_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()

