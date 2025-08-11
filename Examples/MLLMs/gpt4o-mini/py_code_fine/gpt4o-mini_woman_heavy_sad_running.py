
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

# Define the initial positions of the point lights
num_points = 15
points = np.zeros((num_points, 2))

# Define the Y-coordinates for the static part of the body
static_y = [10, 20, 30, 40, 50, 60]

# Initialize the points representing the body
for i, y in enumerate(static_y):
    points[i] = [50, y]

# Additional points for the arms and legs
points[6] = [40, 30]  # left arm
points[7] = [60, 30]  # right arm
points[8] = [45, 10]  # left leg
points[9] = [55, 10]  # right leg
points[10] = [50, 70]  # head
points[11] = [50, 80]  # top of the head
points[12] = [40, 50]  # left hand
points[13] = [60, 50]  # right hand
points[14] = [50, 0]   # ground (weight)

# Define the animation function
def update(frame):
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_facecolor('black')
    
    # Simulate running motion by updating the y-coordinates
    delta_y = -0.5 * (frame % 10)
    
    # Update points
    points[8][1] = max(0, points[8][1] + delta_y)  # left leg (downward)
    points[9][1] = max(0, points[9][1] + delta_y)  # right leg (downward)
    
    points[10][1] = points[11][1] + 10  # Head follows
    points[11][1] = points[11][1] + 1  # Smooth head motion downwards
    
    # Plot the points
    ax.plot(points[:, 0], points[:, 1], 'o', color='white')
    
# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=100)

# Show the animation
plt.show()
