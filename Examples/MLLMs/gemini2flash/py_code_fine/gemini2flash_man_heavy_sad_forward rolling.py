
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=8)

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation in each frame
def animate(i):
    # Define the motion of the points for a 'sadman' rolling forward
    # This is a simplified example; actual motion capture data would be much more complex
    x = np.zeros(num_points)
    y = np.zeros(num_points)

    # Head
    x[0] = np.sin(i * 0.1) * 1.5
    y[0] = np.cos(i * 0.1) * 1.5 + 3

    # Shoulders
    x[1] = np.sin(i * 0.1 + 0.5) * 1 + 1
    y[1] = np.cos(i * 0.1 + 0.5) * 1 + 2.5
    x[2] = np.sin(i * 0.1 - 0.5) * 1 - 1
    y[2] = np.cos(i * 0.1 - 0.5) * 1 + 2.5

    # Elbows
    x[3] = np.sin(i * 0.1 + 1) * 1.5 + 2
    y[3] = np.cos(i * 0.1 + 1) * 1.5 + 1.5
    x[4] = np.sin(i * 0.1 - 1) * 1.5 - 2
    y[4] = np.cos(i * 0.1 - 1) * 1.5 + 1.5

    # Wrists
    x[5] = np.sin(i * 0.1 + 1.5) * 2 + 3
    y[5] = np.cos(i * 0.1 + 1.5) * 2 + 0.5
    x[6] = np.sin(i * 0.1 - 1.5) * 2 - 3
    y[6] = np.cos(i * 0.1 - 1.5) * 2 + 0.5

    # Hip
    x[7] = np.sin(i * 0.1) * 0.5 + 0.5
    y[7] = np.cos(i * 0.1) * 0.5 - 0.5
    x[8] = np.sin(i * 0.1) * 0.5 - 0.5
    y[8] = np.cos(i * 0.1) * 0.5 - 0.5

    # Knees
    x[9] = np.sin(i * 0.1 + 0.3) * 1 + 1
    y[9] = np.cos(i * 0.1 + 0.3) * 1 - 2
    x[10] = np.sin(i * 0.1 - 0.3) * 1 - 1
    y[10] = np.cos(i * 0.1 - 0.3) * 1 - 2

    # Ankles
    x[11] = np.sin(i * 0.1 + 0.6) * 1.5 + 1.5
    y[11] = np.cos(i * 0.1 + 0.6) * 1.5 - 3.5
    x[12] = np.sin(i * 0.1 - 0.6) * 1.5 - 1.5
    y[12] = np.cos(i * 0.1 - 0.6) * 1.5 - 3.5
    
    # Spine
    x[13] = np.sin(i * 0.1) * 0.2
    y[13] = np.cos(i * 0.1) * 0.2 + 1
    
    # Pelvis
    x[14] = np.sin(i * 0.1) * 0.3
    y[14] = np.cos(i * 0.1) * 0.3 - 1

    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, blit=True, repeat=True)

# Show the animation
plt.show()
