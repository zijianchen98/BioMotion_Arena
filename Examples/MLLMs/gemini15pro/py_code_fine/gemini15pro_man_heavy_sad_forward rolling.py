
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [-1, 4], [-2, 4],  # Head and Shoulders
    [0, 3], [1, 2], [2, 2], [-1, 2], [-2, 2], # Elbows
    [0, 0], [1, -1], [2, -1], [-1,-1], [-2, -1]  # Hip and knees
])


# Define the animation function
def animate(frame):
    # Clear the previous frame
    ax.clear()

    # Calculate the new positions based on forward roll animation logic
    # This is a simplified example; replace with accurate biomechanical calculations
    angle = frame * 0.05  # Rolling Speed
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    shifted_positions = initial_positions - np.array([0, 2]) # Shift down slighly for animation effect

    new_positions = (shifted_positions @ rotation_matrix.T) + np.array([frame * 0.1, 0])

    # Plot the point lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], s=50, c='white')


    # Set the axis limits
    ax.set_xlim(-5, 15)
    ax.set_ylim(-5, 8)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])





# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50) #Adjust frames & interval for timing

# Display the animation (or save as GIF/MP4)
plt.show()


# To save as a GIF (uncomment to use):
# ani.save('forward_roll.gif', writer='imagemagick')


