
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the number of points and their initial positions
num_points = 15
points = np.zeros((num_points, 2))
points[:, 0] = np.linspace(-1, 1, num_points)
points[:, 1] = np.linspace(-1, 1, num_points)

# Define the colors and sizes of the points
colors = ['w'] * num_points
sizes = [10] * num_points

# Define the action (waving hand)
def waving_hand(frame):
    # Define the center of the hand
    hand_center = [0, 0]
    
    # Define the radius of the hand
    radius = 0.5
    
    # Define the angle of the hand
    angle = np.pi / 4 + np.sin(2 * np.pi * frame / 100) * np.pi / 2
    
    # Update the positions of the points
    for i in range(num_points):
        # Calculate the position of the point
        x = hand_center[0] + radius * np.cos(angle + i * np.pi / num_points)
        y = hand_center[1] + radius * np.sin(angle + i * np.pi / num_points)
        
        # Update the position of the point
        points[i, 0] = x
        points[i, 1] = y
    
    # Clear the axis
    ax.clear()
    
    # Set the axis limits
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    
    # Set the axis aspect ratio
    ax.set_aspect('equal')
    
    # Set the axis background color
    ax.set_facecolor('black')
    
    # Plot the points
    for i in range(num_points):
        ax.plot(points[i, 0], points[i, 1], 'o', color=colors[i], markersize=sizes[i])

# Create the animation
ani = animation.FuncAnimation(fig, waving_hand, frames=range(100), interval=20)

# Display the animation
plt.show()
