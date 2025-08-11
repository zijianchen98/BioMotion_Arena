
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 10)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point lights
num_points = 15

# Initialize the points' positions (y-coordinates)
# The x-coordinates are fixed to create a sad figure
x_positions = np.zeros(num_points)
y_positions = np.linspace(1, 5, num_points)  # Initial vertical position

# Create scatter plot for the points
points, = ax.plot(x_positions, y_positions, 'o', color='white')

# Update function for the animation
def update(frame):
    # Calculate the movement of the points to simulate jumping
    jump_height = np.sin(frame * 0.5) * 2  # Simulating a jump
    y_positions[0] = 1 + jump_height  # Head
    y_positions[1:5] = 2 + jump_height  # Shoulders
    y_positions[5:10] = 3 + jump_height  # Arms and torso
    y_positions[10:] = 1 + jump_height  # Legs

    # Update the points' positions
    points.set_ydata(y_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Display the animation
plt.show()
