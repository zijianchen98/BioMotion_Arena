
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
x = np.random.rand(num_points) * 20 - 10
y = np.random.rand(num_points) * 20 - 10
points, = ax.plot(x, y, 'wo', markersize=8)

# Define the animation function
def animate(i):
    # Simulate movement for sitting down
    global x, y
    
    # Example movement (replace with more realistic biomechanical model)
    dx = np.random.normal(0, 0.2, num_points) # add some randomness
    dy = np.random.normal(0, 0.2, num_points)
    x += dx
    y += dy
    
    # Constrain points within boundaries to prevent escape
    x = np.clip(x, -8, 8)
    y = np.clip(y, -8, 8)
    
    #Gradually lower the points towards the bottom of the screen
    y -= 0.05

    # Update the plot data
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Save animation (optional, uncomment to save as MP4)
#ani.save('biological_motion.mp4', writer='ffmpeg', fps=30)

# Show the animation
plt.show()

