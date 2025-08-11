
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates and connections for the walking figure
# Simplify points that represent the human skeleton in the walking motion
def generate_walking_coordinates(t):
    """
    Generate coordinates for each frame of walking motion.
    :param t: Time parameter.
    :return: List of (x, y) points representing skeleton joints.
    """
    # Base positions for 'happyman' based on biomechanical plausible walking motion
    # Coordinates for 15 key points (head, 2 shoulders, 2 elbows, 2 hands, 
    # 2 hips, 2 knees, 2 feet)
    positions = [
        (0, 10),  # Head
        (-2, 8), (2, 8),  # Shoulders
        (-3 + 0.5 * np.sin(t), 6), (3 - 0.5 * np.sin(t), 6),  # Elbows (with swing)
        (-3 + np.sin(t), 4), (3 - np.sin(t), 4),  # Hands
        (-2, 4), (2, 4),  # Hips
        (-2 + 0.5 * np.sin(t), 2), (2 - 0.5 * np.sin(t), 2),  # Knees (with swing)
        (-2 + np.sin(t), 0), (2 - np.sin(t), 0)  # Feet (with swing)
    ]
    return positions

# Update the animation frame
def update(frame, ax):
    """
    Update the figure for each animation frame.
    """
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1, 11)

    # Generate the updated positions
    positions = generate_walking_coordinates(frame)

    # Plot each point
    for x, y in positions:
        ax.plot(x, y, 'o', color='white')

    # Optional: Connect body joints with lines here for coherence illustration
    connections = [
        (0, 1), (0, 2),  # Head to shoulders
        (1, 3), (3, 5),  # Left arm
        (2, 4), (4, 6),  # Right arm
        (1, 7), (2, 8),  # Shoulders to hips
        (7, 9), (9, 11),  # Left leg
        (8, 10), (10, 12)  # Right leg
    ]

    # Draw connections
    for start, end in connections:
        x_coords = [positions[start][0], positions[end][0]]
        y_coords = [positions[start][1], positions[end][1]]
        ax.plot(x_coords, y_coords, '-', color='white')


# Main function to execute animation
def main():
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 2 * np.pi, 0.1), fargs=(ax,), interval=100)
    plt.show()


if __name__ == "__main__":
    main()
