
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Define the number of points
num_points = 15

# Define the colors
colors = ['w']

# Define the points
points = np.random.rand(num_points, 2)

# Define the movement parameters
hand_height = 0.5
hand_width = 0.2
wave_amplitude = 0.2
wave_frequency = 0.1

# Initialize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('k')
for i in range(num_points):
    ax.scatter(points[i, 0], points[i, 1], c=colors, s=10)

# Function to update the plot
def update(frame):
    global points
    # Update the points to create a waving motion
    for i in range(num_points):
        x = points[i, 0]
        y = points[i, 1]
        if i < 5:
            # Top 5 points move up and down
            points[i, 1] = hand_height + wave_amplitude * np.sin(wave_frequency * frame)
        elif i < 10:
            # Middle 5 points move side to side
            points[i, 0] = x + wave_amplitude * np.sin(wave_frequency * frame)
        else:
            # Bottom 5 points move up and down
            points[i, 1] = hand_height + wave_amplitude * np.sin(wave_frequency * frame)
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('k')
    # Plot the points
    for i in range(num_points):
        ax.scatter(points[i, 0], points[i, 1], c=colors, s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=False)

plt.show()
