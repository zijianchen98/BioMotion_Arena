
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the number of points in the point-light display
num_points = 15

# Function to generate the point-light data for each frame
def generate_frame(frame_num):
    # Define the base positions of the points
    base_x = [0, 0, -0.3, 0.3, -0.7, 0.7, -0.2, 0.2, -0.8, 0.8, -0.1, 0.1, -0.6, 0.6, 0]
    base_y = [1, 0.5, 0.3, 0.3, 0, 0, -0.2, -0.2, -0.4, -0.4, -0.6, -0.6, -0.8, -0.8, 1.2]

    # Define the amplitude of the sine wave for each point
    amplitude_x = [0, 0, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0]
    amplitude_y = [0, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0]

    # Define the frequency of the sine wave for each point
    frequency_x = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    frequency_y = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    # Define the phase shift for each point
    phase_shift_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    phase_shift_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Calculate the x and y coordinates of each point for the current frame
    x = [base_x[i] + amplitude_x[i] * np.sin(2 * np.pi * frequency_x[i] * frame_num / num_frames + phase_shift_x[i]) for i in range(num_points)]
    y = [base_y[i] + amplitude_y[i] * np.sin(2 * np.pi * frequency_y[i] * frame_num / num_frames + phase_shift_y[i]) for i in range(num_points)]

    # Scale and center the points
    x = [i * 100 + 150 for i in x]
    y = [150 - i * 100 for i in y]

    return x, y

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scat = ax.scatter([], [], s=20, c='white')

# Define the animation function
def animate(frame_num):
    x, y = generate_frame(frame_num)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
