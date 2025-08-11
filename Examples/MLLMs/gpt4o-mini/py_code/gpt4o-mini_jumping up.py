
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the positions of the points for a jumping motion
def jumping_motion(t):
    # Vertical positions for each point, simulating a jump
    jump_height = np.sin(t * np.pi) * 3  # Height varies with sine function
    # Base coordinates for the 'body' points
    positions = {
        'head': (0, 5 + jump_height), 
        'shoulders': [(0.5, 4 + jump_height), (-0.5, 4 + jump_height)],
        'elbows': [(0.75, 3 + jump_height), (-0.75, 3 + jump_height)],
        'hands': [(1, 2 + jump_height), (-1, 2 + jump_height)],
        'hips': [(0.5, 1 + jump_height), (-0.5, 1 + jump_height)],
        'knees': [(0.5, -1), (-0.5, -1)],
        'feet': [(0.5, -3), (-0.5, -3)],
    }
    
    # Extract all point positions and flatten the array
    all_positions = [positions['head']] + positions['shoulders'] + positions['elbows'] + positions['hands'] + positions['hips'] + positions['knees'] + positions['feet']
    return np.array(all_positions)

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 6)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # Initialize white points

# Initialize the animation
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    t = frame / 10  # Adjust speed of animation
    pos = jumping_motion(t)
    points.set_data(pos[:,0], pos[:,1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100, 1), init_func=init, blit=True)

# Show the animation
plt.show()
