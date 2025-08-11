
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the duration of the animation in seconds
num_frames = 120
duration = 4

# Define the initial positions of the 15 point-lights
np.random.seed(0)
initial_positions = np.random.uniform(-100, 100, size=(15, 2))

# Define the velocities of the point-lights to simulate bowing motion
velocities = np.array([
    [0, -1], [0, -1], [0, -1], [0, -1], [0, -1],
    [-1, -0.5], [-0.5, -0.5], [0.5, -0.5], [1, -0.5],
    [-1, 0], [0, 0], [1, 0],
    [-1, 0.5], [0.5, 0.5], [1, 0.5]
]) * 1.5

# Create a function to update the positions of the point-lights
def update_positions(positions, velocities):
    # Update the positions based on the velocities
    positions += velocities
    
    # Keep the point-lights within the screen boundaries
    positions = np.clip(positions, -100, 100)
    
    return positions

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_facecolor('black')

# Create a scatter plot for the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Animation function
def animate(i):
    global initial_positions
    
    # Update the positions of the point-lights
    initial_positions = update_positions(initial_positions, velocities)
    
    # Update the scatter plot data
    scat.set_offsets(initial_positions)
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=duration*1000/num_frames, blit=True)

# Show the animation
plt.show()
