
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_points = 15
frames = 60
walking_distance = 0.1  # Step size
step_counts = 10  # Number of steps

# Create an empty figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize point positions for a happy walking man
def init():
    # Place points as if they're the key joints of a happy man
    y_positions = np.array([-1.0, -0.5, 0, 0.5, 1.0])
    x_positions = np.zeros(num_points)
    
    # Arrange point locations for the initial pose (standing)
    x_positions[0:5] = np.linspace(-0.3, 0.3, 5)  # arms
    x_positions[5:10] = np.linspace(-0.1, 0.1, 5)  # legs
    x_positions[10:] = -0.1  # head/upper body
    points.set_data(x_positions, y_positions)
    return points,

# Update function to modify the points to simulate walking
def update(frame):
    curr_positions = points.get_data()
    x = curr_positions[0]
    y = curr_positions[1].copy()
    
    # Update positions to create a walking effect
    for i in range(5):  # moving arms
        x[i] += np.sin(frame / 10) * 0.05  # subtle arm movement
    for i in range(5, 10):  # moving legs
        x[i] += np.sin(frame / 10) * 0.1 + (frame // 10) * walking_distance * (1 if i % 2 == 0 else -1)

    # Move the entire figure forward in the x direction
    for i in range(len(x)):
        y[i] = y[i] - (walking_distance * (1 if frame % 2 == 0 else -1))  # alternate y positions
    
    # Update the data of points
    points.set_data(x, y)
    return points,

# Creating and displaying the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)

plt.show()
