
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define number of point-lights
num_points = 15

# Initialize positions of the point-lights (assumed to be close to real human body joints)
points = np.array([
    [0, 7.5],   # Head
    [-1, 6],    # Left shoulder
    [1, 6],     # Right shoulder
    [-1, 4],    # Left elbow
    [1, 4],     # Right elbow
    [-1, 2],    # Left wrist
    [1, 2],     # Right wrist
    [0, 5],     # Torso
    [-1, 1],    # Left hip
    [1, 1],     # Right hip
    [-1, 0],    # Left knee
    [1, 0],     # Right knee
    [-1, -1.5], # Left ankle
    [1, -1.5],  # Right ankle
    [0, 4.5],   # Mid torso
    [0, 3]      # Pelvis
])

# Motion parameters
jump_height = 5
jump_distance = 10
frames = 60

def update_points(frame):
    plt.clf()
    plt.xlim(-12, 12)
    plt.ylim(-7, 10)
    plt.gca().set_facecolor('black')
    
    # Update vertical position to simulate jumping
    for i in range(num_points):
        vertical_movement = np.sin(np.pi * frame / frames) * jump_height
        horizontal_movement = frame / frames * jump_distance
        if i in [0, 1, 2, 7]:  # Head, shoulders, torso move up and forward
            points[i, 1] += vertical_movement
            points[i, 0] += horizontal_movement / 3  # Less forward for upper
        elif i in [3, 4, 5, 6]:  # Arms and wrists
            points[i, 1] += vertical_movement * 0.5
            points[i, 0] += horizontal_movement / 2
        elif i in [8, 9, 10, 11]:  # Legs
            points[i, 1] += vertical_movement * 0.3
            points[i, 0] += horizontal_movement
            
        # Draw point-light
        plt.plot(points[i, 0], points[i, 1], 'o', color='white')

# Set up the figure and animation
fig = plt.figure(figsize=(8, 10))
ani = animation.FuncAnimation(fig, update_points, frames=frames, interval=50)

# Show animation
plt.show()
