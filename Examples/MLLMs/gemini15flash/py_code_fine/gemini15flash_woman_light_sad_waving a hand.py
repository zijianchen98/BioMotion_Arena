
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

# Define initial positions (adjust as needed to match image)
initial_positions = np.array([
    [0, 5],  # Head
    [-1, 3.5], [0, 3.5], [1, 3.5], # Shoulders
    [-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2], # Torso
    [-1, 0.5], [1, 0.5], # Hips
    [-1, -2], [1, -2] # Legs
])

x[:initial_positions.shape[0]] = initial_positions[:,0]
y[:initial_positions.shape[0]] = initial_positions[:,1]

# Create the point-light scatter plot
points, = ax.plot(x, y, 'wo', markersize=10)


# Animation update function
def animate(i):
    # Simulate waving hand motion (replace with more sophisticated motion)
    global x, y
    amplitude = 1.0
    frequency = 0.2
    phase_shift = 0.5
    
    # Example waving motion for right hand
    x[8] += amplitude * np.sin(2 * np.pi * frequency * i + phase_shift)  # Hand x
    y[8] += amplitude * np.cos(2 * np.pi * frequency * i + phase_shift)  # Hand y
    
    # Add some natural variation
    x += np.random.normal(0, 0.05, num_points)
    y += np.random.normal(0, 0.05, num_points)

    #Constrain the points to a range to prevent going off screen
    x = np.clip(x, -10, 10)
    y = np.clip(y, -10, 10)
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

