
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and the angles to represent the motion
num_points = 15
angles = np.linspace(0, 2 * np.pi, num_points)

# Define the positions of the point-lights based on body joint locations
# Initial positions in terms of offset from the center
body_positions = [
    (0, 1),  # Head
    (-0.5, 0.75), (0.5, 0.75),  # Shoulders
    (-0.5, 0.5), (0.5, 0.5),  # Elbows
    (-0.5, 0.25), (0.5, 0.25),  # Hands
    (0, 0),  # Center of body
    (-0.5, -0.5), (0.5, -0.5),  # Knees
    (-0.5, -1), (0, -1.1), (0.5, -1)  # Feet
]

# Initialize positions as numpy array
points = np.array(body_positions)

# Function to update the points for the animation
def update_points(frame):
    plt.clf()  # Clear the current frame
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    
    # Rotation matrix for turning around
    angle = frame * 2.5 * np.pi / 30  # Adjust speed accordingly
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    
    # Apply rotation to each point
    rotated_points = np.dot(points, rotation_matrix)
    
    # Plot the points
    plt.plot(rotated_points[:, 0], rotated_points[:, 1], 'o', color='white', markersize=10) 
    plt.gca().set_facecolor('black')  # Set the background color to black

# Create a figure for the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update_points, frames=60, interval=100)

# Display the animation
plt.show()
