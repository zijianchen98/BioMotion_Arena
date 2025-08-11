
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Number of point-lights
num_points = 15
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initial positions of point-lights corresponding to a "lying down" position
# y-coordinates from head to feet
initial_positions = np.array([
    [0, 0.5],  # head
    [-0.3, 0.3], [0.3, 0.3],  # shoulders
    [-0.4, 0.1], [0.4, 0.1],  # elbows
    [-0.5, -0.2], [0.5, -0.2],  # wrists
    [-0.6, -0.8], [0.6, -0.8],  # hips
    [-0.5, -1.4], [0.5, -1.4],  # knees
    [-0.4, -1.8], [0.4, -1.8],  # feet
    [0, -1.0],  # torso center
    [-0.2, -1.1], [0.2, -1.1]   # additional points for realism
])

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    # Simple gravity simulation for the lying down action
    y_shift = -0.01 * frame
    new_positions = initial_positions.copy()
    
    # Shift the y-coordinates to simulate the heavy weight
    new_positions[:, 1] += y_shift
    
    # Update point positions
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    
    # Stop simulation when the bottom of the screen is reached
    if any(new_positions[:, 1] < -1.5):
        return points,  # Stop animate if points go below the limits
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), 
                              init_func=init, blit=True)

# Display the animation
plt.show()
