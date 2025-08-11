
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FPS = 60
DURATION_SECS = 5  # Duration in seconds
START_X = -1
END_X = 1
JUMP_HEIGHT = 0.5

# Generate initial positions for the lights
initial_positions = np.linspace(, END_X, NUM_LIGHTS
initial_positions = np.column_stack (initial_positions, np.zeros(NUM_LIGHTS)

# Function to update the positions of the lights
def update(frame_number):
    global initial_positions
    new_positions = np.copy(initial_positions)
    
    for i in range(NUM_LIGHTS):
        # Update position based on action
        if frame_number % int(FPS * 0.5) == 0: and i % 2 == 0:
            new_positions[i][0] += JUMP_HEIGHT
        
        # Apply gravity effect (simulating acceleration due to gravity
        new_positions[i][0] -= 0.01 * new_positions[i][0]
        
        # Wrap around the x-axis
        new_positions[i][0] %= 2
    
    # Update the initial_positions array
    initial_positions = new_positions
    
    # Plot the lights
    plt.cla()
    plt.scatter new_positions[:, 0], new_positions[:, 1], color='white'
    plt.axis([-2, 2, -1, 1])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Happy Man Jumping Forward')

# Create the animation
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=np.arange(0, DURATION_SECS * FPS), blit=True, interval=1000 / FPS)

plt.show()

