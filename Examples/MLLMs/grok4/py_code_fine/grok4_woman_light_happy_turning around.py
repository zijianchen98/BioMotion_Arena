
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 60  # Total frames for the animation
radius = 50  # Radius for motion around the center
turning_speed = np.pi / 60  # Angular speed for turning

# Initialize the figure and the axis
fig, ax = plt.subplots()
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize point-lights' positions
point_lights = np.array([[0, 10], [-5, 0], [5, 0], [0, -10], 
                         [-10, -5], [-10, 5], [10, -5], [10, 5],
                         [-7, 7], [7, 7], [-7, -7], [7, -7],
                         [-5, 5], [5, 5], [-5, -5]])

# Create a scatter plot for the point-lights
scatter = ax.scatter(point_lights[:, 0], point_lights[:, 1], color='white')

def update(frame):
    # Calculate the current angle based on the frame
    angle = turning_speed * frame
    
    # Update positions for a turning motion
    for i in range(num_points):
        x = radius * np.cos(angle + (i * (2 * np.pi / num_points)))
        y = radius * np.sin(angle + (i * (2 * np.pi / num_points)))
        point_lights[i] = [x, y]
    
    # Update the scatter plot
    scatter.set_offsets(point_lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/30, blit=True)

# Show the animation
plt.show()
