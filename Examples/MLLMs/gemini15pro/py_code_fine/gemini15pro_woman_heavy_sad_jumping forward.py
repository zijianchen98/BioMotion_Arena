
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 50], [-10, 40], [10, 40],  # Head
    [-20, 30], [20, 30],             # Shoulders
    [-25, 20], [25, 20],             # Elbows
    [-30, 10], [30, 10],             # Hands
    [-15, 10], [15, 10],            # Waist/hips
    [-15, -10], [15, -10],           # Knees
    [-15, -30], [15, -30]            # Feet / Ankles 
])


# Number of frames in the animation
num_frames = 60

# Create figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 60)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=6)



def animate(frame):
    # Calculate the positions of the points for the current frame
    x = initial_positions[:, 0] + 8 * np.sin(2 * np.pi * frame / num_frames) 
    y = initial_positions[:, 1] + 10 * np.sin(2 * np.pi * frame / (num_frames*2))

    y[12:] =  initial_positions[12:, 1] + 20 * np.abs(np.sin(2 * np.pi * frame / num_frames))
    y[10:12] =  initial_positions[10:12, 1] + 10 * np.abs(np.sin(2 * np.pi * frame / num_frames))



    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=40, blit=True)

plt.show()

