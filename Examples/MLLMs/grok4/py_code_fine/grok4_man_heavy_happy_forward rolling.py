
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the point-light animation
def update_frame(frame_num, scatters, num_points):
    # Define motion parameters
    rolling_angle = np.pi / 30  # Forward rotation angle per frame
    height_change = 0.05  # Height change simulating forward roll
    
    # Update positions of the points
    for i in range(num_points):
        # Calculate new position based on a simple forward roll
        angle = rolling_angle * frame_num + (i * np.pi / num_points)
        x_pos = np.cos(angle) * (1 + 0.1 * np.sin(frame_num * height_change))
        y_pos = np.sin(angle) * (1 + 0.1 * np.sin(frame_num * height_change))
        
        scatters[i].set_offsets([x_pos, y_pos])
    
    return scatters

def main():
    num_points = 15
    frames = 100  # Total number of frames for the animation

    # Initialize figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor('black')
    ax.axis('off')

    # Create scatter objects for point lights
    scatters = [ax.scatter([], [], s=100, color='white') for _ in range(num_points)]

    # Create the animation
    ani = animation.FuncAnimation(fig, update_frame, frames=frames, fargs=(scatters, num_points),
                                  interval=50, blit=True)

    plt.show()

if __name__ == "__main__":
    main()
