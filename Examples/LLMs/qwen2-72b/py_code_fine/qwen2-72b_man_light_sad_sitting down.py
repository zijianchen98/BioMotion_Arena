
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_facecolor('black')

# Create a list to hold the point lights
points = []

# Function to initialize the animation
def init():
    for _ in range(15):
        point, = ax.plot([], [], 'o', color='white')
        points.append(point)
    return points

# Function to update the animation frame
def animate(i):
    # Generate new positions for each point light
    for j, point in enumerate(points):
        x, y = point.get_data()
        if i % 30 == 0:  # Change direction every 30 frames
            dx = np.random.uniform(-1, 1)
            dy = np.random.uniform(-1, -2) if i % 60 == 0 else np.random.uniform(-1, 1)
        x += dx / 10
        y += dy / 10
        point.set_data(x, y)
    return points

# Call the animation function
ani = animation.FuncAnimation(fig, animate, frames=300, init_func=init, blit=True)

plt.show()
