
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the points representing the woman's body parts
points = [
    [0, 0],  # Center of mass
    [-1, 2], [1, 2],  # Shoulders
    [-2, 1], [2, 1],  # Elbows
    [-3, 0], [3, 0],  # Hands
    [-1, -1], [1, -1],  # Hips
    [-2, -2], [2, -2],  # Knees
    [-3, -3], [3, -3],  # Feet
]

# Convert points to a NumPy array
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

# Define the animation function
def animate(i):
    # Simulate jumping forward
    amplitude = 1.5
    frequency = 0.1
    phase = i * 0.1

    # Update the y-coordinate of each point
    points[:, 1] += amplitude * np.sin(frequency * phase)

    # Update the x-coordinate to simulate forward motion
    points[:, 0] += 0.05

    # Reset the points if they move out of the frame
    if points[0, 0] > 10:
        points[:, 0] -= 20

    # Update the scatter plot
    scat.set_offsets(points)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
