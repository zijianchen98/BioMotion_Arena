
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the function to create the animation
def animate_point_light(subject_action):
    # Define the number of frames and the duration per frame in milliseconds
    num_frames = 100
    duration_per_frame = 20

    # Initialize figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim((-1, 1)
    ax.set_ylim((-1, 1))
    ax.set_aspect('equal')
    ax.axis('off')

    # Background color
    ax.set_facecolor('black')

    # Generate random positions for the points
    points = np.random.rand(num_frames, 15, 2)

    def update(frame):
        ax.clear()  # Clear previous frame
        ax.set_facecolor('black')  # Reset background color
        
        # Calculate the mean position for the current frame
        mean_pos = np.mean(points[:frame], axis=0)
        
        # Draw the points with their mean position
        for i, pos in enumerate(points[frame]):
            circle = plt.Circle(pos, radius=0.05, color='white')
            ax.add_artist(circle)
            if i == 4:
                arrow = plt.Arrow(mean_pos[0], mean_pos[1], 0.2*(mean_pos[0] - pos[0]), 0.2*(mean_pos[1] - pos[1]), width=0.01, color='white')
                ax.add_artist(arrow)
        
        # Set title and update text
        ax.text(0.5, 0.9, f'Subject is {subject_action}', transform=ax.transAxes, fontsize=12, verticalalignment='top')
        ax.text(0.2, 0.8, f'Frame: {frame + 1} of {num_frames}', transform=ax.transAxes, fontsize=10, verticalalignment='top')
    
    anim = animation.FuncAnimation(fig, update, frames=num_frames, interval=duration_per_frame)
    
    return anim

# Call the function and display the animation
animate_point_light('s stimulus animation which represents biological motion. ' 'sittin g')
plt.show()

