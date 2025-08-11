
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

# Initialize the figure and axis
fig, ax = plt.subplots()

# Number of light points
num_points = 15

# Initial positions of points
x_data = np.linspace(-5, 5, num_points)
y_data = np.zeros(num_points)
points, = ax.plot(x_data, y_data, 'o', markersize=10)

# Function to update the positions of the points
def update(frame_no):
    global x_data, y_data
    # Example movement pattern, adjust to simulate sitting down
    # This is a placeholder; replace it with the actual pattern
    y_data += np.sin(x_data + frame_no / 10) / 10
    points.set_ydata(y_data)
    return points,

# Run the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
