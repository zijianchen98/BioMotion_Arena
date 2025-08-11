
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the background color
num_points = 15
background_color = 'black'

# Define the points' initial positions
points = np.random.rand(num_points, 2) * 10

# Define the points' initial velocities
velocities = np.random.rand(num_points, 2) * 2 - 1

# Define the time step and the total duration
dt = 0.01
total_time = 5

# Create a new figure
fig, ax = plt.subplots()

# Set the background color
ax.set_facecolor(background_color)

# Initialize the points' positions
ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Set the limits of the plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Function to update the points' positions
def update(frame):
    global points
    points += velocities * dt
    points = np.clip(points, 0, 10)
    ax.clear()
    ax.set_facecolor(background_color)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(total_time / dt), interval=dt * 1000)

# Save the animation
ani.save('jumping_man.gif', writer='pillow', fps=int(1 / dt))

plt.show()
