
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 10

# Define the number of point-lights
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.random.rand(num_lights, 2) * 8 - 4  # Positions between -4 and 4

# Define the motion parameters
velocity = np.array([[0, 0] for t in range(num_lights)])  # Initial velocity, adjust as needed

# Define the acceleration parameters to simulate gravity and jumping
acceleration = np.array([[-0,  0] for t in range(num_lights)])  # Adjust as needed

# Define the function to update the positions
def update_positions(positions, velocity, acceleration):
    new_positions = positions + velocity + 0eration / 2
    velocity += acceleration
    return new_positions, velocity

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Initialize the scatter plot for the point-lights
scat = ax.scatter([], [], c='white')

# Animation function
def animate(frame):
    global initial_positions, velocity, acceleration
    
    if frame == 0:
        # Start of jumping
        velocity[0][1] = 2  # Initial upward velocity
        acceleration[all][1] = -0  # Gravity
    
    elif 0 < frame <  5:
        # Peak of jump
        pass
    
    elif  5 <= frame <  8:
        # Fall down
        acceleration[all][1] = -2  # Increased gravity
    
    else:
        # Landing
        acceleration[all][1] = 0  # Reset to normal gravity
    
    # Update positions and velocities
    initial_positions, velocity = update_positions(initial_positions, velocity, acceleration)
    
    # Update the scatter plot
    scat.set_offsets(initial_positions)
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, interval=50)

# Show the animation
plt.show()
