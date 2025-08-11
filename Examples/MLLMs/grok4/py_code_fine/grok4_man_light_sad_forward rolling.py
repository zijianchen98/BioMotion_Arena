
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize parameters
num_points = 15
duration = 100  # Number of frames
frames_per_roll = 120  # Frames for one complete forward roll

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Define the forward rolling movement
def forward_roll_frame(t):
    # Key positions forming a forward roll; sadman's points
    roll_radius = 2.0
    roll_height = 1.0
    
    # Y position oscillates up and down during a roll
    y_positions = -np.abs(np.sin(np.linspace(0, 2 * np.pi * (t / frames_per_roll), num_points))) * roll_height
    # X position jumps forward while rolling
    x_positions = np.linspace(-roll_radius, roll_radius, num_points) + (10 * t / frames_per_roll)

    return x_positions, y_positions

# Initialization function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    x_data, y_data = forward_roll_frame(i % frames_per_roll)
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
