
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create a point-light stimulus animation
def create_animation():
    # Define parameters
    num_points = 15
    duration = 5
    fps = 30
    
    # Initialize figure and axes
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim((-1, 1)
    ax.set_ylim((-1, 1))
    ax.set_facecolor('black')
    
    # Generate random positions for points
    positions = np.random.rand(num_points, 2) * 2 - 1
    
    # Function to update frame
    def update(frame):
        global positions
        
        # Smooth motion by averaging positions
        positions = np.roll(positions, 1, axis=0)
        positions[0] = np.sin(frame / duration * 2 * np.pi)
        
        # Update points
        for i, p in enumerate(positions):
            circle = plt.Circle(p, radius=0.05, color='white')
            ax.add_patch(circle)
            
        return tuple(circle)
    
    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=np.arange(duration * fps), interval=1000 / fps, blit=True)
    
    # Show animation
    plt.show()

# Call function to create animation
create_animation()
