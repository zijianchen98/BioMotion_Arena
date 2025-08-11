
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frame_count = 100
weight_position = 1  # Vertical position for the weight

# Generate initial positions of the point-lights (15 points)
def initialize_points():
    points = np.zeros((num_points, 2))
    
    # Set points along the body
    points[0] = [0, 1]  # Head
    points[1] = [-0.5, 0.5]  # Left shoulder
    points[2] = [0.5, 0.5]  # Right shoulder
    points[3] = [-0.5, 0]  # Left elbow
    points[4] = [0.5, 0]  # Right elbow
    points[5] = [-0.5, -0.5]  # Left wrist
    points[6] = [0.5, -0.5]  # Right wrist
    points[7] = [0, -1]  # Torso
    points[8] = [-0.5, -1.5]  # Left hip
    points[9] = [0.5, -1.5]  # Right hip
    points[10] = [-0.5, -2]  # Left knee
    points[11] = [0.5, -2]  # Right knee
    points[12] = [-0.5, -2.5]  # Left ankle
    points[13] = [0.5, -2.5]  # Right ankle
    points[14] = [0, -3]  # Weight position in the middle

    return points

# Function to update the points frame by frame
def update(frame, points, scat):
    # Calculate walk motion
    for i in range(num_points):
        if i < 14:  # Ignore the main weight point
            points[i, 0] += np.sin(np.pi * frame / (frame_count / 2)) * 0.05 * (-1 if (i % 2 == 0) else 1)
            points[i, 1] += np.sin(np.pi * frame / (frame_count / 2)) * 0.02 * (-1 if (i % 2 == 0) else 1)
    
    # Update the scatter points
    scat.set_offsets(points)
    return scat,

# Main function to create the animation
def main():
    points = initialize_points()
    
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-4, 2)
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Create a scatter plot for the point-lights
    scat = ax.scatter(points[:, 0], points[:, 1], color='white')
    
    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=frame_count, fargs=(points, scat), blit=True)
    
    plt.show()

if __name__ == "__main__":
    main()
