
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
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the point-lights
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


# Define the animation function
def animate(i):
    # Generate the new positions of the point-lights
    new_positions = initial_positions.copy()
    
    # Simulate walking motion (adjust parameters for different styles)
    step_size = 0.1
    new_positions[:, 0] += step_size * np.sin(i * 0.1) #x-axis movement
    new_positions[:, 1] += step_size * np.cos(i*0.05) #y-axis movement
    
    #add weight simulation, simulating a sway based on the step
    weight_sway = 0.2 * np.sin(i*0.08)
    new_positions[10:12,1] += weight_sway

    # add arm swing simulation, simulating the counter movement of the arms
    arm_swing = 0.5 * np.sin(i*0.15)
    new_positions[[1,2,13,14], 0] += arm_swing
    arm_swing2 = 0.5 * np.sin(i * 0.15 + np.pi)
    new_positions[[3,4,13,14],0] += arm_swing2


    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)


# Show the animation
plt.show()

