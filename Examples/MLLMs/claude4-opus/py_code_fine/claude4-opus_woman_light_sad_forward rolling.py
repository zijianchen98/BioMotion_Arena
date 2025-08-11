
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100
roll_duration = 3  # seconds
fps = frames / roll_duration

# Create a figure and set background color
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Create random initial positions for the point lights
# The Y positions will be spaced for biomechanical plausibility
y_positions = np.linspace(-3, 1, num_points)  # Vertical positions for lights
x_positions = np.zeros(num_points)  # Initial X positions

# Create points that will be animated
points, = ax.plot(x_positions, y_positions, 'o', color='white')

# Define the animation update function
def update(frame):
    # Simulate a forward roll
    # Simple upward arc followed by downward arc
    t = frame / fps  # Time
    if t < 1.5:  # First half is the upward motion
        y_off = (1.5 - t) * 2  # Goes from 0 to 3
    else:  # Second half is the downward motion
        y_off = (t - 1.5) * 2 - 3  # Goes from 3 to 0
    
    # Update x positions to simulate lateral motion during roll
    x_positions = np.sin(np.pi * t / roll_duration) * 2  # Sway motion

    # Update the points' positions
    points.set_data(x_positions, y_positions + y_off)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
