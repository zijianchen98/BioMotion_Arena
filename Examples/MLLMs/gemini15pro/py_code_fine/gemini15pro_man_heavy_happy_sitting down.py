
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 10], [-2, 8], [2, 8], [-3, 6], [3, 6],
    [-2, 6], [0, 6], [2, 6], [-3, 4], [-1, 4],
    [1, 4], [3, 4], [-2, 2], [2, 2], [0, 0]
])


# Define a function to simulate the 'sitting down' motion
def animate(i):
    # Adjust these parameters to control the motion
    y_offset = -i * 0.05  # Downward movement
    x_spread = 1 + i * 0.02  # Legs spreading
    
    positions = initial_positions.copy()
    
    # Apply downward movement
    positions[:, 1] += y_offset

    # Apply leg spreading
    positions[2, 0] += x_spread
    positions[5, 0] += x_spread/2
    positions[7, 0] -= x_spread/2
    positions[11, 0] -= x_spread

    # Apply slight knee bending
    if i > 10:
        knee_bend = (i-10) * 0.01
        positions[12, 1] += knee_bend
        positions[13, 1] += knee_bend

    scat.set_offsets(positions)
    return scat,


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_xlim([-5, 5])
ax.set_ylim([-2, 12])

# Hide axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])


# Create the scatter plot for the point lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=20, c='white')


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=20, interval=50, blit=True)

# Display the animation (or save as a GIF/MP4)
plt.show()



