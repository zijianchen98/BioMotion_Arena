
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [1, 6], [2, 3], [2, 5], [2, 7],
    [3, 2], [3, 4], [3, 6], [3, 8], [4, 3], [4, 7],
    [5, 2], [5, 8], [6, 5]
])

# Define the animation function
def animate(i):
    # Update positions based on time (i) -  Jumping forward animation logic
    positions = np.copy(initial_positions)  #Start from initial position each frame
    positions[:, 0] += 0.1 * i # Move all points forward
    positions[:, 1] += 0.05 * np.sin(0.2*i) #Add a little up-down jump
    
    #Add some realistic perturbation for legs and arms (adjust as needed for realism):
    positions[6:8, 1] += 0.3*np.sin(0.1*i) #legs
    positions[10:12, 1] += 0.3*np.sin(0.1*i + np.pi) #legs
    positions[1:3, 1] += 0.2*np.sin(0.2*i + np.pi/2) #arms
    positions[8:10, 1] += 0.2*np.sin(0.2*i + 3*np.pi/2) #arms


    # Clear the previous frame
    ln.set_data([], [])


    # Plot the updated positions
    ln.set_data(positions[:, 0], positions[:, 1])

    return ln,

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 10) # adjust x-axis limits as per animation
ax.set_ylim(0, 10)  # adjust y-axis limits as per animation
ax.set_facecolor('black') #black background

# Create the line plot
ln, = ax.plot([], [], 'wo', markersize=8) #white circles

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

