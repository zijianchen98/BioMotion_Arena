
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the woman's body
points = {
    'head': [0, 1],
    'neck': [0, 0.8],
    'shoulder_left': [-0.2, 0.6],
    'shoulder_right': [0.2, 0.6],
    'elbow_left': [-0.4, 0.4],
    'elbow_right': [0.4, 0.4],
    'wrist_left': [-0.6, 0.2],
    'wrist_right': [0.6, 0.2],
    'hip_left': [-0.2, 0.2],
    'hip_right': [0.2, 0.2],
    'knee_left': [-0.4, 0],
    'knee_right': [0.4, 0],
    'ankle_left': [-0.6, -0.2],
    'ankle_right': [0.6, -0.2],
    'center_of_mass': [0, 0.4]
}

# Function to update the positions of the points for each frame
def update(frame):
    # Clear the previous frame
    plt.cla()
    
    # Update the positions of the points based on the running motion
    phase = frame / 100.0 * 2 * np.pi  # Phase of the motion
    for key, value in points.items():
        x, y = value
        if 'ankle' in key or 'knee' in key:
            y += 0.1 * np.sin(phase)
        elif 'wrist' in key or 'elbow' in key:
            y += 0.1 * np.sin(phase + np.pi)
        else:
            y += 0.05 * np.sin(phase)
        points[key] = [x, y]
    
    # Plot the updated positions
    for key, value in points.items():
        plt.plot(value[0], value[1], 'wo', markersize=10)
    
    # Set the plot limits and appearance
    plt.xlim(-1, 1)
    plt.ylim(-0.5, 1.5)
    plt.axis('off')
    plt.gca().set_facecolor('black')

# Create the figure
fig = plt.figure(figsize=(6, 6))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

# Show the animation
plt.show()
