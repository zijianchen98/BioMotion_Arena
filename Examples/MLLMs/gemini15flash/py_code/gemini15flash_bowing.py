
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)
points, = ax.plot(x, y, 'wo', markersize=10)


# Animation function
def animate(i):
    # Define the bowing motion (adjust parameters for desired effect)
    amplitude = 1.5  # Adjust for bowing depth
    frequency = 0.1 # Adjust for bowing speed
    phase_shift = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8]) #adjust phase shift for different body parts

    #Example coordinates, adjust for better realism
    x_coords = np.array([0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 0, -1, 0.5, -0.5, 0])
    y_coords = np.array([4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 3, 1, 1, 0])
    
    #Apply bowing motion
    x_new = x_coords + amplitude * np.sin(2 * np.pi * frequency * i + phase_shift)
    y_new = y_coords


    # Update the point positions
    points.set_data(x_new, y_new)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Remove axis ticks and labels for a cleaner look
ax.set_xticks([])
ax.set_yticks([])


# Save the animation as a GIF (optional)
#ani.save('bowing_animation.gif', writer='imagemagick', fps=20)

# Show the animation
plt.show()

