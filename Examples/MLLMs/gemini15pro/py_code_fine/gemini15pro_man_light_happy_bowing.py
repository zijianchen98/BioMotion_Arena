
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
x = np.array([0, -20, 20, -10, 10, -5, 5, -30, 30, 0, -15, 15, -7, 7, 0])
y = np.array([100, 70, 70, 40, 40, 10, 10, -20, -20, -50, -80, -80, -110, -110, -140])

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)
ax.set_ylim(-150, 120)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot(x, y, 'wo')

# Define the animation function
def animate(i):
    # Simulate bowing motion
    angle = np.sin(i * 0.05) * 30  # Adjust the frequency and amplitude of the bowing

    # Apply the bowing motion to the upper body points
    y[:10] = y[:10] + np.sin(i*0.02)*5
    x[:10] = x[:10] - angle/35*x[:10] 
    

    # Update the positions of the point lights
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(200), interval=50, blit=True)

# Ensure the animation loop doesn't stop immediately 
plt.show()

