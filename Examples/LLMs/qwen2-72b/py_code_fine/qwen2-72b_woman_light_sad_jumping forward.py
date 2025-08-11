
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create empty scatter plot for the points
points, = ax.plot([], [], 'o', color='white')

# Initial data for the points
x_data = np.random.uniform(1, 9, 15)
y_data = np.random.uniform(1, 9, 15)

def update(frame):
    global x_data, y_data
    
    # Update positions (simplified motion)
    y_data += np.sin(frame / 10) * 0.1
    x_data += np.cos(frame / 10) * 0.1
    
    # Wrap around if out of bounds
    x_data[x_data > 10] -= 10
    x_data[x_data < 0] += 10
    y_data[y_data > 10] -= 10
    y_data[y_data < 0] += 10
    
    # Update the scatter plot
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()
