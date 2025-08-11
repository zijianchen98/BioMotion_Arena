
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights.  Adjust these to match your desired pose.
# This example pose is a rough approximation.  You'll likely need to refine it.

x = [0, -10, 10, -20, 20, -25, 25, -15, 15, 0, -5, 5, -5, 5, 0]
y = [100, 80, 80, 60, 60, 40, 40, 40, 40, 20, 0, 0, -20, -20, -40]


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 120])
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot(x, y, 'wo')

# Animation update function
def animate(i):
    global x, y

    # Simple example of oscillatory motion - Replace with your actual motion logic
    y_offset = 5 * np.sin(i * 0.1) # Simulate vertical movement (e.g., walking up and down motion)

    x[0] = 0  # Head stable
    x[1] = x[1] + 0.5 * np.sin(i * 0.12)  # Shoulders (subtle movement)
    x[2] = x[2] - 0.5 * np.sin(i * 0.12)

    # ... (similar logic for other points) Update other points according to biomechanical principles

    y = [val + y_offset for val in y]  #Apply vertical offset for walking effect

    points.set_data(x, y)
    return points,



# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50, blit=True)


plt.show()

