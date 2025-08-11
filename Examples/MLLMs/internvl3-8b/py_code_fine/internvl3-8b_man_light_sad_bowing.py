
import matplotlib.pyplot as plt
import numpy as np

# Parameters for the sadman bowing
num_points = 15
x_position = np.linspace(-1, 1, num_points)
y_position = np.ones(num_points)

# Create a figure and set its background color
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Function to animate the motion
def animate(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.plot(x_position, y_position + frame / 100, 'ko')

# Create animation
ani = FuncAnimation(fig, animate, frames=np.linspace(-7, 7, 100), blit=True)

# Display the first frame
plt.show()
