
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the coordinates for the happyman in a jumping forward action
def happyman_jumping_forward(subject_size, action_duration):
    # Define the initial position of the happyman (subject)
    x = 0
    y = 0
    # Define the speed of the subject
    speed = 1
    
    # Define the time steps for the animation
    time_steps = np.linspace((0, action_duration, 100)
    
    # Initialize arrays to store the x and y coordinates
    x_coords = []
    y_coords = []
    
    # Loop over the time steps
    for t in time_steps:
        # Calculate the x and y coordinates for the current time step
        x = speed * np.sin(((np.pi / 4) * t)
        y = speed * np.cos((np.pi / 4) * t) - subject_size / 2
        
        # Append the coordinates to the arrays
        x_coords.append(x)
        y_coords.append(y)
        
        # If the subject reaches the end of the screen, reset its position
        if x > 0:
            x = 0
            y += subject_size
        elif x < 0:
            x = 0
            y -= subject_size
    
    return x_coords, y_coords

# Function to create the animation
def create_animation(subject_size, action_duration):
    fig, ax = plt.subplots()
    ax.set_xlim(-subject_size, 2 * subject_size)
    ax.set_ylim(-subject_size, 2 * subject_size)
    ax.set_facecolor('black')
    
    x_coords, y_coords = happyman_jumping_forward(subject_size, action_duration)
    
    # Initialize the scatter plot
    scat = ax.scatter([], [], c='white', s=100)
    
    def update(frame):
        scat.set_offsets(np.c_[x_coords[frame], y_coords[frame]])
        return scat,
    
    ani = animation.FuncAnimation(fig, update, frames=len(x_coords), interval=20, blit=True)
    
    plt.show()

# Parameters
subject_size = 50
action_duration = 5

# Create the animation
create_animation(subject_size, action_duration)

