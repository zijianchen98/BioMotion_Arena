
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [ -1, 4], [0, 4], [1, 4], [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2], [-0.5, 1], [0.5, 1], [0,0]
])


# Define the animation function
def animate(i):
    # Update the positions of the point-lights based on time
    updated_positions = update_positions(i)

    # Clear the previous frame
    ax.clear()

    # Plot the updated positions of the point-lights
    ax.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white', s=50)

    # Set the axis limits
    ax.set_xlim([-3, 3])
    ax.set_ylim([0, 6])

    # Remove axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('black')



# Function to update positions to simulate sitting down
def update_positions(i):
    positions = np.copy(initial_positions)
    # Simulate a smooth sitting down motion
    # Adjust parameters below to fine-tune the animation
    dt = 0.1
    for j in range(len(positions)):
      if j < 8:
        positions[j,1] -= dt* (0.5 + np.sin(i/5 * 0.1 * j))
      elif j <12:
        positions[j, 1] -= dt*(0.3 + np.sin(i/7 * 0.1 *j))
      else:
        positions[j, 1] -= dt * 0.2
        
    
    return positions

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50)

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Display the animation
plt.show()

# Save the animation (optional)
#ani.save('biological_motion.gif', writer='imagemagick', fps=20)

