
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and frames
n_points = 15
n_frames = 100

# Define the point-light positions and velocities
points = np.zeros((n_points, 2))
velocities = np.zeros((n_points, 2))

# Initialize the point-lights to form a person
points[0] = [0, 10]  # head
points[1] = [-2, 8]  # left shoulder
points[2] = [2, 8]   # right shoulder
points[3] = [-3, 6]  # left elbow
points[4] = [3, 6]   # right elbow
points[5] = [-4, 4]  # left wrist
points[6] = [4, 4]   # right wrist
points[7] = [0, 6]   # torso
points[8] = [-1, 4]  # left hip
points[9] = [1, 4]   # right hip
points[10] = [-2, 2] # left knee
points[11] = [2, 2]  # right knee
points[12] = [-3, 0] # left ankle
points[13] = [3, 0]  # right ankle
points[14] = [0, 2]  # body

# Define the animation function
def animate(i):
    global points, velocities
    
    # Update the point-light positions based on the velocities
    points += velocities
    
    # Update the velocities to create a rolling motion
    for j in range(n_points):
        velocities[j] += np.random.uniform(-0.1, 0.1, 2)
        
        # Add a forward rolling motion
        if j < 5:  # upper body
            velocities[j] += [0.1, -0.05]
        else:  # lower body
            velocities[j] += [0.1, 0.05]
        
        # Add a bouncing motion
        if points[j, 1] < 0:
            velocities[j, 1] *= -1
    
    # Clear the previous frame and plot the new frame
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.scatter(points[:, 0], points[:, 1], c='white', s=50, edgecolors='white')

# Create the figure and axis
fig, ax = plt.subplots(facecolor='black')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=50)

plt.show()
