
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initial positions of the points
positions = np.random.uniform(-5, 5, (num_points, 2))

# Function to update the positions of the points
def update(frame):
    global positions
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor('black')
    plt.axis('off')
    
    # Simulate jumping up motion
    amplitude = 2.0
    frequency = 0.1
    phase = frame * frequency
    
    # Update positions based on a sine wave to simulate jumping
    for i in range(num_points):
        x, y = positions[i]
        y += amplitude * np.sin(phase)
        positions[i] = (x, y)
    
    # Plot the points
    for pos in positions:
        ax.plot(pos[0], pos[1], 'wo', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()
