
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [3, 4],
    [0.5, 3], [1.5, 3], [2.5, 3], [3.5, 3],
    [1, 2], [2, 2],
    [1, 1], [2, 1],
    [1.5, 0]
])


# Define the animation function
def animate(i):
    # Update the positions of the point lights based on the frame number
    updated_positions = np.copy(initial_positions)

    #Example of adding a simple animation, you will need to refine this part. 
    updated_positions[:, 1] -= 0.05 * i  # Move points downwards.  Adapt for a realistic sit.
    updated_positions[0:4, 0] += 0.02*np.sin(0.1*i) #Add some simple arm movement
    updated_positions[8:10, 0] += 0.01*np.cos(0.15*i) #Add some simple leg movement



    # Check if points are out of bounds, then "reset" them for a continuous animation. Adapt for your desired looping.
    updated_positions[updated_positions[:, 1] < -5, 1] = 5 #Example reset for the y-axis. 
    


    # Plot the updated positions
    ax.clear()
    ax.set_xlim([-1, 4])  #Adjust limits for x,y axis as needed.
    ax.set_ylim([-6, 6])
    ax.scatter(updated_positions[:, 0], updated_positions[:, 1], s=50, c='w')
    ax.set_aspect('equal')
    ax.axis('off')


# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(200), interval=50)  #200 frames, 50ms interval. adjust as needed.


# Show the animation (or save it as a GIF)
plt.show()

#If you want to save as a GIF, uncomment the below line. Requires imageio library.
#ani.save('biological_motion.gif', writer='imagemagick', fps=20) #Adjust FPS if needed.

