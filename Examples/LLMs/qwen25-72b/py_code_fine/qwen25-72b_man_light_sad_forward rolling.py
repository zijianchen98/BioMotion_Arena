
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a forward roll
def get_forward_roll_points(t):
    # t is the time parameter (0 to 1)
    # Define the positions of the 15 points for a forward roll
    points = np.zeros((15, 2))
    
    # Head
    points[0] = [0.5 + 0.2 * np.sin(2 * np.pi * t), 0.8 - 0.2 * np.cos(2 * np.pi * t)]
    
    # Shoulders
    points[1] = [0.4 + 0.2 * np.sin(2 * np.pi * t), 0.7 - 0.2 * np.cos(2 * np.pi * t)]
    points[2] = [0.6 + 0.2 * np.sin(2 * np.pi * t), 0.7 - 0.2 * np.cos(2 * np.pi * t)]
    
    # Elbows
    points[3] = [0.3 + 0.2 * np.sin(2 * np.pi * t), 0.6 - 0.2 * np.cos(2 * np.pi * t)]
    points[4] = [0.7 + 0.2 * np.sin(2 * np.pi * t), 0.6 - 0.2 * np.cos(2 * np.pi * t)]
    
    # Wrists
    points[5] = [0.2 + 0.2 * np.sin(2 * np.pi * t), 0.5 - 0.2 * np.cos(2 * np.pi * t)]
    points[6] = [0.8 + 0.2 * np.sin(2 * np.pi * t), 0.5 - 0.2 * np.cos(2 * np.pi * t)]
    
    # Hips
    points[7] = [0.4 + 0.2 * np.sin(2 * np.pi * t), 0.4 - 0.2 * np.cos(2 * np.pi * t)]
    points[8] = [0.6 + 0.2 * np.sin(2 * np.pi * t), 0.4 - 0.2 * np.cos(2 * np.pi * t)]
    
    # Knees
    points[9] = [0.3 + 0.2 * np.sin(2 * np.pi * t), 0.3 - 0.2 * np.cos(2 * np.pi * t)]
    points[10] = [0.7 + 0.2 * np.sin(2 * np.pi * t), 0.3 - 0.2 * np.cos(2 * np.pi * t)]
    
    # Ankles
    points[11] = [0.2 + 0.2 * np.sin(2 * np.pi * t), 0.2 - 0.2 * np.cos(2 * np.pi * t)]
    points[12] = [0.8 + 0.2 * np.sin(2 * np.pi * t), 0.2 - 0.2 * np.cos(2 * np.pi * t)]
    
    # Additional points for realism
    points[13] = [0.5 + 0.1 * np.sin(2 * np.pi * t), 0.6 - 0.1 * np.cos(2 * np.pi * t)]
    points[14] = [0.5 + 0.1 * np.sin(2 * np.pi * t), 0.5 - 0.1 * np.cos(2 * np.pi * t)]
    
    return points

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], c='white', s=10)

# Initialization function
def init():
    scat.set_offsets([])
    return scat,

# Animation update function
def update(frame):
    points = get_forward_roll_points(frame / 100)
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), init_func=init, blit=True)

# Show the animation
plt.show()
