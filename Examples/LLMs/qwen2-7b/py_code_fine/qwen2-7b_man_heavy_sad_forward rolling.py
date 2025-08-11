
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create a point-light stimulus animation
def sadman_forward_rolling():
    # Define the number of frames and duration of the animation
    num_frames = 100
    frame_duration = 0.05
    
    # Initialize figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim((-1, 1)
    ax.set_ylim((-1, 1))
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Background color
    ax.set_facecolor('#000000')
    
    # Initial positions for the point-lights (representing the sadman
    point_lights_positions = [(np.cos((theta), np.sin(theta)) for theta in np.linspace((0, 2*np.pi, 15)]
    
    def animate(frame):
        global point_lights_positions
        
        # Calculate the new positions for each point-light
        new_positions = [((x - 0.1 * np.sign(np.sin(frame)), y + 0.1 * np.sign(np.sin(frame))) for x, y in point_lights_positions]
        
        # Update the positions of the point-lights on the plot
        for i, (new_position in enumerate(new_positions):
            point_lights[i].set_xdata(new_position[0])
            point_lights[i].set_ydata(new_position[1])
            
        # Update the positions for the next frame
        point_lights_positions = new_positions
        
        return point_lights
    
    # Create the animation object
    sadman_animation = animation.FuncAnimation(fig, animate, frames=num_frames, interval=frame_duration, blit=True)
    
    # Show the animation
    plt.show()

# Run the function to display the animation
sadman_forward_roll()
