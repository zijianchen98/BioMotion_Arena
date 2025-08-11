
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [3, 4], [0, 3], [1, 3], [2, 3], [3, 3], [0, 2], [1, 2], [2, 2], [3, 2],
    [1, 1], [2, 1], [1.5, 0]
])


# Function to update the positions of the point-lights for each frame
def update(frame_num, data, scat):
    #Simulate a bowing motion.  This is a simplified example; more sophisticated 
    #motion could be generated using kinematic models or motion capture data.
    amplitude = 1  # Adjust for bowing intensity
    frequency = 0.2 # Adjust for bowing speed

    # Modify the y-coordinates to simulate bowing.  More complex movements would require a separate function for each joint.
    new_positions = np.copy(initial_positions)
    new_positions[:,1] += amplitude * np.sin(2 * np.pi * frequency * frame_num + np.random.rand() * np.pi)
    
    #add slight random jitter to simulate natural movement imperfections.
    new_positions += np.random.normal(0, 0.1, size=new_positions.shape)
    
    # Ensure that point lights stay within bounds. (Simple clipping for this example)
    new_positions[:, 0] = np.clip(new_positions[:, 0], 0, 4)
    new_positions[:, 1] = np.clip(new_positions[:, 1], 0, 6)


    data.set_offsets(new_positions)
    return data,


# Set up the figure and axes
fig = plt.figure(figsize=(5, 7)) #Adjust figure size as needed
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(0, 4), ylim=(0, 6))
ax.set_facecolor('black') #Set background to black

# Create the scatter plot of point-lights
data = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(data, data), frames=100, interval=50, blit=True)


# Save the animation. Comment out if you just want to display it
# ani.save('bowing_animation.gif', writer='imagemagick')

plt.show()
