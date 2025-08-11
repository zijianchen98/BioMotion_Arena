
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [3, 4],
    [0, 3], [1, 3], [2, 3], [3, 3],
    [0, 2], [1, 2], [2, 2], [3, 2],
    [1, 1], [2, 1], [1.5, 0]
])


# Function to update the positions of the point-lights for each frame
def update(frame, points, scat):
    # Simple forward rolling animation (replace with more sophisticated biomechanical model)
    for i in range(len(points)):
        points[i, 0] += 0.1  # Move along the x-axis
        points[i, 1] += 0.05*np.sin(frame/10 + i) # add some slight vertical wobble

        # Keep points within the screen, loop back
        if points[i, 0] > 10:
            points[i, 0] -=10
    scat.set_offsets(points)
    return scat,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-1, 10])  # Adjust x-axis limits as needed
ax.set_ylim([-1, 6])  # Adjust y-axis limits as needed
ax.set_facecolor('black')  # Set background color to black

# Create the point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(initial_positions, scat), frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()

# Save the animation (optional)
# ani.save('biological_motion.gif', writer='imagemagick', fps=20) #Requires ImageMagick

