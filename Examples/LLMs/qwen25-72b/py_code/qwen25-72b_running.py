
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing key joints of a running man
# These points are simplified and may need to be adjusted for more realism
points = [
    [0, 0],  # Hip
    [-0.1, 0.1],  # Knee (left)
    [-0.2, 0.2],  # Ankle (left)
    [0.1, 0.1],  # Knee (right)
    [0.2, 0.2],  # Ankle (right)
    [0, 0.5],  # Torso
    [0, 0.7],  # Neck
    [-0.1, 0.8],  # Shoulder (left)
    [0.1, 0.8],  # Shoulder (right)
    [-0.2, 0.9],  # Elbow (left)
    [0.2, 0.9],  # Elbow (right)
    [-0.3, 1.0],  # Wrist (left)
    [0.3, 1.0],  # Wrist (right)
    [0, -0.1],  # Foot (left)
    [0, -0.1]   # Foot (right)
]

# Convert points to a NumPy array for easier manipulation
points = np.array(points)

# Define the animation parameters
frame_rate = 60  # frames per second
total_frames = 120  # total number of frames
step_size = 0.05  # step size for each frame

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

def update(frame):
    global points
    # Update the positions of the points to simulate running
    for i in range(len(points)):
        if i in [0, 5, 6]:  # Hip, Torso, Neck
            points[i, 0] += step_size * np.sin(frame / 10)
        elif i in [1, 2, 4, 13, 14]:  # Left leg, Right leg, Left foot, Right foot
            points[i, 1] += step_size * np.sin(frame / 10)
        elif i in [3, 7, 8, 10, 11]:  # Right knee, Left shoulder, Right shoulder, Left elbow, Right elbow
            points[i, 1] -= step_size * np.sin(frame / 10)
        elif i in [9, 12]:  # Left wrist, Right wrist
            points[i, 0] += step_size * np.sin(frame / 10)
    
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/frame_rate, blit=True)

# Display the animation
plt.show()
