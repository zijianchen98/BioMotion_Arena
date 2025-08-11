
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the animation function
def animate(i):
    # Clear the previous frame
    plt.cla()

    # Set the background color to black
    plt.gca().set_facecolor('black')

    # Define the x and y coordinates of the point lights for a running motion.
    # This is a simplified example, and a more realistic motion would require
    # a more complex model.
    # You can adjust these values to change the running motion.

    # Head
    x_head = 0 + 0.1 * np.sin(i * 0.1)
    y_head = 2.0

    # Shoulders
    x_shoulder_left = -0.5 + 0.2 * np.sin(i * 0.1 + np.pi/2)
    x_shoulder_right = 0.5 + 0.2 * np.sin(i * 0.1 + np.pi/2)
    y_shoulder = 1.5

    # Elbows
    x_elbow_left = -1.0 + 0.3 * np.sin(i * 0.1)
    x_elbow_right = 1.0 + 0.3 * np.sin(i * 0.1)
    y_elbow = 1.0

    # Hands
    x_hand_left = -1.5 + 0.4 * np.sin(i * 0.1 + np.pi/2)
    x_hand_right = 1.5 + 0.4 * np.sin(i * 0.1 + np.pi/2)
    y_hand = 0.5

    # Hips
    x_hip_left = -0.3 + 0.1 * np.sin(i * 0.1)
    x_hip_right = 0.3 + 0.1 * np.sin(i * 0.1)
    y_hip = 0.0

    # Knees
    x_knee_left = -0.7 + 0.4 * np.sin(i * 0.1 + np.pi/2)
    x_knee_right = 0.7 + 0.4 * np.sin(i * 0.1 + np.pi/2)
    y_knee = -1.0

    # Feet
    x_foot_left = -1.0 + 0.5 * np.sin(i * 0.1)
    x_foot_right = 1.0 + 0.5 * np.sin(i * 0.1)
    y_foot = -2.0

    # Create the point lights
    x = [x_head, x_shoulder_left, x_shoulder_right, x_elbow_left, x_elbow_right,
         x_hand_left, x_hand_right, x_hip_left, x_hip_right, x_knee_left,
         x_knee_right, x_foot_left, x_foot_right, 0.0, 0.0]
    y = [y_head, y_shoulder, y_shoulder, y_elbow, y_elbow, y_hand, y_hand,
         y_hip, y_hip, y_knee, y_knee, y_foot, y_foot, 1.3, -0.3]

    # Plot the point lights
    plt.plot(x, y, 'wo', markersize=8)

    # Set the axis limits
    plt.xlim(-2, 2)
    plt.ylim(-3, 3)

    # Remove the axis labels and ticks
    plt.axis('off')


# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, interval=50)

# Show the animation
plt.show()
