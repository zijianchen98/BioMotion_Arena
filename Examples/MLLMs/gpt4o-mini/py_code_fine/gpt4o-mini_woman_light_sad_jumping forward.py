
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_frames = 60
num_points = 15
height = 10
width = 6
jump_height = 2.5

# Create point light positions for a sad woman jumping forward
def generate_positions(frame):
    angles = np.linspace(0, np.pi, num_points//3)
    
    # Base position for the jump
    base_positions = np.array([
        [0, 0],  # Center
        [-1, -0.5], [1, -0.5],  # Feet
        [-1, -1], [1, -1],  # Legs
        [-0.5, -1.5], [0.5, -1.5],  # Thighs
        [-1, -2], [1, -2],  # Pelvis
        [0, -3],  # Torso
        [-0.5, -3.5], [0.5, -3.5],  # Arms 
        [-1.5, -4], [1.5, -4],  # Shoulders
        [-1, -4.5], [1, -4.5]   # Head
    ])

    t = frame / num_frames
    leap = jump_height * np.sin(np.pi * t)  # Parabolic jump

    # Update positions with a forward jump
    positions = base_positions + np.array([0.05 * frame, leap])
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 2)
ax.set_facecolor('black')
points = ax.scatter([], [], c='white')

# Initialize the animation
def init():
    points.set_offsets([])
    return points,

# Update function for the animation
def update(frame):
    positions = generate_positions(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=True)

# Display the animation
plt.show()
