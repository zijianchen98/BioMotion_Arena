
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Point lights' positions for a jumping action
# Y values oscillate to simulate jumping, X values to depict forward motion
def get_point_positions(frame):
    # Jumping motion parameters
    jump_height = np.abs(np.sin(frame / 20.0))  # Simulate jumping up and down
    forward_motion = frame / 10.0  # Simulate forward movement

    # Define X positions
    x_positions = np.array([
        -1, -0.5, 0, 0.5, 1,  # Head and shoulders
        -1, -0.5, 0, 0.5, 1,  # Arms
        -0.5, 0, 0.5,         # Torso
        -0.5, 0.5,            # Legs
    ]) + forward_motion

    # Define Y positions with the jump height
    y_positions = np.array([
        2, 2, 2, 2, 2,         # Head level
        1.5, 1.5, 1.5, 1.5, 1.5, # Shoulders level
        1, 1, 1,               # Torso
        0, 0,                  # Feet level
    ]) + jump_height

    return x_positions, y_positions

# Creating the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 3)
points, = ax.plot([], [], 'o', color='white')  # Create a point light

# Animation update function
def update(frame):
    x_positions, y_positions = get_point_positions(frame)
    points.set_data(x_positions, y_positions)
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=100, blit=True, interval=100)
plt.axis('off')  # Turn off the axis
plt.show()
