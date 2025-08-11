
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 points
# Adjust these based on your specific needs
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [-1, 4], [-2, 4],
    [0, 3], [1, 2], [2, 2], [-1, 2], [-2, 2],
    [0, 0], [1, -1],
    [0, -4], [1, -5],
    [0, -8]
])


# Define the animation function
def animate(i):
    # Modify the positions of the points to simulate hand waving
    positions = initial_positions.copy()
    wave_angle = np.sin(i * 0.1)  # Adjust the speed and amplitude of the wave
    positions[1:5, 0] += wave_angle * 0.5 #  hand waving movement 
    scatter.set_offsets(positions)
    return scatter,


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background color to black
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_xlim([-5, 5]) # Adjust x and y limits if needed
ax.set_ylim([-10, 6])

# Create the scatter plot for the points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=20, c='white') # Adjust s to change the point size


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True) # Adjust frame and interval as needed


# To save as a GIF (uncomment to use)
# ani.save('hand_wave.gif', writer='pillow')

# Display the animation
plt.show()

