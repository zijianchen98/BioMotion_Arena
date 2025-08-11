
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 5], [2, 7],
    [3, 2], [3, 4], [3, 6], [3, 8], [4, 3], [4, 7],
    [5, 2], [5, 8], [6, 5]
])

# Define the animation parameters
num_frames = 100
dt = 0.1

# Define the animation function
def animate(i):
    global initial_positions
    
    #jumping forward animation.  Simulate leg and arm movements in a simplified way.
    new_positions = initial_positions.copy()
    
    #Simulate leg movement
    new_positions[[3, 4, 10, 11]] += np.array([0, 0.1 * np.sin(i * dt * 2)])
    new_positions[[7,8, 12, 13]] += np.array([0, -0.1 * np.sin(i * dt * 2)])

    #Simulate arm movement
    new_positions[[1, 2]] += np.array([0.1 * np.sin(i * dt), 0])
    new_positions[[13, 14]] += np.array([-0.1 * np.sin(i * dt), 0])

    #Simulate overall forward movement
    new_positions += np.array([0.05,0])
    
    # Limit the x-coordinate to prevent points from going off-screen
    new_positions[:,0] = np.clip(new_positions[:,0], 0,10)

    #update positions only if within range
    initial_positions = new_positions
    
    ln.set_data(initial_positions[:, 0], initial_positions[:, 1])
    return ln,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-1, 10])
ax.set_ylim([-1, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point-light plot
ln, = ax.plot([], [], 'wo', markersize=8)


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)


# Save the animation as a GIF
ani.save('biological_motion_animation.gif', writer='imagemagick')

# Show the animation (optional - comment out if you only want to save the GIF)
plt.show()
