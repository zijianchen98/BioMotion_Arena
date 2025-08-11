
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 50], [10, 40], [20, 40], [30, 40],
    [10, 30], [15, 30], [25, 30], [30,30],
    [5, 20], [15, 20], [25, 20], [35, 20],
    [15, 10], [25, 10], [15,0]
])


# Function to update the positions of the point lights for each frame
def update(frame, points, lines):
    # Simple animation: Circular motion for each point
    for i in range(len(points)):
        angle = frame * 0.05 + i * 0.2  # Different speeds and phases for each point
        x = initial_positions[i, 0] + 20 * np.cos(angle) #adjust the radius and range for better visualization
        y = initial_positions[i, 1] + 15 * np.sin(angle) #adjust the radius and range for better visualization
        points[i].set_data(x,y)


    return points,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-50, 100])  # Adjust x-axis limits as needed
ax.set_ylim([-50, 100])  # Adjust y-axis limits as needed
ax.set_facecolor('black') #set background to black
ax.axis('off')  # Turn off the axes

# Create the point lights
points = [plt.plot([], [], 'wo')[0] for _ in range(15)]

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(points,[]), frames=100, interval=50, blit=True)

# Show the animation
plt.show()

