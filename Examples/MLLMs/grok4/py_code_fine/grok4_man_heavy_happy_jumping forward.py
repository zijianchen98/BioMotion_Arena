
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate jumping motion points
def generate_jump_frames(num_frames):
    # Initialize points - represent joints
    points = np.array([
        [0, 0],   # Center of mass
        [0.1, 0.3],  # Head
        [-0.1, 0.2], # Left Shoulder
        [0.1, 0.2],  # Right Shoulder
        [-0.1, 0.1], # Left Elbow
        [0.1, 0.1],  # Right Elbow
        [0, 0.1],    # Waist
        [-0.05, -0.2], # Left Leg
        [0.05, -0.2],  # Right Leg
        [-0.05, -0.3], # Left Foot
        [0.05, -0.3],  # Right Foot
    ])
    
    # Initialize an array to store the positions at each frame
    frames = []
    
    for i in range(num_frames):
        # Calculate vertical and horizontal displacement for jumping motion
        t = i / num_frames
        height = 0.5 * np.sin(np.pi * t)  # Simulate jumping effect
        forward_movement = 0.5 * t  # Move forward over time
        
        # Update points based on the calculated displacement
        updated_points = points + np.array([forward_movement, height])
        frames.append(updated_points)

    return frames

# Animation function
def update(frame):
    plt.clf()
    plt.xlim(-1, 2)
    plt.ylim(-1, 1)
    plt.axis('off')
    
    # Draw the points for the current frame
    for point in frame:
        plt.scatter(point[0], point[1], color='white', s=100)

# Set up the figure and animation
fig = plt.figure()
num_frames = 60  # Total number of frames
frames = generate_jump_frames(num_frames)

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/30)
plt.style.use('dark_background')
plt.show()
