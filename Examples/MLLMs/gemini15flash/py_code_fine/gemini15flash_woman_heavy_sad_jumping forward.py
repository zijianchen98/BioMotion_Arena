
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-light positions
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)

# Define the initial positions of the point lights (adjust as needed for the sad woman jumping)

x = np.array([0, 1, -1, 2, -2, 1, -1, 0, 0, -1, 1, 2, -2, 1.5, -1.5])
y = np.array([5, 4, 4, 3, 3, 2, 2, 1, 0, -1, -1, -2, -2, -3, -3])


# Create the point-light scatter plot
points, = ax.plot(x, y, 'wo', markersize=8)

# Animation update function
def animate(i):
    global x, y

    #Simulate jumping motion (adjust parameters for better realism)

    jump_height = 2
    jump_duration = 20 # Number of frames in jump
    gravity = -0.1

    if i<jump_duration:
        jump_progress = i/jump_duration
        y_jump = jump_height * np.sin(np.pi * jump_progress)
        y = y + y_jump

    # Simulate slight sway during jump
    x += 0.1 * np.random.randn(num_points)

    if i > jump_duration:
        y = y - y[0] # Return to the original y position 
    
    
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation (optional: save as gif)

plt.show()

#To save as a gif uncomment below
# ani.save('biological_motion.gif', writer='pillow')
