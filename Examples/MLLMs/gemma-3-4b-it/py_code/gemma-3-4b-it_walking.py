
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_walking_animation(duration=10):
    """
    Generates a point-light animation of a man walking.

    Args:
        duration (int): Duration of the animation in seconds.
    """

    # Define the number of points representing the body
    num_points = 15

    # Define the walking parameters
    step_length = 1.0
    step_width = 0.2  # Adjust for natural stride width
    leg_length = 0.3
    hip_height = 0.4
    head_height = 0.15
    arm_length = 0.4
    hand_length = 0.15

    # Create the initial positions of the points
    positions = np.zeros((num_points, 3))

    # Initial pose (standing)
    positions[0, 0] = 0.0
    positions[0, 1] = 0.0
    positions[0, 2] = hip_height
    
    positions[1:num_points//2, 0] = step_length * np.cos(np.linspace(0, np.pi, num_points//2))
    positions[1:num_points//2, 1] = -step_length * np.sin(np.linspace(0, np.pi, num_points//2))
    positions[1:num_points//2, 2] = hip_height
    
    positions[num_points//2:num_points, 0] = step_length * np.cos(np.linspace(np.pi, 2*np.pi, num_points//2))
    positions[num_points//2:num_points, 1] = -step_length * np.sin(np.linspace(np.pi, 2*np.pi, num_points//2))
    positions[num_points//2:num_points, 2] = hip_height
    
    positions[0, 0] = positions[1,0] + step_width
    positions[0, 1] = positions[1,1]
    positions[0, 2] = hip_height

    positions[num_points-1, 0] = positions[num_points//2-1, 0] - step_width
    positions[num_points-1, 1] = positions[num_points//2-1, 1]
    positions[num_points-1, 2] = hip_height

    # Create the figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Create the point-lights
    points = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

    # Create the animation
    def animate(i):
        # Update the positions of the points (simplified walking motion)
        for j in range(num_points):
          if j < num_points//2:
            positions[j, 0] = step_length * np.cos(np.linspace(0, np.pi, num_points//2)[j] + i*0.1)
            positions[j, 1] = -step_length * np.sin(np.linspace(0, np.pi, num_points//2)[j] + i*0.1)
          else:
            positions[j, 0] = step_length * np.cos(np.linspace(np.pi, 2*np.pi, num_points//2)[j] - i*0.1)
            positions[j, 1] = -step_length * np.sin(np.linspace(np.pi, 2*np.pi, num_points//2)[j] - i*0.1)
        points.set_offsets(positions)
        return points

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * 30), blit=True, repeat=True)

    # Save the animation (optional)
    # ani.save("walking_animation.gif", writer='pillow', fps=30)

    plt.show()


if __name__ == '__main__':
    generate_walking_animation(duration=10)
