
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_jumping_animation(duration=10, fps=30):
    """
    Generates a point-light animation depicting a sad woman jumping up.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.
    """

    # Define the number of points
    num_points = 15

    # Define the movement pattern for the points (simplified for demonstration)
    # This is a highly simplified representation and would need to be 
    # refined for a truly biomechanically plausible animation.
    time = np.arange(0, duration, 1/fps)
    
    # Simplified jumping motion
    y_positions = np.sin(time * 2 * np.pi * 3) * 0.5 + 0.5  # Vertical movement
    z_positions = np.zeros_like(time) # Fixed Z position
    
    # Adjust positions for a sadwoman jump
    y_positions = np.clip(y_positions, 0.2, 0.9) # Limit vertical movement
    
    # Create the figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-0.5, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    # Create the points
    points, = ax.plot([], [], 'w.', markersize=5)

    # Animation function
    def animate(i):
        points.set_data(np.cos(time[i] * 2 * np.pi * 3), np.sin(time[i] * 2 * np.pi * 3))
        return points,

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=len(time), blit=True, repeat=False)

    # Save the animation
    ani.save('sad_woman_jumping.gif', writer='pillow', fps=fps)  # Use pillow writer

if __name__ == '__main__':
    generate_sad_woman_jumping_animation()
    print("Animation 'sad_woman_jumping.gif' generated.")
