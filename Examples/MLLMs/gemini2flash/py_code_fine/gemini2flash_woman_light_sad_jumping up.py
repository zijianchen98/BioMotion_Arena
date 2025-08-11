
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the animation function
def animate(i):
    # Clear the previous frame
    plt.cla()

    # Define the base positions of the points
    head = [0, 2]
    shoulder_l = [-0.5, 1.5]
    shoulder_r = [0.5, 1.5]
    elbow_l = [-1, 0.5]
    elbow_r = [1, 0.5]
    wrist_l = [-1.5, 0]
    wrist_r = [1.5, 0]
    hip_l = [-0.3, -0.5]
    hip_r = [0.3, -0.5]
    knee_l = [-0.5, -1.5]
    knee_r = [0.5, -1.5]
    ankle_l = [-0.7, -2.5]
    ankle_r = [0.7, -2.5]
    foot_l = [-0.8, -2.7]
    foot_r = [0.8, -2.7]

    # Define the amplitude of the jump
    jump_amplitude = 0.5

    # Define the frequency of the jump
    jump_frequency = 0.1

    # Calculate the vertical displacement based on the sine wave
    vertical_displacement = jump_amplitude * np.sin(2 * np.pi * jump_frequency * i)

    # Update the positions of the points based on the jump
    head[1] += vertical_displacement
    shoulder_l[1] += vertical_displacement
    shoulder_r[1] += vertical_displacement
    elbow_l[1] += vertical_displacement
    elbow_r[1] += vertical_displacement
    wrist_l[1] += vertical_displacement
    wrist_r[1] += vertical_displacement
    hip_l[1] += vertical_displacement
    hip_r[1] += vertical_displacement
    knee_l[1] += vertical_displacement
    knee_r[1] += vertical_displacement
    ankle_l[1] += vertical_displacement
    ankle_r[1] += vertical_displacement
    foot_l[1] += vertical_displacement
    foot_r[1] += vertical_displacement

    # Define the x and y coordinates of the points
    x = [head[0], shoulder_l[0], shoulder_r[0], elbow_l[0], elbow_r[0], wrist_l[0], wrist_r[0], hip_l[0], hip_r[0], knee_l[0], knee_r[0], ankle_l[0], ankle_r[0], foot_l[0], foot_r[0]]
    y = [head[1], shoulder_l[1], shoulder_r[1], elbow_l[1], elbow_r[1], wrist_l[1], wrist_r[1], hip_l[1], hip_r[1], knee_l[1], knee_r[1], ankle_l[1], ankle_r[1], foot_l[1], foot_r[1]]

    # Plot the points
    plt.plot(x, y, 'wo', markersize=8)

    # Set the limits of the plot
    plt.xlim([-2, 2])
    plt.ylim([-3, 3])

    # Set the background color to black
    plt.gca().set_facecolor('black')

    # Remove the axis labels
    plt.xticks([])
    plt.yticks([])

    # Set the title of the plot
    plt.title('Point-Light Stimulus Animation: Sad Woman Jumping Up', color='white')

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, interval=50)

# Show the animation
plt.show()
