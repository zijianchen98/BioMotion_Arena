
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create bowing motion
def create_bowing_motion(frames):
    # Initial positions of the 15 points (skeleton points)
    points = np.array([
        [0, 1],  # head
        [-0.5, 0.5], [0.5, 0.5],  # shoulders
        [-0.5, 0], [0.5, 0],  # elbows
        [-0.5, -0.5], [0.5, -0.5],  # hands
        [0, -1],  # hip
        [-0.3, -1.5], [0.3, -1.5],  # knees
        [-0.3, -2], [0.3, -2],  # ankles
        [0, -2.5],  # feet
    ])
    
    # Movement parameters
    bow_angle = np.linspace(0, np.pi / 4, frames)  # bowing movement
    weights = np.linspace(0, 0.1, frames)  # simulate weight effect on bowing
    
    # Create an array for each frame
    motion = []
    for i in range(frames):
        # Create a new frame by applying the bowing effect
        new_points = points.copy()
        new_points[:, 1] -= (weights[i] * np.sin(bow_angle[i]))  # lowering the body
        
        motion.append(new_points)
    
    return motion

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-3, 1)
ax.axis('off')  # Turn off the axis

# Generate the motion data
frames = 30
motion = create_bowing_motion(frames)

# Initialize points
scat = ax.scatter([], [], color='white')

# Updating function for animation
def update(frame):
    scat.set_offsets(motion[frame])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=100)

# Show the animation
plt.style.use('dark_background')
plt.show()
