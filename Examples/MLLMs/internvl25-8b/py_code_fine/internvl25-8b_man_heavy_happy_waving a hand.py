
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-10, 10])
ax.axis('off')

# Define the arm movement function
def arm_movement(angle):
    x = 6 + 4 * np.cos(angle)
    y = 3 + 2 * np.sin(angle)
    return x, y

# Initialize the points
points = []
for _ in range(11):
    points.append(ax.plot([], [], 'o', markersize=3, color='white')[0])
points.append(ax.plot([], [], 'o', markersize=3, color='white')[0])
points.append(ax.plot([], [], 'o', markersize=3, color='white')[0])
points.append(ax.plot([], [], 'o', markersize=3, color='white')[0])
points.append(ax.plot([], [], 'o', markersize=3, color='white')[0])

# Function to update the points
def update(frame):
    angles = np.linspace(0, 2 * np.pi, 36)
    for idx, angle in enumerate(angles):
        points[6-int(idx/9)].set_data(arm_movement(angle)[0], arm_movement(angle)[1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=50, blit=True)

# Show the plot
plt.show()
