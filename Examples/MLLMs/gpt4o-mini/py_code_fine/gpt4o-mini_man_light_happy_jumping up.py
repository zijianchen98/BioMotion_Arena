
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the frame rate
num_points = 15
frame_rate = 30
jump_height = 1.5
jump_duration = 1  # in seconds
total_frames = frame_rate * jump_duration

# Function to generate coordinates for the points representing the happy man's body
def generate_coordinates(frame):
    phase = frame / total_frames * np.pi  # normalizing to range [0, pi]
    
    # Calculate vertical position for the jump
    y_pos = np.sin(phase) * jump_height
    
    # Base positions for the 'happy man' (static in x axis, varies in y)
    base_y = np.linspace(-1, 1, num_points)
    x_pos = np.zeros(num_points)
    
    # Add the dynamic y position to the base positions
    coordinates = np.column_stack((x_pos, base_y + y_pos))
    return coordinates

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    coords = generate_coordinates(frame)
    points.set_data(coords[:, 0], coords[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, interval=1000/frame_rate)
plt.show()
