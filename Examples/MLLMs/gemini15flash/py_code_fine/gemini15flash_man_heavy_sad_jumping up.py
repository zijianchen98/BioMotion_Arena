
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-light positions
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)

# Define the initial positions of the point lights.  These coordinates roughly match the example image. Adjust as needed for better representation.
initial_positions = np.array([
    [0, 8],
    [-1.5, 6.5],
    [0, 6.5],
    [1.5, 6.5],
    [-2.5, 5],
    [-1, 5],
    [0, 5],
    [1, 5],
    [2.5, 5],
    [-1.5, 3.5],
    [1.5, 3.5],
    [-1, 2],
    [1, 2],
    [0, 0],
    [0,-2]

])
x = initial_positions[:,0]
y = initial_positions[:,1]


# Create the point-light scatter plot
scat = ax.scatter(x, y, c='white', s=50)


# Animation update function
def animate(i):
    global x, y
    # Simulate a jump - adjust parameters for desired effect
    amplitude = 3  # Adjust the jump height
    frequency = 0.1  # Adjust the jump speed
    
    #Apply different vertical jump trajectory to each point light
    y += amplitude * np.sin(2 * np.pi * frequency * i + np.linspace(0,2*np.pi,num_points)) * 0.1

    #Simulate slight sideways motion and swaying during jump
    x += amplitude * np.sin(2 * np.pi * frequency * i + np.linspace(0,2*np.pi,num_points)) * 0.01 * np.random.randn(num_points)
   
    #Keep the point lights within the bounds of the figure
    x = np.clip(x, -5, 5)
    y = np.clip(y, -5, 10)


    scat.set_offsets(np.c_[x, y])
    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=30, blit=True)

# Show the animation
plt.show()
