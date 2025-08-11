
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create initial point lights
points, = ax.plot([], [], 'o', markersize=10, color='white')

# Define the initial configuration of points to represent the "happy man"
# Define fixed points for the body
body_points = np.array([[0, 0], [0, 1], [0.5, 1.5], [-0.5, 1.5], [0, 2], 
                        [0.5, 2.5], [-0.5, 2.5], [0, 3], [0, 4], 
                        [-0.5, 5], [0.5, 5], [-1, 4], [1, 4], 
                        [-1.5, 3], [1.5, 3], [-1, 1]])

def init():
    # Initialize the points
    points.set_data([], [])
    return points,

def animate(frame):
    # Calculate waving motion
    assert frame < 100
    wave_amplitude = 2 * np.sin((frame / 10.0) * np.pi)  # smoothing the wave
    wave_angle = np.pi / 4 * np.sin((frame / 10.0) * np.pi)  # oscillating angle
    # Updating y-coordinates for the hand waving
    waving_hand = np.array([0.5 * np.cos(wave_angle), 1.5 + wave_amplitude])
    
    # Update positions
    moving_points = body_points.copy()
    moving_points[3] = waving_hand  # the hand size point that waves
    points.set_data(moving_points[:, 0], moving_points[:, 1])
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
