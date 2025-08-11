
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points.  These are arbitrary and need to be adjusted for the desired pose and motion.
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [1, 4],
    [-2, 3],
    [0, 3],
    [2, 3],
    [-2.5, 2],
    [-1.5, 2],
    [0, 2],
    [1.5, 2],
    [2.5, 2],
    [-1, 1],
    [1, 1],
    [-0.5, 0],
    [0.5, 0]
])


# Animation update function
def animate(i):
    # Generate new positions for the points.  This is where the core animation logic goes.  This example is highly simplified, and a much more sophisticated approach (perhaps using kinematic models) would be required to create biomechanically realistic motion.
    #The motion will be a simple up and down movement for each point with small random variations to simulate some natural movement.

    new_positions = initial_positions.copy()  #Start from initial positions each time


    #Simulate a slow lying down action
    amplitude = 0.5 * np.sin(i * 0.1)  #Adjust frequency and amplitude for the desired slow motion

    for j in range(num_points):
        new_positions[j,1] += amplitude * (1 - (abs(initial_positions[j, 0])/ max(abs(initial_positions[:,0]))) )  #Points closer to center move more

        #Add some small random noise to make it look slightly more natural
        new_positions[j] += np.random.normal(0, 0.05, 2) 


    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)  # Adjust frames and interval as needed.

# Show the plot
plt.show()

